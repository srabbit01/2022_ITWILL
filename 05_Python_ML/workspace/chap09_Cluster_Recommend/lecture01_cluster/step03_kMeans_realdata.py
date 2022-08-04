# -*- coding: utf-8 -*-

'''
UCI ML Repository 데이터셋 url
https://archive.ics.uci.edu/ml/datasets.php
'''

### 기본 라이브러리 불러오기
import pandas as pd
pd.set_option('display.max_columns', 100) # 콘솔에서 보여질 최대 칼럼 개수 
import matplotlib.pyplot as plt


'''
[Step 1] 데이터 준비 : 도매 고객 데이터셋 
 - 도매 유통업체의 고객 관련 데이터셋으로 다양한 제품 범주에 대한 연간 지출액을 포함  
'''
# 출처: UCI ML Repository
uci_path = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00292/Wholesale%20customers%20data.csv'
df = pd.read_csv(uci_path)
df.info() # 변수 및 자료형 확인
'''
RangeIndex: 440 entries, 0 to 439
Data columns (total 8 columns):
 #   Column            Non-Null Count  Dtype
---  ------            --------------  -----
 0   Channel           440 non-null    int64 : 유통업체 : Horeca(호텔/레스토랑/카페) 또는 소매(명목)
 1   Region            440 non-null    int64 : 지역 : Lisnon,Oporto 또는 기타(명목) - 리스본,포르토(포르투갈)  
 2   Fresh             440 non-null    int64 : 신선함 : 신선 제품에 대한 연간 지출(연속)
 3   Milk              440 non-null    int64 : 우유 : 유제품에 대한 연간 지출(연속)
 4   Grocery           440 non-null    int64 : 식료품 : 식료품에 대한 연간 지출(연속)
 5   Frozen            440 non-null    int64 : 냉동 제품 : 냉동 제품에 대한 연간 지출(연속)
 6   Detergents_Paper  440 non-null    int64 : 세제-종이 : 세제 및 종이 제품에 대한 연간 지출(연속)
 7   Delicassen        440 non-null    int64 : 델리카슨 : 델리카트슨(수입식품) 제품(연속)
'''

'''
[Step 2] 데이터 탐색
'''

# 데이터 살펴보기
print(df.head())  

# 명목형 변수 
df.Channel.value_counts()
'''
1    298 -> Horeca
2    142 -> 소매
'''

# 연속형 변수 
df.Region.value_counts()
'''
3    316 -> 기타
1     77 -> Lisnon
2     47 -> Oporto
'''

# 연속형 변수: 요약통계량
df.describe()
'''
          Channel      Region          Fresh          Milk       Grocery  \
count  440.000000  440.000000     440.000000    440.000000    440.000000   
mean     1.322727    2.543182   12000.297727   5796.265909   7951.277273   
std      0.468052    0.774272   12647.328865   7380.377175   9503.162829   
min      1.000000    1.000000       3.000000     55.000000      3.000000   
25%      1.000000    2.000000    3127.750000   1533.000000   2153.000000   
50%      1.000000    3.000000    8504.000000   3627.000000   4755.500000   
75%      2.000000    3.000000   16933.750000   7190.250000  10655.750000   
max      2.000000    3.000000  112151.000000  73498.000000  92780.000000   

             Frozen  Detergents_Paper    Delicassen  
count    440.000000        440.000000    440.000000  
mean    3071.931818       2881.493182   1524.870455  
std     4854.673333       4767.854448   2820.105937  
min       25.000000          3.000000      3.000000  
25%      742.250000        256.750000    408.250000  
50%     1526.000000        816.500000    965.500000  
75%     3554.250000       3922.000000   1820.250000  
max    60869.000000      40827.000000  47943.000000  
'''


'''
[Step 3] 데이터 전처리
'''

# 분석에 사용할 변수 선택
X = df.copy() # 내용 복제본 생성

# 설명변수 데이터 정규화
from sklearn.preprocessing import StandardScaler # 표준화 
X = StandardScaler().fit_transform(X) # numpy 객체로 반환 -> describe 사용 불가능
# numpy -> pandas
X_pandas=pd.DataFrame(X)
X_pandas.describe()

'''
[Step 4] k-means 군집 모형 - sklearn 사용
'''

# sklearn 라이브러리에서 cluster 군집 모형 가져오기
from sklearn.cluster import KMeans

# 모형 객체 생성 
kmeans = KMeans(n_clusters=5, n_init=10, max_iter=300)
'''
Parameters
----------
n_clusters : int, default=8
n_init : int, default=10 - centroid seeds -> 중심점 seed 값
max_iter : int, default=300
'''
        
# 모형 학습
kmeans.fit(X)  # KMeans(n_clusters=5) 

