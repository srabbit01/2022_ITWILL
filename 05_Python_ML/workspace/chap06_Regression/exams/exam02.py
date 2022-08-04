# -*- coding: utf-8 -*-
"""
문2) california 주택가격을 대상으로 다음과 같은 단계별로 선형회귀분석을 수행하시오.
"""

# california 주택가격 데이터셋 
'''
캘리포니아 주택 가격 데이터(회귀 분석용 예제 데이터)

•타겟 변수
1990년 캘리포니아의 각 행정 구역 내 주택 가격의 중앙값

•특징 변수(8) 
MedInc : 행정 구역 내 소득의 중앙값
HouseAge : 행정 구역 내 주택 연식의 중앙값
AveRooms : 평균 방 갯수
AveBedrms : 평균 침실 갯수
Population : 행정 구역 내 인구 수
AveOccup : 평균 자가 비율
Latitude : 해당 행정 구역의 위도
Longitude : 해당 행정 구역의 경도
'''

from sklearn.datasets import fetch_california_housing # dataset load
import pandas as pd # DataFrame 생성 
from sklearn.linear_model import LinearRegression  # model
from sklearn.model_selection import train_test_split # dataset split
from sklearn.metrics import mean_squared_error, r2_score # model 평가 
import matplotlib.pyplot as plt 

# 캘리포니아 주택 가격 dataset load 
california = fetch_california_housing()
print(california.DESCR)

X = california.data
type(X) # numpy.ndarray


# 단계1 : 특징변수(8개)와 타켓변수(MEDV)를 이용하여 DataFrame 생성하기  
#  numpy -> DataFrame 
cal_df = pd.DataFrame(california.data, 
                      columns=california.feature_names)
cal_df["MEDV"] = california.target # y변수 추가 
print(cal_df.tail())
print(cal_df.info()) 

type(cal_df) # pandas.core.frame.DataFrame


# 단계2 : 타켓변수와 가장 상관관계가 높은 특징변수 확인하기  
# 힌트 : DF.corr()
cal_df.corr()['MEDV']
'''
MedInc        0.688075
HouseAge      0.105623
AveRooms      0.151948
AveBedrms    -0.046701
Population   -0.024650
AveOccup     -0.023737
Latitude     -0.144160
Longitude    -0.045967
MEDV          1.000000
Name: MEDV, dtype: float64
'''

# 단계3 : california 데이터셋을 대상으로 1만개 샘플링하여 서브셋 생성하기  
# 힌트 : 20,640 -> DF.sample(10000) 
cal_sample=cal_df.sample(10000,random_state=200)
y=cal_sample.pop('MEDV')
X=cal_sample

# 단계4 : 75%(train) vs 25(test) 비율 데이터셋 split 
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.25, random_state=321)

# 단계5 : 회귀모델 생성
model=LinearRegression().fit(X_train,y_train)

# 단계6 : 모델 검정(evaluation)  : 과적합(overfitting) 확인  
ytest_pred=model.predict(X_val)
ytest_true=y_val
# 과적합 확인
model.score(X_train,y_train) # 0.6108252760796156
model.score(X_val,y_val) # 0.6217437442549416
# 과적합 없으며, 일반화 가능 -> 그러나, 예측력이 낮은 것으로 보임

# 단계7 : 모델 평가(test) : new dataset 적용 
import numpy as np
cal_sample=cal_df.sample(10000,random_state=200)
test_idx=[]
for i in cal_df.index:
    if i not in list(cal_sample.index):
        test_idx.append(i)
new_dataset=cal_df.iloc[test_idx,:]
new_y=new_dataset.pop('MEDV')
new_X=new_dataset

# 조건1) 단계3의 서브셋 대상으로 30% 샘플링 자료 이용
X_train, X_test, y_train, y_test = train_test_split(new_X, new_y, test_size=0.3, random_state=124)

# 조건2) 평가방법 : MSE, r2_score
ytest_pred=model.predict(X_test)
ytest_true=y_test
mean_squared_error(ytest_true,ytest_pred)
# MSE = 0.5091718021804146

# 단계8 : 예측치 100개 vs 정답 100개 비교 시각화 
import seaborn as sn
plt.figure(figsize=(10, 5))
sn.distplot(ytest_true[:100],hist=False,label='y_true')
sn.distplot(ytest_pred[:100],hist=False,label='y_predict')
plt.legend(loc='best')
