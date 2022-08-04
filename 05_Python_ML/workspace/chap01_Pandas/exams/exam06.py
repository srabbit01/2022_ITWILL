'''   
문6) iris.csv 파일을 읽어와서 다음과 같이 처리하시오.
   <단계1> 1~4 칼럼 대상 vector 생성(col1, col2, col3, col4)    
   <단계2> 1,4 칼럼 대상 합계, 평균, 표준편차 구하기 
   <단계3> 1,2 칼럼과 3,4 칼럼을 대상으로 각 df1, df2 데이터프레임 생성
   <단계4> df1과 df2 칼럼 단위 결합 iris_df 데이터프레임 생성      
'''

import pandas as pd
import os
os.chdir(r'C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML\data') # file 경로 변경 

iris = pd.read_csv('iris.csv')
print(iris.info())

# <단계1> 1~4 칼럼 대상 vector 생성(col1, col2, col3, col4)    
col1 = iris['Sepal.Length']
col2 = iris['Sepal.Width']
col3 = iris['Petal.Length']
col4 = iris['Petal.Width']

# <단계2> 1,4 칼럼 대상 합계, 평균, 표준편차 구하기
sub1=pd.concat(objs=[col1,col4],axis=1)
sub1.sum() # 합계
'''
Sepal.Length    876.5
Petal.Width     179.9
dtype: float64
'''
sub1.mean() # 평균
'''
Sepal.Length    5.843333
Petal.Width     1.199333
dtype: float64
'''
sub1.std() # 표준편차
'''
Sepal.Length    0.828066
Petal.Width     0.762238
dtype: float64
'''

# <단계3> 1,2 칼럼과 3,4 칼럼을 대상으로 각 df1, df2 데이터프레임 생성
df1=pd.concat(objs=[col1,col2],axis=1)
df2=pd.concat(objs=[col3,col4],axis=1)

# <단계4> df1과 df2 칼럼 단위 결합 iris_df 데이터프레임 생성
iris_df=pd.concat(objs=[df1,df2],axis=1)
iris_df.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 150 entries, 0 to 149
Data columns (total 4 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   Sepal.Length  150 non-null    float64
 1   Sepal.Width   150 non-null    float64
 2   Petal.Length  150 non-null    float64
 3   Petal.Width   150 non-null    float64
dtypes: float64(4)
memory usage: 4.8 KB
'''