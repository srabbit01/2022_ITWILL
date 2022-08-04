
# -*- coding: utf-8 -*-
"""
random 모듈
 - 난수 생성 함수 제공 
"""

import numpy as np # 별칭 
import matplotlib.pyplot as plt # 그래프

# 1. 난수 실수와 정수  

# 1) 난수 실수 : [0, 1) = 0 <= R < 1 = 0 이상 1 이하
data = np.random.rand(5, 3) # (행, 열)
print(data)
# 30개 이상인 경우 중심극한 정리에 의해 평균 0.5에 근접

# 차원 모양
print(data.shape) # (5, 3) -> (300, 400)

# 난수 통계
print(data.min()) # 0.08132439151228676
print(data.max()) # 0.9462959398267136
print(data.mean()) # 0.63050758946005
print(data.std())

# 2) 난수 정수 : [a, b) 
data = np.random.randint(165, 175, size=50) # (행, 열)
print(data)

# 차원 모양
print(data.shape) # (50,)

# 난수 통계
print(data.min()) # 165
print(data.max()) # 174
print(data.mean()) # 169.78


# 2. 정규분포
height = np.random.normal(173, 5, 2000) # N(173, 5^2)
print(height) # (2000,) -> 난수 2000개 생성

height2 = np.random.normal(173, 5, (500, 4))# N(173, 5^2)
print(height2) # (500, 4)


# 난수 통계
print(height.mean()) # 173.64868062947306
print(height2.mean()) # 173.38566887645658

# 정규분포 시각화 
plt.hist(height, bins=100, density=True, histtype='step')
plt.hist(height, bins=100, density=False, histtype='step')
plt.hist(height, bins=100, density=True)
# density: True면
# histtype: 히스토그램 선형 타입 (step: 막대 그래프 다각형 형식)
plt.show()


# 3. 표준정규분포: N(0,1) = 표준화된 표준 정규분포
standNormal = np.random.randn(500, 3)
print(standNormal.mean()) # -0.04444361993656145

# normal 함수 이용 
standNormal2 = np.random.normal(0, 1, (500, 3))
print(standNormal2.mean())


# 정규분포 시각화 
plt.hist(standNormal[:,0], 
         bins=100, density=True, histtype='step', label='col1')
plt.hist(standNormal[:,1], 
         bins=100, density=True, histtype='step', label='col2')
plt.hist(standNormal[:,2], 
         bins=100, density=True, histtype='step',label='col3')
plt.legend(loc='best')
plt.show()

# 4. 균등분포: uniform(a,b,n) = [a,b)
# sample data가 서로 균등하게 분포되어 있는 것
uniform=np.random.uniform(-1,0,1000) # -1 ~ 0
plt.hist(uniform,bins=15,density=True)

uniform.min()
uniform.max()

# 5. DataFrame sampling

import pandas as pd

path = r'C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML\data'

## csv file 가져오기
wdbc = pd.read_csv(path + '/wdbc_data.csv')
print(wdbc.info())
'''
RangeIndex: 569 entries, 0 to 568
Data columns (total 32 columns):
    '''

# 1) seed값 적용 
np.random.seed(123) # 매번 동일한 난수 생성하기 위해
# 생성한 난수 기억하기 위해

# 2) pandas sample() 이용  
wdbc_df = wdbc.sample(400) # seed 사용하지 않으면 매번 다른 난수 생성
print(wdbc_df.shape) #  (400, 32)
print(wdbc_df.head())
'''
          id diagnosis  ...  symmetry_worst  dimension_worst
333   894090         B  ...          0.2293          0.06037
273  8610175         B  ...          0.2618          0.07609
201    90745         B  ...          0.2965          0.07662
178   857010         M  ...          0.3799          0.09185
85      8913         B  ...          0.2309          0.06915

[5 rows x 32 columns]
'''

# 3) training vs test sampling
idx = np.random.choice(a = len(wdbc), size = int(len(wdbc) * 0.7),
       replace = False)
'''
a: 전체 관측치 개수
size: sample 개수
replace: True면 복원 추출, False면 중복 샘플링하지 않음(비복원)
'''
print(idx) # 전체 중 70% 숫자 랜점 추출

# train_set: 70%
train=wdbc.iloc[idx,:] # 해당 행 70% 추출
train.shape # (398, 32)

train.head()
'''
          id diagnosis  ...  symmetry_worst  dimension_worst
196  9010018         M  ...          0.2654          0.09438
544  8610862         M  ...          0.5440          0.09964
530  8912909         B  ...          0.2465          0.09981
182   891923         B  ...          0.2823          0.06794
156  8911800         B  ...          0.2335          0.06263

[5 rows x 32 columns]
'''

# test_set: 30%
# list + for = list 내포
test_idx=[i for i in range(len(wdbc)) if i not in idx] # list 내포
len(test_idx) # 171
test=wdbc.iloc[test_idx,:]
test.shape # (171, 32)

wdbc.iloc[~(idx),:].shape
