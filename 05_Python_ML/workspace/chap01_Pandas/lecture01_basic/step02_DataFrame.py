# -*- coding: utf-8 -*-
"""
step02_DataFrame.py

DataFrame 자료구조 특징 
 - 2차원 행렬구조(DB의 Table 구조와 동일함)
 - 칼럼 단위 상이한 자료형 
 - Series -> DataFrame
"""

import pandas as pd # 별칭 -> pd.DataFrame()
from pandas import DataFrame # DataFrame()


# 1. DataFrame 객체 생성 

# 1) list와 dict 이용 
names = ['hong', 'lee', 'kim', 'park']
ages = [35, 45, 55, 25]
pays = [250, 350, 450, 250]

# key -> 칼럼명, value -> 칼럼값 
frame = pd.DataFrame({'name':names, 'age': ages, 'pay': pays})
frame.index
# R: data.frame(name=names,age=ages,pay=pays)
type(frame) # pandas.core.frame.DataFrame
print(frame)
'''
   name  age  pay
0  hong   35  250
1   lee   45  350
2   kim   55  450
3  park   25  250
'''

# 객체 정보 
frame.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 4 entries, 0 to 3 -> 관측치
Data columns (total 3 columns): -> 칼럼(변수)
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   name    4 non-null      object = 문자형
 1   age     4 non-null      int64 = 정수형
 2   pay     4 non-null      int64 = 정수형
dtypes: int64(2), object(1)
memory usage: 224.0+ bytes
'''
# 모양 확인 (행/열 수 반환)
frame.shape # (4, 3) = 4행 3열
gender=pd.Series(['M','F','M','F']) # 1차원
frame['gender']=gender # 칼럼추가
frame['gender']=['M','F','M','F']
'''
   name  age  pay gender
0  hong   35  250      M
1   lee   45  350      F
2   kim   55  450      M
3  park   25  250      F
'''
pay=frame.pay # DF.column(R: DF$column)
type(pay) # pandas.core.series.Series
pay.mean() # 325.0

# 2) numpy 객체 이용
# 모든 자료형이 숫자형인 경우, 사용하는 것이 유리
import numpy as np # 수치과학용 패키지
np.arange(12)
data = np.arange(12).reshape(3, 4) # 1d -> 2d
# arange(): 0~n번까지 한 줄 값 만들기
# reshape(행,열): 행/열 구조로 만들기
print(data) 

# numpy -> pandas
frame2 = DataFrame(data, columns=['a','b','c','d'])
frame2
'''
   a  b   c   d
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
'''
frame2.columns # Index(['a', 'b', 'c', 'd'], dtype='object')
# pandas -> numpy
values=frame2.values
'''
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
'''
type(values) # numpy.ndarray = 고차원 배열 구조
frame2.info()

# 행/열 단위 통계
frame2.mean(axis=0) # axis: 행(0) 혹은 열(1) 지정 (기본: 행=0)
# = 같은 열 모음 = 열 단위 평균
frame2.mean(axis=1) # 열축
# = 같은 행 모음 = 행 단위 평균

# 2. DF 칼럼 참조 
# 경로 지정
path = r'C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML\data' # 경로 지정
# csv 파일 불러오기
emp = pd.read_csv(path + "/emp.csv", encoding='utf-8')
'''
    No Name  Pay
