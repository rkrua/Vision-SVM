def calc_bmi(h, w):
    bmi = w / (h/100) ** 2
    if bmi < 18.5:
        return "thin"
    elif bmi < 23 :
        return "normal"
    elif bmi < 25 :
        return "Obesity"
    return "fat"



# 출력 파일 준비하기 : bmi.csv
fp = open("bmi.csv", "w",encoding="utf-8")
fp.write("height,weight,label\r\n")

# 무작위로 데이터 생성하기
cnt = {"thin":0, "normal":0, "Obesity":0, "fat":0}
for i in range(20000):
    h = random.randint(120, 200)
    w = random.randint(35, 90)
    label = calc_bmi(h, w)
    # print(f"신장 : {h}\t몸무게 : {w}\t 결과 : {label}")
    cnt[label] += 1
    fp.write(f"{h},{w},{label}\r\n")
fp.close()