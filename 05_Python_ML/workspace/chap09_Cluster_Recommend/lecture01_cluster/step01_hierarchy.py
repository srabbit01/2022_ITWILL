'''
계층적 군집분석(Hierarchical Clustering) 
 - 상향식(Bottom-up)으로 계층적 군집 형성 
 - 유클리드안 거리계산식 이용 
 - 숫자형 변수만 사용 (등간척도 이상)
'''

from sklearn.datasets import load_iris # dataset
import pandas as pd # DataFrame
from scipy.cluster.hierarchy import linkage, dendrogram # 군집분석 tool
import matplotlib.pyplot as plt # 산점도 시각화 

# 1. dataset loading
iris = load_iris() # Load the data

X = iris.data # x변수 
y = iris.target # y변수(target) - 숫자형 : 거리계산 

# numpy -> DataFrame 
iris_df = pd.DataFrame(X, columns=iris.feature_names)
iris_df['species'] = y # target 추가 
iris_df.info()
'''
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   sepal length (cm)  150 non-null    float64
 1   sepal width (cm)   150 non-null    float64
 2   petal length (cm)  150 non-null    float64
 3   petal width (cm)   150 non-null    float64
 4   species            150 non-null    int32  
dtypes: float64(4), int32(1)
'''


# 2. 계층적 군집분석 
help(linkage)
clusters = linkage(iris_df, method='complete')
clusters # 좌표 생성
'''
method = 'complete' : default - 완전연결 
method = 'simple' : 단순연결
method = 'average' : 평균연결
'''
print(clusters)
# 유클리드 공간 확인
clusters.shape # (149, 4)

# 3. 덴드로그램 시각화 : 군집수는 사용자가 결정 
help(dendrogram)
plt.figure(figsize = (25, 10))
dendrogram(clusters)
plt.show()


# 4. 클러스터링 자르기
from scipy.cluster.hierarchy import fcluster # 클러스터 자르기 도구 

# 클러스터 자르기
help(fcluster)
cluster = fcluster(clusters, t=3, criterion='maxclust') 
# t=3, criterion='maxclust': 최대 클래스 수 = 3 으로 지정함 의미
'''
- t: 자를 군집의 개수
- criterion: 자르는 기준 (가본: maxclust)
  - maxclust: 거리 기준
  - ???
'''
print(cluster) # 1 ~ 3
'''
[1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 1 1 1 1 1 1 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 2 3 2 2 2 2 3 2 2 2 2
 3 2 3 3 2 2 2 2 3 2 3 2 3 2 2 3 3 2 2 2 2 2 3 3 2 2 2 3 2 2 2 3 2 2 2 3 2
 2 3] -> 각 행 별 데이터 군집 출력
'''
# 덴드로그램에서 보인 그룹 수 만큼 자르기
len(cluster) # 150
cluster.shape # (150,)

# raw dataset 칼럼 추가
iris_df['cluster']=cluster
iris_df.info()
'''
 5   cluster            150 non-null    int32  
 '''

# 산점도 시각화
plt.scatter(x=iris_df['sepal length (cm)'],
            y=iris_df['petal length (cm)'],
            c=iris_df['cluster'])
plt.show() 


# 5. 각 군집 별 특성분석

# 1) group_by: 그룹객체 생성
cluster_group=iris_df.groupby('cluster')
cluster_group.size() # 각 군집 별 크기 반환
'''
cluster
1    50
2    34
3    66
'''

# 2) 각 군집의 평균
cluster_group.mean()
'''
         sepal length (cm)  sepal width (cm)  ...  petal width (cm)   species
cluster                                       ...                            
1                 5.006000          3.428000  ...          0.246000  0.000000
2                 6.888235          3.100000  ...          2.123529  2.000000
3                 5.939394          2.754545  ...          1.445455  1.242424
'''