0  101  홍길동  150
1  102  이순신  450
2  103  강감찬  500
3  104  유관순  350
4  105  김유신  400
'''
print(emp.info())


# 1) 단일 칼럼 : 단일 list 
no = emp.No # 방법1 = DF.column -> 칼럼명 내 점(.)이 존재 등 일부 사용 불가능
# ex) iris.Sepal.Length
name = emp['Name'] # 방법2 = DF['column']
# iris['Sepal.Length'] # 앞은 객체 뒤는 값으로 인식
no2=emp['No']
print(no)
print(name)
print(name[1:])

pay = emp.Pay[2:] # 방법1
print(pay)

pay = emp['Pay'] # 방법2
type(pay) # pandas.core.series.Series

pay.plot() # 1d : 선그래프 
print('급여 평균 :', pay.mean()) # 급여 평균 : 370.0


# 2) 복수 칼럼 : 중첩 list 
df = emp[['No','Pay']] # old DF -> new DF
#emp[['No':'Pay']] # SyntaxError  

print(df)
df.plot() # 2d : 선그래프
# 2개 이상이기 때문에 자동으로 범례 생성
col = ['No', 'Pay'] # list
print(emp[col])


# 3. subset 만들기 : old DF -> new DF

# 1) 특정 칼럼 제외 : 특정 칼럼 선택(칼럼수가 작은 경우)
subset1 =  emp[['Name', 'Pay']] # 가장 기본적인 subset 생성
print(subset1)

# 2) 특정 행 제외 
subset2 = emp.drop(1) # 2행 제외 : 현재 object 변경 없음 
# 특정 행 색인으로 넣어주면 그것을 제외한 새로운 DF 생성
# 만일 변수 없으면 의미 X
print(subset2)


# 3) 조건식으로 행 선택 
subset3 = emp[emp.Pay > 350] # ex) 급여가 350 이하 관측치 제외 
# 1, 2, 4 행만 추출
print(subset3)

# 4) 칼럼수가 많은 경우: 복수 칼럼 (2개 이상의 칼럼 선택)
iris=pd.read_csv(path+'/iris.csv')
iris.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 150 entries, 0 to 149
Data columns (total 5 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   Sepal.Length  150 non-null    float64
 1   Sepal.Width   150 non-null    float64
 2   Petal.Length  150 non-null    float64
 3   Petal.Width   150 non-null    float64 = 연속 숫자형 (실수형)
 4   Species       150 non-null    object = 범주형(문자형)
dtypes: float64(4), object(1)
memory usage: 6.0+ KB
'''
cols=list(iris.columns) # iris 칼럼 객체 -> list 변수명만 반환
'''
['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width', 'Species']
'''
iris_x=iris[cols[:4]] # 4개의 칼럼 추출: iris.Sepal.Length로 추출 불가능
# cols[:4] = ['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width'] 의미
iris_x
iris_x.shape # 행/열 개수 반환 = (150, 4)

iris_y=iris['Species'] # = [cols[-1]] # 결과 위와 동일
iris_y
iris_y.shapae # (150, 1) = 2d = 2차원
# 만일, 1d = 1차원(벡터)
type(iris_y) # pandas.core.series.Series

# 칼럼 단위 연산
print('칼럼 단위 평균 :',iris_x.mean(axis=0))
'''
칼럼 단위 평균 : 
Sepal.Length    5.843333
Sepal.Width     3.057333
Petal.Length    3.758000
Petal.Width     1.199333
dtype: float64
'''

# 각 범주 별 빈도수 확인
iris_y.value_counts()
'''
setosa        50
versicolor    50
virginica     50
Name: Species, dtype: int64
'''
iris_y.unique()
# array(['setosa', 'versicolor', 'virginica'], dtype=object)

# 5) 논리연산자 이요한 조건식
iris_x.head() # 앞부분 5개
iris_x.tail() # 뒷부분 5개
# Sepal.Length > 5 and Petal.Length < 1.7
# iris[iris['Sepal.Length']>5 and iris['Petal.Length']<1.7] # ValueError
iris_sub=iris[np.logical_and(iris['Sepal.Length']>5,iris['Petal.Length']<1.7)]
'''
관계 연산자 사용
np.logical_and(): 그리고
np.logical_or(): 또는
np.logical_not(): 아니다
np.logical_xor()
'''
iris_sub.shape # (17, 5) -> 조건을 두어 일부 행만 추출 가능

# 4. DataFrame 행열 참조 
'''
DF.loc[행,열]: 명칭(이름) 기반 (숫자는 명칭의 의미로 사용 가능)
DF.iloc[행,열]: 숫자 기반(0~n)
'''
print(emp)
'''
칼럼: 명칭
행: 숫자
    No Name  Pay
0  101  홍길동  150
1  102  이순신  450
2  103  강감찬  500
3  104  유관순  350
4  105  김유신  400
'''

# 1) loc 속성 : 명칭 기반 
# LOC에서 숫자 사용 =  숫자를 명칭으로 해석함 
# 즉, '앞:뒤'에서 뒤 포함
emp.loc[0, :] # 1행 전체 
emp.loc[0] # 열 생략 가능 
emp.loc[0,['No','Pay']] # 비연속 칼럼: 문자형의 경우, 여러개 지정 시 리스트로 묶기
emp.loc[0,'No':'Pay'] # 연속 칼럼

emp.loc[0:2] # 1~3행 전체 
emp.loc[1:3,'No':'Name']

# 2) iloc 속성 : 숫자(integer) 위치 기반
# ILOC에서 숫자 사용 =  숫자를 숫자로 해석함  
# 즉, '앞:뒤'에서 뒤 제외
emp.loc[0] # 1행 전체 
emp.iloc[0] # 1행 전체 -> 열 전체 생략 가능 
# emp.iloc[0:2,'No':'Name'] # 명칭 사용 시, TypeError
emp.iloc[0:2,0:2]
emp.iloc[0:2] # 1~2행 전체 
emp.iloc[:,1:] # 2번째 칼럼 이후 연속 칼럼 선택
