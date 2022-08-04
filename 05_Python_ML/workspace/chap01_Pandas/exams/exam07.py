# -*- coding: utf-8 -*-
"""
문7) titanic 데이터셋을 대상으로 아래와 같이 단계별로 처리하시오. 
"""

import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')
titanic.info()

# 단계1 : age, sex, class, fare, survived 칼럼만 선택하여 서브셋 생성 
titanic_new=titanic.iloc[:,[3,2,8,6,0]]
titanic_new.info()

# 단계2 : class와 sex 칼럼 기준으로 그룹을 생성하고 그룹의 크기 확인 
titanic_gp=titanic_new.groupby(['class','sex'])
titanic_gp.size()
'''
class   sex   
First   female     94
        male      122
Second  female     76
        male      108
Third   female    144
        male      347
dtype: int64
'''

# 단계3 : 그룹별 평균 구하기 
titanic_gp.mean()
'''
                     age        fare  survived
class  sex                                    
First  female  34.611765  106.125798  0.968085
       male    41.281386   67.226127  0.368852
Second female  28.722973   21.970121  0.921053
       male    30.740707   19.741782  0.157407
Third  female  21.750000   16.118810  0.500000
       male    26.507589   12.661633  0.135447
'''

# 단계4 : [단계3]에서 만든 그룹별 평균을 대상으로 survived 칼럼 기준 막대차트 시각화  
titanic_sur=titanic_gp['survived'].mean()
titanic_sur.plot(kind='bar')
