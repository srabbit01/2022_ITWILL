#########################################
### 4. 피처 스케일링(feature scaling) 
#########################################

"""
피처 스케일링 : 서로 다른 크기(단위)를 갖는 X변수(feature)를 대상으로 일정한 범위로 조정하는 전처리 작업 
 - 방법 : 표준화, 최소-최대 정규화, 로그변환    
 
 1. 표준화 : X변수를 대상으로 정규분포가 될 수 있도록 평균=0, 표준편차=1로 통일 시킴 
   -> 회귀모델, SVM 계열은 X변수가 정규분포라고 가정하에 학습이 진행되므로 표준화를 적용   
 2. 최소-최대 정규화 : 서로 다른 척도(값의 범위)를 갖는 X변수를 대상으로 최솟값=0, 최댓값=1로 통일 시킴 
   -> 트리모델 계열(회귀모델 계열이 아닌 경우)에서 서로 다른 척도를 갖는 경우 적용 
 3. 로그변환 : log()함수 이용하여 로그변환   
   -> 비선형(곡선) -> 선형(직선)으로 변환
   -> 왜곡을 갖는 분포 -> 좌우대칭의 정규분포로 변환   
   -> 회귀모델에서 Y변수 적용(X변수를 표준화 또는 정규화할 경우 Y변수는 로그변환) 
"""

# 1. 함수 스케일링 도구  
from sklearn.preprocessing import scale # 표준화(mu=0, st=1) 
from sklearn.preprocessing import minmax_scale # 정규화(0~1)
import numpy as np # 로그변환 + 난수

# data 생성 : 난수 정수 생성  
np.random.seed(12) # 시드값 
X = np.random.randint(-10, 100, (5, 4)) # -10~100
X
'''
array([[ 65,  17,  -4,  -8],
       [ -7,  57,  66,  38],
       [ 12,  39,  42,  -5],
       [  3,  79,  24,  65],
       [ 64, -10,  94,  66]])
'''
X.min() # -10 
X.max() # 94

# 1) 표준화 (mu=0,st=1)
# 독립변수(X)의 평균 0 표준편차 1로 변환
# 표준화(Z) = (X-mu)/sigma
X_zscore=scale(X)
print(X_zscore)
'''
[[ 1.21744704 -0.62775611 -1.43459212 -1.21010711]
 [-1.11383453  0.66658639  0.64023119  0.20991654]
 [-0.49863523  0.08413226 -0.0711368  -1.11749688]
 [-0.79004542  1.37847476 -0.60466279  1.04340869]
 [ 1.18506813 -1.5014373   1.47016052  1.07427876]]
'''
# 첫번째 열
X_zscore[:,0].mean() # 평균: 8.881784197001253e-17 = 0에 근사
X_zscore[:,0].std() # 표준편차: 1.0
# 마지막 열
X_zscore[:,-1].mean() # 평균: -4.4408920985006264e-17 = 0에 근사
X_zscore[:,-1].std() # 표준편차: 1.0

# 2) 정규화
# (X-min(X))/(max(X)-min(X))
X_norm=minmax_scale(X)
print(X_norm)
'''
[[1.         0.30337079 0.         0.        ]
 [0.         0.75280899 0.71428571 0.62162162]
 [0.26388889 0.5505618  0.46938776 0.04054054]
 [0.13888889 1.         0.28571429 0.98648649]
 [0.98611111 0.         1.         1.        ]]
'''
# 첫번째 열
X_norm[:,0].min() # 0.0
X_norm[:,0].max() # 0.9999999999999999
# 마지막 열
X_norm[:,-1].min() # 0.0
X_norm[:,-1].max() # 1.0

# 3) 로그화
np.log(X) # 밑이 e인 로그
'''
RuntimeWarning: invalid value encountered in log: -> X가 음수인 경우 warning
 - 0 -> Inf(무한대)
 - 음수 -> NaN
 - 확률 -> 음수
이런 일부 값이 들어가면 문제가 발생할 수 있기 때문에 주의하라는 의미
제대로된 연산이 X
'''
X_log=np.log1p(np.abs(X)) # log(|n|+1)
# Inf(무한대 나오지 않음)
# np.log1p(): 음수의 경우 절댓값 -> 양수화
print(X_log)
'''
[[4.18965474 2.89037176 1.60943791 2.19722458]
 [2.07944154 4.06044301 4.20469262 3.66356165]
 [2.56494936 3.68887945 3.76120012 1.79175947]
 [1.38629436 4.38202663 3.21887582 4.18965474]
 [4.17438727 2.39789527 4.55387689 4.20469262]]
'''
# 모두 작은 규모(범위)로 변환

