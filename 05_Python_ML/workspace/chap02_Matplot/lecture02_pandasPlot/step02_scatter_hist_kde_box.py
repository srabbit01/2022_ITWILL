# -*- coding: utf-8 -*-
"""
Pandas 객체 시각화 : 연속형 변수 시각화  
 kind = hist, kde, scatter, box 등 
"""

import pandas as pd
import numpy as np # dataset 
import matplotlib.pyplot as plt # chart

# file 경로 
path = r'C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML\data' # 경로 지정

# 1. 산점도 
dataset = pd.read_csv(path + '/dataset.csv')
print(dataset.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 217 entries, 0 to 216
Data columns (total 7 columns):
 #   Column    Non-Null Count  Dtype  
---  ------    --------------  -----  
 0   resident  217 non-null    int64  
 1   gender    217 non-null    int64  
 2   job       205 non-null    float64
 3   age       217 non-null    int64  
 4   position  208 non-null    float64
 5   price     217 non-null    float64
 6   survey    217 non-null    int64  
 '''

# 연속형 변수 
plt.scatter(dataset['age'], dataset['price'], c=dataset['gender'])
plt.show()


# 2. hist, kde, box
# DataFrame 객체 
df = pd.DataFrame(np.random.randn(100, 4),
               columns=('one','two','three','fore'))

# 1) 히스토그램
df['one'].plot(kind = 'hist', title = 'histogram') # 계급 별 출현 빈도수
plt.show()

# 2) 커널밀도추정 : 히스토그램에 밀도분포곡선 추정
df['one'].plot(kind = 'kde', title='kernel density plot') # 분포곡선 표시
plt.show()

# 3) 박스플롯
df.plot(kind='box', title='boxplot chart')
plt.show()

