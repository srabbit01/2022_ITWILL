'''
문1) load_boston() 함수를 이용하여 보스턴 시 주택 가격 예측 회귀모델 생성 
  조건1> train/test - 7:3비울
  조건2> y 변수 : boston.target
  조건3> x 변수 : boston.data
  조건4> 모델 평가 : MSE, r2_score
'''

from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

import numpy as np
import pandas as pd

# 1. data load
boston = load_boston()
print(boston)

# 2. 변수 선택  
X=boston.data
y=boston.target

# 3. train/test split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=123)
X_train.shape # (105, 3)
y_train.shape # (105,)

# 4. 회귀모델 생성 : train set
model=LinearRegression().fit(X=X_train,y=y_train)
print('회귀계수')
print('기울기 :', model.coef_)
print('y절편 :', model.intercept_)
'''
회귀계수
기울기 : [ 0.75572271 -0.6715641   1.43222782]
y절편 : -0.3150495624708074
'''

# 5. 모델 평가 : test set
ytest_pred=model.predict(X=X_test)
ytest_true=y_test

# 1) MSE
mean_squared_error(ytest_true,ytest_pred)
# 28.40585481050824

# 2) 결정계수
r2_score(ytest_true,ytest_pred) # 0.6485645742370703

# 과적합 유무 확인 
train_score=model.score(X=X_train, y=y_train)
test_score=model.score(X=X_test, y=y_test) 
print('train_score =',train_score,',','test_score =',test_score)
# train_score = 0.7647156501433012 , test_score = 0.6485645742370703
# [해설] 두 결정계수 차가 적기 때문에 일반화 가능하며, 비교적 낮은 예측력

# 3) 결과 시각화 및 비교
import matplotlib.pyplot as plt

plt.plot(ytest_pred,linestyle=':',color='y',label='y predict')
plt.plot(ytest_true,linestyle='--',color='g',label='y true')
plt.legend(loc='best')
plt.show()