# 2. 클래스 스케일링 도구 
from sklearn.preprocessing import StandardScaler, MinMaxScaler 
import pandas as pd
path=r'C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML'
iris = pd.read_csv(path+r"\data\iris.csv")
iris.info()

# 1) DataFrame 표준화

# (1) 객체 생성
type(iris) # pandas.core.frame.DataFrame
scaler=StandardScaler() # 객체 생성
dir(scaler) 

# (2) 표준화 스케일링
# 보통 2차원 이상은 대문자 X, 1차원은 소문자 y
X_scaled=scaler.fit_transform(X=iris.drop('Species',axis=1)) # Species 칼럼 제외, 행 단위
X_scaled.shape # (150,4)
type(X_scaled) # numpy.ndarray

# (3) numpy -> pandas: 칼럼 단위 처리하고 싶을 때 변환
col_names=list(iris.columns)
new_df=pd.DataFrame(X_scaled,columns=col_names[:4])
new_df.info() # scaling 후 값 저장
# 요약통계량 확인
new_df.describe() # mean(평균)=0, std(표준편차)=1 확인
'''
       Sepal.Length   Sepal.Width  Petal.Length   Petal.Width
count  1.500000e+02  1.500000e+02  1.500000e+02  1.500000e+02
mean  -2.775558e-16 -9.695948e-16 -8.652338e-16 -4.662937e-16
std    1.003350e+00  1.003350e+00  1.003350e+00  1.003350e+00
min   -1.870024e+00 -2.433947e+00 -1.567576e+00 -1.447076e+00
25%   -9.006812e-01 -5.923730e-01 -1.226552e+00 -1.183812e+00
50%   -5.250608e-02 -1.319795e-01  3.364776e-01  1.325097e-01
75%    6.745011e-01  5.586108e-01  7.627583e-01  7.906707e-01
max    2.492019e+00  3.090775e+00  1.785832e+00  1.712096e+00
'''

# (4) DataFrame 내 종속변수(Y) 추가
new_df['Species']=iris.Species
new_df.info()
print(new_df) # 앞 4개 칼럼(X): 스케일링, 뒤 1개 칼럼(Y) 추가

# 2) DataFrame 정규화

# (1) 객체 생성
scaler=MinMaxScaler() # 객체 생성
dir(scaler)

# (2) 정규화 스케일링
# 보통 2차원 이상은 대문자 X, 1차원은 소문자 y
X_scaled=scaler.fit_transform(X=iris.drop('Species',axis=1)) # Species 칼럼 제외, 행 단위
X_scaled.shape # (150,4)
type(X_scaled) # numpy.ndarray

# (3) numpy -> pandas: 칼럼 단위 처리하고 싶을 때 변환
col_names=list(iris.columns)
new_df=pd.DataFrame(X_scaled,columns=col_names[:4])
new_df.info() # scaling 후 값 저장
# 요약 통계량 확인
new_df.describe() # min(최소)=0, max(최대)=1 확인
'''
       Sepal.Length  Sepal.Width  Petal.Length  Petal.Width
count    150.000000   150.000000    150.000000   150.000000
mean       0.428704     0.440556      0.467458     0.458056
std        0.230018     0.181611      0.299203     0.317599
min        0.000000     0.000000      0.000000     0.000000
25%        0.222222     0.333333      0.101695     0.083333
50%        0.416667     0.416667      0.567797     0.500000
75%        0.583333     0.541667      0.694915     0.708333
max        1.000000     1.000000      1.000000     1.000000
'''

# (4) DataFrame 내 종속변수(Y) 추가
new_df['Species']=iris.Species
new_df.info()
print(new_df) # 앞 4개 칼럼(X): 스케일링, 뒤 1개 칼럼(Y) 추가
