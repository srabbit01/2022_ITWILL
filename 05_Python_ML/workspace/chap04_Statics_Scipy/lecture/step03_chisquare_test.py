'''
 카이제곱 검정(chisquare test) 
  - 확률변수의 적합성 검정 - 일원  
  - 두 집단변수 간의 독립성 검정 - 이원 
  - 검정통계량(기대비율) = sum( (관측값 - 기댓값)**2 / 기댓값 )
'''

from scipy import stats # 확률분포 검정 


# 1. 일원 chi-square(1개 변수 이용) : 적합성 검정 
'''
 귀무가설 : 관측치와 기대치는 차이가 없다.
 대립가설 : 관측치와 기대치는 차이가 있다. 
'''

# 주사위 적합성 검정 
real_data = [4, 6, 17, 16, 8, 9] # 관측값 - 관측도수 
exp_data = [10,10,10,10,10,10] # 기대값 - 기대도수 
chis = stats.chisquare(real_data, exp_data) # stats.chisquare(관측값,기대값)
print(chis)
print('statistic = %.3f, pvalue = %.3f'%(chis))
# statistic = 14.200, pvalue = 0.014
# statistic: 검정통계량, pvalue: 유의확률
# format을 이용하여 두 개로 나누어짐

# p-value = 0.014 < alpha = 0.05: 기각(대립가설 채택) 

import numpy as np # 검정통계량 구하기
real_array=np.array(real_data)
exp_array=np.array(exp_data)

stat=sum((real_array-exp_array)**2/exp_array) # 14.200000000000001

# 2. 이원 chi-square(2개 변수 이용) : 교차행렬의 관측값과 기대값으로 검정
'''
 귀무가설 : 교육수준과 흡연율 간에 관련성이 없다.(기각)
 대립가설 : 교육수준과 흡연율 간에 관련성이 있다.(채택)
'''

# 파일 가져오기
import pandas as pd

path = r'C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML\data'
smoke = pd.read_csv(path + "/smoke.csv")
smoke.info()
'''
 0   education  355 non-null    int64 -> 숫자형
 1   smoking    355 non-null    int64 -> 숫자형
'''
education.unique() # array([1, 2, 3], dtype=int64)
smoking.unique() # array([1, 2, 3], dtype=int64)

# <단계 1> 변수 선택 
print(smoke)# education, smoking 변수
education = smoke.education # smoke['education']
smoking = smoke.smoking # smoke['smoking']

# <단계 2> 교차분할표 
tab = pd.crosstab(index=education, columns=smoking)
print(tab) # 관측값 
'''
smoking     1   2   3
education            
1          51  92  68 -> 빈도수
2          22  21   9
3          43  28  21
'''

# <단계3> 카이제곱 검정 : 교차분할표 이용 
# 이원카이제곱 검정은 반드시 교차분할표만 활용 가능
chi2, pvalue, df, evalue = stats.chi2_contingency(observed= tab)
'''
(18.910915739853955, -> 카이제곱 검정통계량
 0.0008182572832162924, -> 유의확률
 4, -> 자유도(정수)
 array([[68.94647887, 83.8056338 , 58.24788732],
        [16.9915493 , 20.65352113, 14.35492958],
        [30.06197183, 36.54084507, 25.3971831 ]]))
'''

# chi2 검정통계량, 유의확률, 자유도, 기대값  
print('chi2 = %.6f, pvalue = %.6f, d.f = %d'%(chi2, pvalue, df))
# chi2 = 18.910916, pvalue = 0.000818, d.f = 4

# <단계4> 기대값 
print(evalue)
# 값이 높을 수록 교육수준/흡연률 높음
'''
smoking     1   2   3
education            
1          51  92  68 
2          22  21   9
3          43  28  21 -> 관측값
chi2 = 18.910916, pvalue = 0.000818, d.f = 4
[[68.94647887 83.8056338  58.24788732]
 [16.9915493  20.65352113 14.35492958]
 [30.06197183 36.54084507 25.3971831 ]] -> 기대값
'''
# chi2가 크면 기대값과 관측값 사이 간격이 크며, pvalue=0에 가까워짐

#############################################
# 성별과 흡연 간의 독립성 검정 example 
#############################################
'''
 귀무가설 : 성별과 흡연유무 간에 관련성이 없다.(채택)
 대립가설 : 성별과 흡연유무 간에 관련성이 있다.(기각)
'''
import seaborn as sn
import pandas as pd

# <단계1> titanic dataset load 
tips = sn.load_dataset('tips')
print(tips.info())

# <단계2> 교차분할표 
table = pd.crosstab(index=tips.smoker, columns=tips.sex)
'''
sex     Male  Female
smoker              
Yes       60      33
No        97      54
'''

# <단계3> 카이제곱 검정 
chi2, pvalue, df, evalue = stats.chi2_contingency(observed= table)
print('chi2 = %.6f, pvalue = %.6f, d.f = %d'%(chi2, pvalue, df))
# chi2 = 0.008763, pvalue = 0.925417, d.f = 1
print(evalue)
'''
[[59.84016393 33.15983607]
 [97.15983607 53.84016393]]
'''