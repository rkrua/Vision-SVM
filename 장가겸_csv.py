import random

# 시력을 측정하는 함수
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

# 출력 파일 준비하기 : bmi.csv
fp = open("vision.csv", "w",encoding="utf-8")
fp.write("Left,Right,label\r\n")

# 무작위로 데이터 생성하기
cnt = {"bad":0, "notbad":0, "soso":0, "good":0}
for i in range(20000):
    l = random.uniform(0.01, 2.0)

    # 실제 짝눈이 너무 심한사람은 오차범위 밖이기에 제외
    r = random.uniform(l-0.8, l+0.8)

    # 설정한 차이에서, 너무 높아질 경우 데이터 조정(그래프를 위함)
    if r <= 0:
        r = 0.1
    elif r > 2:
        r = 2

    l = round(l, 2)
    r = round(r, 2)
    label = calc_vision(l, r)
    print(f"왼쪽눈 : {l}\t오른쪽눈 : {r}\t 결과 : {label}")
    cnt[label] += 1
    fp.write(f"{l},{r},{label}\r\n")
fp.close()
# print(cnt)
print('ok')





