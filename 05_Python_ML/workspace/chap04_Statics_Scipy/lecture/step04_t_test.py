'''
t검정 : t 분포에 대한 가설검정  
  1. 한 집단 평균 검정: 모평균 검정
  2. 두 집단 평균 검정
  3. 대응 두 집단 검정: 한 집단 내 대응되는 소집단
'''

from scipy import stats # test
import numpy as np # sampling
import pandas as pd # csv file read

# 1. 한 집단 평균 검정 : 남자 평균 키(모평균)  
sample_data = np.random.uniform(172,179, size=29) # 172~179
print(sample_data)

# 기술통계 
print('평균 키 =', sample_data.mean()) 
# 평균 키 = 176.19279702246678

# 단일집단 평균차이 검정 
one_group_test = stats.ttest_1samp(sample_data, 176) 
print('t검정 통계량 = %.3f, pvalue = %.5f'%(one_group_test))
# t검정 통계량 = 0.530, pvalue = 0.60001
# 대부분 t검정 통계량이 +-1.96 내에 존재하면 귀무가설 채택
# 평균과 차이가 없음

# 2. 두 집단 평균 검정 : 남여 평균 점수 차이 검정 
female_score = np.random.uniform(50, 100, size=30) # 여성 
male_score = np.random.uniform(45, 95, size=30) # 남성 

# 기본 가설: 두 집단 평균 차이가 없다.

two_sample = stats.ttest_ind(female_score, male_score)
print(two_sample)
print('두 집단 평균 차이 검정 = %.3f, pvalue = %.3f'%(two_sample))
# 두 집단 평균 차이 검정 = 0.342, pvalue = 0.733
# 채택역 내 존재

# file 자료 이용 : 교육방법에 따른 실기점수의 평균차이 검정  
sample = pd.read_csv(r'C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML\data\two_sample.csv')
print(sample.info())
'''
 2   method  240 non-null    int64  
 3   score   180 non-null    float64
 '''

two_df = sample[['method', 'score']]
print(two_df)

# 교육방법 기준 subset
method1 = two_df[two_df.method==1]
method2 = two_df[two_df.method==2]

# score 칼럼 추출 
score1 = method1.score
score2 = method2.score

# NaN -> 길이는 항상 같아야 하기 때문에 '평균'으로 대체
type(score1)
score1=score1.fillna(score1.mean())
score2=score2.fillna(score2.mean())

# 두 집단 평균차이 검정 
two_sample = stats.ttest_ind(score1, score2)
print(two_sample)


# 3. 대응 두 집단 : 복용전 65 -> 복용후 60 몸무게 변환  
before = np.random.randint(60, 65, size=30)  
after = np.random.randint(59, 64,  size=30) 

paired_sample = stats.ttest_rel(before, after)
print(paired_sample)
print('t검정 통계량 = %.5f, pvalue = %.5f'%paired_sample)
# 만일, 통계량 내 NaN 결측치 존재할 경우, 결측치 제거 등 전처리 후 수행
# t검정 통계량 = 3.05626, pvalue = 0.00478
# 많은 효능은 없으나, 복용전과 복용후 차이가 있음
