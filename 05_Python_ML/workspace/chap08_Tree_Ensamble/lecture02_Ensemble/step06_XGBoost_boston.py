# -*- coding: utf-8 -*-
"""
step06_XGBoost_boston.py

 - XGBoost 회귀트리 예
"""

from xgboost import XGBRegressor # 회귀트리 (연속형 변수)
from xgboost import plot_importance # 중요변수 시각화 

from sklearn.datasets import load_boston # dataset
from sklearn.model_selection import train_test_split # dataset split 
from sklearn.metrics import mean_squared_error, r2_score # 평가 

# 1. dataset load
boston = load_boston()

x_names = boston.feature_names
x_names
# array(['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS',
#       'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT'], dtype='<U7')

X = boston.data
y = boston.target # 연속형 변수
X.shape # (506, 13)
# numpy array 행렬

#  2. train/test split: 70% vs 30%
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3)

# 3. model 생성 
model = XGBRegressor().fit(X = X_train, y = y_train)
print(model)
'''
XGBRegressor(base_score=0.5, booster='gbtree', callbacks=None,
             colsample_bylevel=1, colsample_bynode=1, colsample_bytree=1,
             early_stopping_rounds=None, enable_categorical=False,
             eval_metric=None, gamma=0, gpu_id=-1, grow_policy='depthwise',
             importance_type=None, interaction_constraints='',
             learning_rate=0.300000012, max_bin=256, max_cat_to_onehot=4,
             max_delta_step=0, max_depth=6, max_leaves=0, min_child_weight=1,
             missing=nan, monotone_constraints='()', n_estimators=100, n_jobs=0,
             num_parallel_tree=1, predictor='auto', random_state=0, reg_alpha=0,
             reg_lambda=1, ...)
# 별도의 활성함수(activation function)를 통해 가중치를 주어
# 계산된 값을 y로 넘김
# 그러나, 회귀트리에서는 활성함수를 거치지 않고 바로 넘김 = 항등함수 (기본 계산값)
'''


# 4. 중요변수 확인 
fscore = model.get_booster().get_fscore()
print(fscore)
'''
{'f0': 696.0, 'f1': 67.0, 'f2': 91.0, 'f3': 17.0, 'f4': 165.0,
 'f5': 431.0, 'f6': 340.0, 'f7': 269.0, 'f8': 49.0, 'f9': 66.0,
 'f10': 91.0, 'f11': 281.0, 'f12': 310.0}
'''


# 중요변수 시각화 
plot_importance(model, max_num_features=13) # f0 ~ f12 
# 변수 이름 대수 'f위치'로 결과 출력
# -> Pandas.DataFrame으로 변형하면 칼럼 이름 출력 가능

# 5. model 평가
y_pred = model.predict(X_test)

# 1) mean_squared_error
mse=mean_squared_error(y_true=y_test,y_pred=y_pred)
print(mse) # 9.332109294153978

# 2) r2_score
r2=r2_score(y_true=y_test,y_pred=y_pred)
print(r2) # 0.8598391325477043 -> 분류 정확도 비교적 높음

####################################################
## 중요변수 시각화에 X 변수명 표시 = pandas 객체 활용
####################################################
import pandas as pd

X=boston.data
y=boston.target

# df 생성 
df=pd.DataFrame(X,columns=x_names)
df['target']=y
df.info()

# train/test split: 70% vs 30%
X_train, X_test, y_train, y_test = train_test_split(
    df.iloc[:,:13],df.iloc[:,:13], test_size=0.3)

# model 생성 
model = XGBRegressor().fit(X = X_train, y = y_train)
print(model)

# 중요변수 확인 
fscore = model.get_booster().get_fscore()
print(fscore)
'''
{'CRIM': 3810.0, 'ZN': 690.0, 'INDUS': 1072.0, 'CHAS': 141.0,
 'NOX': 1239.0, 'RM': 2305.0, 'AGE': 1939.0, 'DIS': 1660.0,
 'RAD': 485.0, 'TAX': 583.0, 'PTRATIO': 575.0, 'B': 1577.0,
 'LSTAT': 1675.0}
'''

# 중요변수 시각화 
plot_importance(model, max_num_features=13)