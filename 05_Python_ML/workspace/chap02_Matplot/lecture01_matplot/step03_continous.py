# -*- coding: utf-8 -*-
"""
step03_continous.py

 연속형 변수 시각화 : 산점도, 히스토그램, 박스 플롯 
"""

import numpy as np # 수치 data 생성 
import matplotlib.pyplot as plt # data 시각화 
import pandas as pd

# 차트에서 한글 지원 
plt.rcParams['font.family'] = 'Malgun Gothic'
# 음수 부호 지원 
import matplotlib
matplotlib.rcParams['axes.unicode_minus'] = False


# 차트 자료 생성: 1:1로 일치해야 함
data1 = np.arange(-3, 7) # -3 ~ 6
data2 = np.random.randn(10) # N(0,1): 표준 정규분포 난수 10개

# 1. 산점도 
plt.scatter(x=data1, y=data2, c='r', marker='o')
plt.title('scatter plot')
plt.show()

# 여러가지 색상의 산점도: 범주형 변수(더미변수)
cdata=np.random.randint(1,4,10) # 정수형 난수 생성 # 1이상 ~ 4미만 (1,4] 10개 생성 
cdata # array([2, 2, 3, 1, 2, 2, 1, 1, 2, 3])
# 숫자별 색상이 약속되어 있음 -> 1: 진파랑, 2: 진초록, 3: 노랑 등

plt.scatter(x=data1, y=data2, c=cdata, marker='o')
plt.title('scatter plot')
plt.show()

# 2. 히스토그램 : 대칭성 
data3 = np.random.normal(0, 1, 2000) # N(0,1^2) # 정규분포 난수 생성
data4 = np.random.normal(0, 2, 2000) # N(0,2^2) # (평균,표준편차,개수)

# 난수 통계
data3.mean() # -0.017565342386895593
data3.std() # 1.011900994607206

# 정규분포 시각화 
plt.hist(data3, bins=100, density=True, label='data3')
plt.hist(data4, bins=100, density=True, label='data4')
plt.legend(loc = 'best') # 범례 
plt.show()
'''
loc 속성값 
lower left/right
center left/right
upper left/right
'''

# 3. 박스 플롯(box plot)
data5 = np.random.random(100) # 0~1  난수 100개
print(data5)
data.shape # (100,) = 1차원

# 요약 통계량: numpy -> pandas
df=pd.Series(data5) # 1차원의 판다스 객체 생성
df.describe()
'''
count    100.000000
mean       0.532861
std        0.280083
min        0.023208
25%        0.284230
50%        0.543745
75%        0.765438
max        0.992228
dtype: float64
'''

plt.boxplot(data5)
plt.show()













