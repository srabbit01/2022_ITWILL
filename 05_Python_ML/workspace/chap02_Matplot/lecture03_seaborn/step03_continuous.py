#step03_continuous

# 연속형 변수 시각화 
# - 산점도, 산점도 행렬, boxplot 

import matplotlib.pyplot as plt
import seaborn as sn

# seaborn 한글과 음수부호, 스타일 지원 
sn.set(font="Malgun Gothic", 
            rc={"axes.unicode_minus":False}, style="darkgrid")
# style: white, dark, whitegrid, darkgrid, ticks

# dataset load 
iris = sn.load_dataset('iris')
tips = sn.load_dataset('tips')


x = iris.sepal_length

# 1. distplot: 히스토그램 + 밀도분포곡선
sn.distplot(x, hist=True, kde=True)
# hist: 히스토그램 출력 여부
# kde: 카널 밀도 곡선 출력 여부
plt.title('iris Sepal length hist & kde')
plt.show()


# 2. 산점도 행렬(scatter matrix)  
# sn.pairplot(data=데이터셋, hue='범주형변수',kind='scatter')
sn.pairplot(data=iris, hue='species',kind='scatter') 
plt.show()


# 3. 산점도 : 연속형+연속형   
sn.scatterplot(x="sepal_length", y="petal_length",
               data=iris,hue='species')
plt.title('산점도 행렬(scatter matrix)')
plt.show()

# 4. box plot
sn.boxplot(x='day',y='total_bill',hue='sex',data=tips)
plt.title('성별을 기준으로 요일별 총 지불 금액 현황')

tips.info()

