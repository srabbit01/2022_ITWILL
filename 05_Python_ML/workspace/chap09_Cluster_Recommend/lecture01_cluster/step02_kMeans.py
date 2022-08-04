# -*- coding: utf-8 -*-
"""
step02_kMeans.py

kMeans 알고리즘 
 - 확인적 군집분석 
 - 군집수 k를 알고 있는 분석방법 
"""

import pandas as pd # DataFrame 
from sklearn.cluster import KMeans # model 
import matplotlib.pyplot as plt # 군집결과 시각화 
import numpy as np # array 


# 1. text file -> dataset 생성 
path=r"C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML"
file = open(path+'/data/testSet.txt')
lines = file.readlines() # list 반환 

print(lines)

dataset = [] # 2차원(80x2)
for line in lines : # '1.658985\t4.285136\n'
    cols = line.split('\t') # '1.658985'  '4.285136\n'
    
    rows = [] # 1줄 저장 
    for col in cols : # '1.658985' -> '4.285136\n'
        rows.append(float(col)) # 실수화: 1.658985 
        
    dataset.append(rows) # [[1.658985, 4.285136],...] # 중첩 리스트 형식
        
print(dataset) # 중첩 list   

# list : 1d -> numpy(array) : 2d
dataset_arr = np.array(dataset)

dataset_arr.shape # (80, 2)
print(dataset_arr)


# 2. numpy -> DataFrame(column 지정)
data_df = pd.DataFrame(dataset_arr, columns=['x', 'y'])
data_df.info()
'''
RangeIndex: 80 entries, 0 to 79
Data columns (total 2 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   x       80 non-null     float64
 1   y       80 non-null     float64
'''


# 3. KMeans model 생성 
model = KMeans(n_clusters=4, max_iter=300, algorithm='auto')
'''
- n_clusters: 군집 수 (기본: 8)
- max_iter: 반복 학습 횟수 (기본: 300)
- algorithm: 군집 분석에 사용되는 알고리즘 (기본: auto)
- n_init: 초기 중심 위치 시도 횟수 (기본: 10)
'''

model.fit(data_df) # 학습 수행 

# 현재 적용된 dataset 예측된 레이블 (cluster 번호)
cluster_lables=model.labels_ # 현재 dataset 적용
print(cluster_lables) # 0 ~ 3
'''
[3 1 2 0 3 1 2 0 3 1 2 0 3 1 2 0 3 1 2 0 3 1 2 0 3 1 2 0 3 1 2 0 3 1 2 0 3
 1 2 0 3 1 2 0 3 1 2 0 3 1 2 0 3 1 2 0 3 1 2 0 3 1 2 0 3 1 2 0 3 1 2 0 3 1
 2 0 3 1 2 0]
'''

# 예측치 생성 
pred = model.predict(data_df) # new dataset 적용
print(pred) # 0 ~ 3


# 군집 중앙값 
centers = model.cluster_centers_
print(centers) # 각 군집 별 중앙값
'''
     x           y
0 [[-3.38237045 -2.9473363 ]
1  [-2.46154315  2.78737555]
2  [ 2.80293085 -2.7315146 ]
3  [ 2.6265299   3.10868015]]
'''
type(centers) # numpy.ndarray

# clusters 시각화 : 예측 결과 확인 
# data_df['predict'] = pred # 칼럼추가 
data_df['labels'] = cluster_lables
data_df.info()

# 산점도 
plt.scatter(x=data_df['x'], y=data_df['y'], 
            c=data_df['labels'])

# 중앙값 추가 
plt.scatter(x=centers[:,0], y=centers[:,1], 
            c='r', marker='D')
plt.show()










