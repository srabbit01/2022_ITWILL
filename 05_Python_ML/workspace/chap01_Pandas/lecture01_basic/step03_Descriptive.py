# -*- coding: utf-8 -*-
"""
step03_Descriptive.py

1. DataFrame의 요약통계량 
2. 상관계수
"""

import pandas as pd 

path = r'C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML\data' # 경로 지정
product = pd.read_csv(path + '/product.csv')


# DataFrame 정보 보기 
product.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 264 entries, 0 to 263
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   a       264 non-null    int64
 1   b       264 non-null    int64
 2   c       264 non-null    int64
'''

# 앞부분/뒷부분 관측치 5개 보기 
product.head()
product.tail()

# 1. DataFrame의 요약통계량 
summ = product.describe()
print(summ)
'''
                a           b           c
count  264.000000  264.000000  264.000000 = 길이
mean     2.928030    3.132576    3.094697 = 평균
std      0.970345    0.859657    0.828744 = 표준편차
min      1.000000    1.000000    1.000000 = 최솟값
25%      2.000000    3.000000    3.000000 = 제1사분위수
50%      3.000000    3.000000    3.000000 = 중앙값 = 제2사분위수
75%      4.000000    4.000000    4.000000 = 제3사분위수
max      5.000000    5.000000    5.000000 = 최댓값
'''

# 행/열 통계
product.shape # (264, 3)
product.sum(axis = 0) # 행축: 같은 열의 모음
product.sum(axis = 1) # 열축: 같은 행의 모음 -> 행 단위 합계

# 산포도 : 분산, 표준편차 
product.var() # axis = 0
product.std() # axis = 0

# 빈도수 : 집단변수 
product['a'].value_counts()


# 유일값 
product['b'].unique()
# array([4, 3, 2, 5, 1], dtype=int64)


# 2. 상관관계 
cor = product.corr()
print(cor) # 상관계수 행렬 
'''
          a         b         c
a  1.000000  0.499209  0.467145
b  0.499209  1.000000  0.766853
c  0.467145  0.766853  1.000000
'''


