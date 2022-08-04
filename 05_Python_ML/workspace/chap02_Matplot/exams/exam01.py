'''
문1) iris.csv 파일을 이용하여 다음과 같이 차트를 그리시오.
    <조건1> iris.csv 파일을 iris 변수명으로 가져온 후 파일 정보 보기
    <조건2> 1번 칼럼과 3번 칼럼을 대상으로 산점도 그래프 그리기
    <조건3> 1번 칼럼과 3번 칼럼을 대상으로 산점도 그래프 그린 후 5번 칼럼으로 색상 적용
            힌트) plt.scatter(x, y, c) 
'''

import pandas as pd
import matplotlib.pyplot as plt

# <조건1> iris.csv 파일을 iris 변수명으로 가져온 후 파일 정보 보기
path = r'C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML\data' # 경로 지정
iris = pd.read_csv(path + '/iris.csv')

print(iris.info())
'''
 0   Sepal.Length  150 non-null    float64
 1   Sepal.Width   150 non-null    float64
 2   Petal.Length  150 non-null    float64
 3   Petal.Width   150 non-null    float64
 4   Species       150 non-null    object
'''

# <조건2> 1번 칼럼과 3번 칼럼을 대상으로 산점도 그래프 그리기
plt.scatter(x=iris.iloc[:,0],y=iris.iloc[:,2])
plt.show()

# <조건3> 1번 칼럼과 3번 칼럼을 대상으로 산점도 그래프 그린 후 5번 칼럼으로 색상 적용
# 레이블 인코딩
from sklearn.preprocessing import LabelEncoder
encoder=LabelEncoder()
Species_Label=encoder.fit_transform(iris['Species'])
# 추가하기
iris['Species_Label']=Species_Label
# 확인
iris.info()
# 산점도 그래프 그리기
plt.scatter(x=iris['Sepal.Length'],y=iris['Petal.Length'],
            c=iris['Species_Label'])
