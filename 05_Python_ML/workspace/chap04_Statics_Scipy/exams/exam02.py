# -*- coding: utf-8 -*-
"""
문2) titanic 데이터셋을 이용하여 다음과 같이 카이제곱 검정하시오.
   <단계1> 생존여부(survived), 사회적지위(pclass) 변수를 이용하여 교차분할표 작성 
   <단계2> 카이제곱 검정통계량, 유의확률, 자유도, 기대값 출력      
   <단계3> 가설검정 결과 해설  
"""

import seaborn as sn
import pandas as pd
from scipy import stats # 확률분포 검정 

# titanic dataset load 
titanic = sn.load_dataset('titanic')
print(titanic.info())

# <단계1> 교차분할표 
tab=pd.crosstab(index=titanic.survived,columns=titanic.pclass)
'''
pclass      1   2    3
survived              
0          80  97  372
1         136  87  119
'''

# <단계2> 카이제곱 검정통계량, 유의확률, 자유도, 기대값  
chi2, pvalue, df, evalue = stats.chi2_contingency(observed= tab)

# <단계3> 가설검정 해설 
print('chi2 = %.6f, pvalue = %.6f, d.f = %d'%(chi2, pvalue, df))
# chi2 = 102.888989, pvalue = 0.000000, d.f = 2
