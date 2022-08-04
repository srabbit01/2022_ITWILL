# -*- coding: utf-8 -*-
"""
문2) 아래와 같은 단계로 kMeans 알고리즘을 적용하여 확인적 군집분석을 수행하시오.

 <조건> 변수 설명 : tot_price : 총구매액, buy_count : 구매횟수, 
                   visit_count : 매장방문횟수, avg_price : 평균구매액

  단계1 : 3개 군집으로 군집화
 
  단계2: 원형데이터에 군집 예측치 추가
  
  단계3 : tot_price 변수와 가장 상관계수가 높은 변수로 산점도(색상 : 클러스터 결과)
  
  단계4 : 산점도에 군집의 중심점 시각화

   단계5 : 군집별 특성분석 : 우수고객 군집 식별
"""

import pandas as pd
from sklearn.cluster import KMeans # kMeans model
import matplotlib.pyplot as plt

path=r"C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML"
sales = pd.read_csv(path+"/data/product_sales.csv")
print(sales.info())
'''
RangeIndex: 150 entries, 0 to 149
Data columns (total 4 columns):
tot_price      150 non-null float64 -> 총구매금액 
visit_count    150 non-null float64 -> 매장방문수 
buy_count      150 non-null float64 -> 구매횟수 
avg_price      150 non-null float64 -> 평균구매금액 
'''

# 단계1 : 3개 군집으로 군집화
model = KMeans(n_clusters=3, max_iter=300, algorithm='auto')
model=model.fit(sales)

# 단계2: 원형데이터에 군집 예측치 추가
cluster_lables=model.labels_
sales['labels'] = cluster_lables

# 단계3 : tot_price 변수와 가장 상관계수가 높은 변수로 산점도(색상 : 클러스터 결과)
sales.corr()['tot_price']
'''
tot_price      1.000000
visit_count    0.817954
buy_count     -0.013051
avg_price      0.871754 -> 가장 상관계수 높음
labels         0.349480
'''
plt.scatter(x=sales['avg_price'], y=sales['tot_price'], 
            c=sales['labels'])

# 단계4 : 산점도에 군집의 중심점 시각화
centers = model.cluster_centers_
plt.scatter(x=centers[:,3], y=centers[:,0], 
            c='r', marker='D')

# 단계5 : 군집별 특성분석 : 우수고객 군집 식별
sales_g=sales.groupby('labels')
sales_g.size()
'''
labels
0    62
1    50
2    38
'''
sales_g.mean()
'''
        tot_price  visit_count    avg_price
labels                                              
0        5.901613     1.433871   2.754839   4.393548
1        5.006000     0.244000   3.284000   1.464000
2        6.850000     2.071053   3.071053   5.742105
'''

# 가장 우수 고객 집단 생성
vip=sales.loc[sales['labels']==2] # 38
vip.info()
vip
