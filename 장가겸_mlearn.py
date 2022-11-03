from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import pandas as pd


# 양쪽 시력 데이터 csv 파일로부터 읽기
tabel = pd.read_csv("vision.csv")
# print(tabel)
# print(type(tabel))    # DataFrame

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
# clf = svm.LinearSVC()
clf.fit(train_data, train_label)

# 예측
pre = clf.predict(test_data)

# 결과
ac_score = metrics.accuracy_score(test_label, pre)
cl_report = metrics.classification_report(test_label, pre)
print(f"정확도 : {ac_score}")
print(f"리포트 : {cl_report}")
