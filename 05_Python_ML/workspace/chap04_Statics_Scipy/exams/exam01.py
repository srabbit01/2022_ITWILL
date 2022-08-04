# -*- coding: utf-8 -*-
"""
문1) 이항검정 : 95% 신뢰수준에서 토요일(Sat)에 오는 여자 손님 중 비흡연자가 흡연자 보다 많다고 할 수 있는가?

 귀무가설 : 비흡연자와 흡연자의 비율은 차이가 없다.(P=0.5)
"""

from scipy import stats # 이항검정 
import pandas as pd # csv file read

path = r'C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML\data'
tips = pd.read_csv(path + "/tips.csv")
print(tips.info())
print(tips.head())

# 1. 행사 요일 빈도수 
day = tips['day']
print(day.value_counts())
'''
Sat     87  -> 토요일 빈도수 
Sun     76
Thur    62
Fri     19
'''

# 2. 성별 빈도수 
gender = tips['sex']
print(gender.value_counts())
'''
Male      157
Female     87 -> 여자 빈도수
'''

# 3. Sat 기준 subset 생성 
sat_day = tips[tips['day'] == 'Sat'] # DF[DF['칼럼명'] 관계식]
print(sat_day.head())
'''
    total_bill   tip     sex smoker  day    time  size
19       20.65  3.35    Male     No  Sat  Dinner     3
20       17.92  4.08    Male     No  Sat  Dinner     2
21       20.29  2.75  Female     No  Sat  Dinner     2
22       15.77  2.23  Female     No  Sat  Dinner     2
23       39.42  7.58    Male     No  Sat  Dinner     4
'''

# 4. sat_day를 대상으로 Female 기준 subset 생성 
sat_fem=sat_day[sat_day.sex=='Female']

# 5. subset을 대상으로 smoker 기준 group 
# - 성공회수(비흡연자)와 시행회수(비흡연자+흡연자)  확인 
len(sat_fem[sat_fem.smoker=='No']) # 13
len(sat_fem) # 28

# group 객체 이용
print(sat_fem.groupby('smoker'))

# 6. 이항검정(binom test) : 성공회수와 시행회수 이용 
p_value=stats.binom_test(x=13, n=28, p=0.5, alternative='two-sided') 
p_value # 0.8505540192127226

alpha=0.05 # 95% 신뢰수준: alpha=1-0.95
if pvalue>=alpha:
    print('토요일 여자 손님 중 흡연자와 비흡연자 차이가 없다.') # 채택
else:
    print('토요일 여자 손님 중 흡연자와 비흡연자 차이가 있다.')
# 토요일 여자 손님 중 흡연자와 비흡연자 차이가 있다.

