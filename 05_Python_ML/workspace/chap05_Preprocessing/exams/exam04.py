# -*- coding: utf-8 -*-
"""
문4) BostonHousing 데이터셋을 대상으로 다음과 같은 단계별로 전처리를 수행하시오. 
"""

import pandas as pd # csv file load 
from sklearn.preprocessing import StandardScaler # 스케일링 도구
import numpy as np # np.log1p() 함수 

# 단계1. dataset load

### BostonHousing.csv : 카페에서 다운로드
path=r'C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML'
boston = pd.read_csv(path+r'\data\BostonHousing.csv')
boston.info()
'''
RangeIndex: 506 entries, 0 to 505
Data columns (total 15 columns):
 #   Column     Non-Null Count  Dtype  
---  ------     --------------  -----  
 0   CRIM       506 non-null    float64  -> 1번 x변수  
 1   ZN         506 non-null    float64  -> 2번 x변수
 2   INDUS      506 non-null    float64
 3   CHAS       506 non-null    int64  
 4   NOX        506 non-null    float64
 5   RM         506 non-null    float64
 6   AGE        506 non-null    float64
 7   DIS        506 non-null    float64
 8   RAD        506 non-null    int64  
 9   TAX        506 non-null    int64  
 10  PTRATIO    506 non-null    float64
 11  B          506 non-null    float64
 12  LSTAT      506 non-null    float64 -> 13번 x변수 
 13  MEDV       506 non-null    float64 -> y변수
 14  CAT. MEDV  506 non-null    int64   -> 변수 제거   
'''
 
# 단계2 :  'CAT. MEDV' 변수 제거 후 new_df 만들기 
new_df=boston.drop('CAT. MEDV',axis=1)

# 단계3 : new_df에서 1~13칼럼으로 X변수 만들기   
X=new_df.iloc[:,:13]
X.info()

# 단계4 : new_df에서 'MEDV' 칼럼으로 y변수 만들기 
y=new_df.iloc[:,13]

# 단계5 : X변수와 y변수 요약통계량 확인하기   
X.describe()
'''
             CRIM          ZN       INDUS  ...     PTRATIO           B       LSTAT
count  506.000000  506.000000  506.000000  ...  506.000000  506.000000  506.000000
mean     3.613524   11.363636   11.136779  ...   18.455534  356.674032   12.653063
std      8.601545   23.322453    6.860353  ...    2.164946   91.294864    7.141062
min      0.006320    0.000000    0.460000  ...   12.600000    0.320000    1.730000
25%      0.082045    0.000000    5.190000  ...   17.400000  375.377500    6.950000
50%      0.256510    0.000000    9.690000  ...   19.050000  391.440000   11.360000
75%      3.677083   12.500000   18.100000  ...   20.200000  396.225000   16.955000
max     88.976200  100.000000   27.740000  ...   22.000000  396.900000   37.970000
'''
y.describe()
y.shape # (506,) = 1차원 의미
'''
count    506.000000
mean      22.532806
std        9.197104
min        5.000000
25%       17.025000
50%       21.200000
75%       25.000000
max       50.000000
'''

# 단계6. X변수 표준화 : X변수 표준화 후 칼럼명을 지정하여 new_df2 만들기 
col_names=list(new_df.columns)
scaler=StandardScaler()
new_X=scaler.fit_transform(X)
new_df2=pd.DataFrame(new_X,columns=col_names[0:13])
new_df2.info()

# 단계7. y변수 로그화  : y변수 로그변환 후 new_df2에 'MEDV'이름으로 칼럼 추가하기   
new_y=np.log1p(np.abs(y))
new_df2['MEDV']=new_y
new_df2.info()

# 단계8 : 최종결과 완성된 new_df2을 대상으로 요약통량으로 확인하기 
new_df2.describe()
'''
               CRIM            ZN  ...         LSTAT        MEDV
count  5.060000e+02  5.060000e+02  ...  5.060000e+02  506.000000
mean  -8.513173e-17  3.306534e-16  ... -1.595123e-16    3.085437
std    1.000990e+00  1.000990e+00  ...  1.000990e+00    0.386966
min   -4.197819e-01 -4.877224e-01  ... -1.531127e+00    1.791759
25%   -4.109696e-01 -4.877224e-01  ... -7.994200e-01    2.891757
50%   -3.906665e-01 -4.877224e-01  ... -1.812536e-01    3.100092
75%    7.396560e-03  4.877224e-02  ...  6.030188e-01    3.258097
max    9.933931e+00  3.804234e+00  ...  3.548771e+00    3.931826
'''