# 군집 예측 
cluster_labels = kmeans.labels_ # 예측된 레이블(Cluster 번호)    
print(cluster_labels)
pd.value_counts(cluster_labels)
'''
0    209
1    126
4     91
2     10 -> 제외
3      4 -> 제외
# 군집 내 데이터 수가 적은 것은 제외하기
'''

# 군집 수가 3개인 경우
kmeans2 = KMeans(n_clusters=3, n_init=10, max_iter=300).fit(X)
cluster_labels2 = kmeans2.labels_
pd.value_counts(cluster_labels2)
'''
1    297
0    130
2     13
'''

# 군집 수가 2개인 경우
kmeans3 = KMeans(n_clusters=2, n_init=10, max_iter=300).fit(X)
cluster_labels3 = kmeans3.labels_
pd.value_counts(cluster_labels3)
'''
1    304
0    136
'''

# 데이터프레임에 예측된 레이블 추가
df['Cluster'] = cluster_labels
print(df.head())   

# 상관관계 분석 
r = df.corr()
r['Grocery']
'''
Channel             0.608792
Region              0.007696
Fresh              -0.011854
Milk                0.728335
Grocery             1.000000
Frozen             -0.040193
Detergents_Paper    0.924641 -> 매우 상관성이 높음
Delicassen          0.205497
Cluster             0.050995
'''

# 그래프로 표현 - 시각화
# 상관변수가 높은 변수끼리 시각화하는 것이 좋음
df.plot(kind='scatter', x='Grocery', y='Detergents_Paper', c='Cluster', 
        cmap='Set1', colorbar=True, figsize=(15, 10))
'''
- cmap: 색상
- colorbar: True면 colorbar 표시
  -> colorbar: 숫자형 범주 별 색상 막대 형태로 표기
'''
plt.show()  

# 3군집과 2군집(군집 특성 X -> 분산되어 분포) 외 -> 0, 1, 4번 군집 
mask=(df['Cluster']==3)|(df['Cluster']==2) # 2, 3 True, 0, 1, 4 False
new_df=df[~mask] # 부정: ~
new_df.plot(kind='scatter', x='Grocery', y='Detergents_Paper', c='Cluster', 
        cmap='Set1', colorbar=True, figsize=(15, 10))

'''
[Step 5] 각 cluster별 특성 분석
'''
# 1) 그룹화
newdf_group=new_df.groupby('Cluster')

# 그룹 별 데이터 수 구하기
newdf_group.size()
'''
Cluster
0    209
1    126
4     91
'''

# 그룹 별 평균 구하기
newdf_group.mean()
'''
          Channel    Region         Fresh         Milk       Grocery  \
Cluster                                                                
0        1.000000  3.000000  13297.947368  3168.306220   3740.588517   
1        2.000000  2.674603   8130.031746  8874.071429  14139.150794   
4        1.054945  1.307692  12183.945055  3254.714286   4130.923077   

              Frozen  Detergents_Paper   Delicassen  
Cluster                                              
0        3436.971292        769.392344  1262.511962  
1        1339.476190       6104.936508  1542.706349  
4        3458.252747        860.263736  1149.934066  
'''

# 2) 명목형 변수
cluster1=new_df[new_df['Cluster']==0]
cluster2=new_df[new_df['Cluster']==1]
cluster3=new_df[new_df['Cluster']==4]
# 그룹 별 Channel 범주 확인
cluster1.Channel.value_counts() # 1(206)
cluster2.Channel.value_counts() # 2(126)
cluster3.Channel.value_counts() # 1(86) + 2(5)
# 그룹 별 Region 범주 확인
cluster1.Region.value_counts() # 3(209)
cluster2.Region.value_counts() # 3(97) + 2(17) + 1(12)
cluster3.Region.value_counts() # 1(63) + 2(28)

# 연속형 변수
cluster1.describe().iloc[1,:]
'''
Channel                 1.000000
Region                  3.000000
Fresh               13297.947368
Milk                 3168.306220
Grocery              3740.588517
Frozen               3436.971292
Detergents_Paper      769.392344
Delicassen           1262.511962
Cluster                 0.000000
'''
cluster2.describe().iloc[1,:]
'''
Channel                 2.000000
Region                  2.674603
Fresh                8130.031746
Milk                 8874.071429
Grocery             14139.150794
Frozen               1339.476190
Detergents_Paper     6104.936508
Delicassen           1542.706349
Cluster                 1.000000
'''
cluster3.describe().iloc[1,:]
'''
Channel                 1.054945
Region                  1.307692
Fresh               12183.945055
Milk                 3254.714286
Grocery              4130.923077
Frozen               3458.252747
Detergents_Paper      860.263736
Delicassen           1149.934066
Cluster                 4.000000
'''