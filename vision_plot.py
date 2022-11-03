import matplotlib.pyplot as plt
import pandas as pd

# Pandas로 csv 파일 읽기
# index_col : 인덱스로 지정할 컬럼 선택
table = pd.read_csv("vision2016.csv", index_col=2)
# print(table)

# 그래프 그리기
fig = plt.figure()
# print(fig)
# 1, 1, 1 -> 1*1 그리드, 첫번째 서브 플롯
ax = fig.add_subplot(1, 1, 1)

# 데이터 프레임으로부터 특정 컬럼의 값 가져오기 : 데이터 프레임의 인덱싱 방법
# df.loc["row", "column"]
# t = table.loc["bad"]
# n = table.loc["notbad"]
# o = table.loc["good"]
# f = table.loc["soso"]
# print(t)# print(n)# print(o)# print(f)

# 서브 플롯 전용 - 지정한 레이블을 임의의 색으로 칠하기
def scatter(label, color):
    data = table.loc[label]
    # print(data)
    # 산포도 그리는 함수 : 해당하는 서브플롯.scatter(x축값, y축값, 컬러, 라벨)
    ax.scatter(data["Left"], data["Right"], c=color, label=label)

scatter("notbad", "yellow")
scatter("bad", "red")
scatter("good", "blue")
scatter("soso", "pink")

ax.legend()     # 범례(데이터 종류를 나타내는 텍스트) 표시
plt.savefig("vision-plot2016.png")     # 이미지 저장
# plt.show()