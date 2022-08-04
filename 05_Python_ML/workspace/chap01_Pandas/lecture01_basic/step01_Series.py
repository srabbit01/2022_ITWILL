# -*- coding: utf-8 -*-
"""
step01_Series.py

Series 객체 특징 
 - pandas 1차원(vector) 자료구조 (list와 유사)
 - DataFrame의 칼럼 구성요소 
 - 수학/통계 관련 함수(method) 제공 
 - indexing/slicing 기능 = 자료 순서 존재
"""

import pandas as pd # 별칭 -> pd.Series()
from pandas import Series # class -> Series()

# 1. Series 객체 생성 

# 1) list 이용 
price = pd.Series([3000,2000,1000,5200]) # 생성자 -> object
print(price) # 색인 따로 지정하지 않으면 기본 색인 지정
'''
0    3000
1    2000
2    1000
3    5200
dtype: int64 # 데이터형
'''
price[0] # 3000
price[3] # 5200

type(price) # pandas.core.series.Series

idx = price.index # 색인 반환 
values = price.values # 값 반환  

print(idx) # RangeIndex(start=0, stop=4, step=1): 0~3
print(values) # [3000 2000 1000 5200]

# index 적용
price2=pd.Series([3000,2000,1000,5200],index=['a','b','c','d'])
'''
a    3000
b    2000
c    1000
d    5200
dtype: int64
'''
price2['a'] # 3000
price2[0] # 3000
print(price2.index)

# 튜플
price3=pd.Series((000,2000,1000,5200),index=[1,2,3,4])
print(price3.index)
price3[1]

# 2) dict 이용 
person = Series({'name':'홍길동', 'age':35, 'addr':'서울시'}) 
print(person)
'''
name    홍길동
age      35
addr    서울시
dtype: object = 2가지 이상의 자료형인 경우
'''
print(person.index)
print(person.values)

# 2. indexing/slicing 
ser = Series([4, 4.5, 6, 8, 10.5])  
print(ser)
'''
0     4.0
1     4.5
2     6.0
3     8.0
4    10.5
dtype: float64 -> 자료형 통일 
'''
ser[:] # 전체 원소 
ser[0] # 1번 원소 
ser[:3] # start~2번 원소 
ser[3:] # 3~end 원소 
# ser[-1] # KeyError: -1

ser2=ser[2:]
ser2

id(ser) # 1963434322048
id(ser2) # 1963434322048

# 3. Series 결합과 NA 처리 
s1 = pd.Series([3000, None, 2500, 2000],
               index = ['a', 'b', 'c', 'd'])

s2 = pd.Series([4000, 2000, 3000, 1500],
               index = ['a', 'c', 'b', 'd'])


# Series 결합(사칙연산)
s3 = s1 + s2 # 덧셈 (같은 index 기준)
# 반드시 s1 및 s2 내 값은 숫자형 혹은 결측치(None) 중 하나여야 함
print(s3)
'''
a    7000.0
b       NaN -> 연산 불가능
c    4500.0
d    3500.0
dtype: float64
'''

# 결측치 처리: 상수 혹은 통계 결과로 대체
result = s3.fillna(s3.mean()) # 결측치가 있으면 평균으로 대체
print(result)
'''
a    7000.0
b    5000.0
c    4500.0
d    3500.0
dtype: float64
'''

result2 = s3.fillna(0) # 결측치가 있으면 0으로 대체
print(result2)
'''
a    7000.0
b       0.0
c    4500.0
d    3500.0
dtype: float64
'''

# 결측치 제거 
result3 = s3[pd.notnull(s3)]
print(result3)
'''
a    7000.0
c    4500.0
d    3500.0
dtype: float64
'''
s3[s3>=3000] # 부울리언 색인 

# 4. Series 연산 

# 1) 블럭 수정 
print(ser)
ser[1:4] = 5.0
print(ser)

# list 블럭 수정 불가능
lst=[1,2,3,4,5]
# lst[1:4]=5 # TypeError

# 2) broadcast 연산 
# - 서로 다른 차원 간 연산
# - 차원이 큰 쪽으로 개수 늘어난 후 1:1 연산
# 1차원(vector) * 0차원(scala)
print(ser * 0.5) # 직접 산술 연산 가능 -> 각 원소 별 5.0 더하기 가능
'''
0    2.00
1    2.50
2    2.50
3    2.50
4    5.25
dtype: float64
'''
# print(lst * 0.5) # TypeError
# 1차원(vector) + 0차원(scala)
print(ser+2)

# 3) 수학/통계 함수: 결측치가 존재하면 그 외 값 연산
# 객체.메서드 = object.method()
ser.mean() #  5.9
ser.sum() # 29.5
ser.var() #  6.8
ser.std() # 2.6076809620810595
ser.max() # 10.5
ser.min() # 4.0

# 각 범주 별 빈도수
ser.value_counts()
'''
5.0     3
10.5    1
4.0     1
dtype: int64
'''

# 범주 확인
ser.unique()# array([ 4. ,  5. , 10.5])

# 최빈수
ser.mode() # 5.0

# 객체 내 다양한 메서드
dir(s3)

##########################
## 결측치 (NaN, None)
##########################
'''
- NaN: Not a Number
- 잘못 입력으로 인해 계산할 수 없는 기호
- ex) 음수의 제곱근
'''
from statistics import sqrt # 제곱근
import numpy as np # np.NaN
# numpy에서 None은 결측치로 인식하지 X

test = pd.Series([10,-20])
test

sqrt(test[0]) # 3.1622776601683795
sqrt(test[1]) # ValueError

# 결측치 입력
# 판다스 입력 결측치: None, np.NaN
test2=pd.Series([10,np.NaN,None]) # np 데이터는 자동으로 실수형으로 인식됨
sqrt(test2[1]) # nan
# np.NaN=결측치
# 결측치 -> 결측치 관련 함수 사용 가능 (isna, isnull 메서드) -> 두가지 사용 가능
# 결측치 감지하기 위해 결측치로 전환 필요

# 결측치 유무 확인
test2.isna() # 결측치 존재 =  TRUE, 결측치 존재 X = FALSE
'''
0    False
1     True
dtype: bool
'''
test2.isnull() # isna()와 동일한 기능
'''
0    False
1     True
dtype: bool
'''
help(test2.isna)
help(test2.isna)

# isnull() 반대
test2.notnull() # 결측치 X 존재 = TRUE, 결측치 = FALSE 
'''
0  True
1  False
'''
# 결측치 제거 시 사용
test2[test.notnull()]

# NaN va None
arr1=np.array([10,20.3,np.NaN])
arr1 # array([10. , 20.3,  nan])
arr1.sum() # nan

arr2=np.array([10,20.3,None])
arr2 # array([10, 20.3, None], dtype=object)
arr2.sum() # TypeError

test3=pd.Series([10,None]) # None=값이 없음
sqrt(test3[1]) # nan
'''
'None' 사용하지 않는 이유
- Pandas 내 연산속도 느림
- Numpy에서는 TypeError 발생
'''