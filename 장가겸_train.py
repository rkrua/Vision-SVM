import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import random

def calc_vision(l, r):
    v_accuracy = l-r
    v_rate = (l+r) * 5

    #짝눈이 심할경우
    if abs(v_accuracy) >= 0.5 :
        return "bad"

    # 시력이 낮을경우(운전면허 기준 2종 불통)
    elif v_rate < 5 :
        return "bad"

    # 보통 시력인경우(운전면허 기준 1종 불통 / 2종 합격)
    elif v_rate < 8:
        return "notbad"

    # 운전면허 기준 1종 합격
    elif v_rate <= 10 and l >0.5 and r >0.5:
        return "soso"

    # 좋은 시력 / 운전면허 시력검사 최대치
    return "good"


# 데이터 정제 (시력데이터)
csv =[]
with open('국가건강검진_시력데이터.csv', 'r', encoding='utf-8') as fp:
    # 한줄씩 읽기
    for line in fp:
        line = line.strip()     # 줄바꿈 제거
        # print(line)
        cols = line.split(',')  #쉼표를 구분자로 데이터 분할
        csv.append(cols)
del csv[0]
random.shuffle(csv)

# 학습에 이용할 최종 csv 파일 생성
fn = open("vision2016.csv", "w", encoding="utf-8")
fn.write("Left,Right,label\r\n")

# 정제한 데이터 분류
cnt = {"bad": 0, "notbad": 0, "soso": 0, "good": 0}
for i in range(20000):
    l = float(csv[i][2])
    r = float(csv[i][3])
    if l == 9.9:            # 왼쪽 눈이 실명일 때
        l = 0.1
    if r == 9.9:            # 오른쪽 눈이 실명일 때
        r = 0.1
    label = calc_vision(l, r)
    cnt[label] += 1
    fn.write(f"{l},{r},{label}\r\n")
fn.close()

# 양쪽 시력 데이터 최종 csv 파일로부터 읽기
tabel = pd.read_csv("vision2016.csv")

# 컬럼(열)을 자르고 정규화하기
label = tabel["label"]
# print(label)
l = tabel["Left"]
# print(l)
r = tabel["Right"]
# print(r)

# concat : 여러개의 동일 형태 데이터 프레임을 합칠 때 사용
# axis = 0 인 경우, 세로(위+아래) 병합
# axis = 1 인 경우, 가로(왼+오) 병합
lr = pd.concat([l,r], axis=1)
# print(lr)

# 학습 데이터와 테스트 데이터 분할(default = 75%, 25%)
# test_size : 테스트 데이터 셋 비율
# shuffle   : 데이터 섞을지 여부 설정 (default = True(섞음))
train_data, test_data, train_label, test_label = \
    train_test_split(lr, label, test_size=0.25, shuffle=True)
# print(train_data)
# print(train_label)

# 학습
clf = svm.SVC()
clf.fit(train_data, train_label)

# 예측
pre = clf.predict(test_data)

# 결과
ac_score = metrics.accuracy_score(test_label, pre)
cl_report = metrics.classification_report(test_label, pre)
print(f"정확도 : {ac_score}")
print(f"리포트 : {cl_report}")
