# -*- coding: utf-8 -*-
"""
statistics 모듈의 주요 함수 
  - 기술통계 : 대푯값, 산포도, 왜도/첨도 등   
"""

import statistics as st # 기술통계 
import pandas as pd # csv file 


# 기술통계 
path = r'C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML\data'
dataset = pd.read_csv(path + '/descriptive.csv')
print(dataset.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 300 entries, 0 to 299
Data columns (total 8 columns):
 #   Column    Non-Null Count  Dtype  
---  ------    --------------  -----  
 0   resident  300 non-null    object 
 1   gender    300 non-null    int64   -> 범주형
 2   age       300 non-null    int64   
 3   level     300 non-null    object 
 4   cost      300 non-null    float64 -> 연속형
 5   type      300 non-null    object 
 6   survey    187 non-null    float64
 7   pass      296 non-null    object 
dtypes: float64(2), int64(2), object(4)
memory usage: 18.9+ KB
'''

x = dataset['cost'] # 구매비용 선택 

# 1. 대푯값
print('평균 =', st.mean(x)) # 5.351
print('중위수=', st.median(x)) # 5.4
print('낮은 중위수 = ', st.median_low(x)) # 5.4
print('높은 중위수 = ', st.median_high(x)) # 5.4
print('최빈수 =',  st.mode(x)) # 6.0

type(x) # pandas.core.series.Series
x.value_counts()

# 2. 산포도   
var = st.variance(x)
print('표본의 분산 = ', var) 
print('모집단의 분산 =', st.pvariance(x)) 

std = st.stdev(x)
print('표본의 표준편차 =', std) 
print('모집단의 표준편차 =', st.pstdev(x))

'''
표준편차=분산의 제곱근(sqrt)
분산=표준편차의 제곱(**2)
'''

# 사분위수 
print('사분위수 :', st.quantiles(x)) 
# 사분위수 : [4.425000000000001, 5.4, 6.2]
# 제 1, 2, 3 사분위수 출력
# 이때, 중위수 = 제2사분위수

import scipy.stats as sts

# 3. 왜도/첨도 

# 1) 왜도 
sts.skew(x)  # -0.1531779106237012
'''
왜도 = 0 : 좌우대칭 
왜도 > 0 : 왼쪽 치우침
왜도 < 0 :  오른쪽 치우침
# 기울어진 척도
'''

# 첨도 
sts.kurtosis(x) # fisher 기준 # -0.1830774864331568
sts.kurtosis(x, fisher=False) # Pearson 기준 # 2.816922513566843
'''
첨도 0 : 정규분포 첨도 
첨도 > 0 : 뾰족함
첨도 < 0 : 완만함  
'''

# 히스토그램
import matplotlib.pyplot as plt
import seaborn as sn

sn.distplot(x,hist=True,kde=True)
plt.show()