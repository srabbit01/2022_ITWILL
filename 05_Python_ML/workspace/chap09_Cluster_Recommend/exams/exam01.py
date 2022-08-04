'''
 문) 신입사원 면접시험(interview.csv) 데이터 셋을 이용하여 다음과 같이 군집모델을 생성하시오.
 <단계1> 대상칼럼 : 가치관,전문지식,발표력,인성,창의력,자격증,종합점수 
 <단계2> 계층적 군집분석의 완전연결방식 적용 
 <단계3> 덴드로그램 시각화 : 군집 결과 확인  
 <단계4> 클러스터링 자르기 & 군집별 특성 분석 
'''

import pandas as pd
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster # 군집분석 도구
import matplotlib.pyplot as plt

# data loading - 신입사원 면접시험 데이터 셋 
path=r"C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML"
interview = pd.read_csv(path+"/data/interview.csv", encoding='ms949')
print(interview.info())
'''
RangeIndex: 15 entries, 0 to 14
Data columns (total 9 columns):
'''
# 레이블 인코딩
from sklearn.preprocessing import LabelEncoder
encoder=LabelEncoder()
interview['합격여부']=encoder.fit_transform(interview['합격여부'])

# <단계1> subset 생성 : no 칼럼을 제외한 나머지 칼럼 이용 
interview=interview.iloc[:,1:]

# <단계2> 계층적 군집 분석  완전연결방식 - 가장 먼 거리의 클러스터를 대상으로 거리 측정하는 방식  
clusters = linkage(interview, method='complete')

# <단계3> 덴드로그램 시각화 : 군집 결과 확인
dendrogram(clusters,leaf_font_size=12)

# <단계4> 클러스터링 자르기 & 군집별 특성 분석 

# 1) 클러스터링 자르기
cluster = fcluster(clusters, t=3, criterion='maxclust') 
interview['cluster']=cluster

# 2) 군집별 특성 분석
cluster_group=interview.groupby('cluster')
cluster_group.mean()
'''
           가치관   전문지식    발표력     인성    창의력  자격증   종합점수  합격여부
cluster                                                     
1        11.00  15.20  19.40  11.00   6.20  0.4  62.80     0
2        18.75  14.25  15.75  14.75  11.75  1.0  75.25     1
3        14.40  18.80  10.80   9.40  18.20  0.0  71.60     0
'''