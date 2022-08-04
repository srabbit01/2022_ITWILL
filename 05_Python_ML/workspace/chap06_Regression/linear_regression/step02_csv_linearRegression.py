# -*- coding: utf-8 -*-
"""
step02_csv_linearRegression.py

csv file 자료 + 회귀모델  
"""

import pandas as pd # csv file read
from sklearn.linear_model import LinearRegression # model 
from sklearn.metrics import mean_squared_error, r2_score # 평가도구 
from sklearn.model_selection import train_test_split # split


# 1. dataset load
path = r'C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML\data' # file path 

iris = pd.read_csv(path + '/iris.csv')
print(iris.info())
type(iris)

# 2. 변수 선택 
# 변수 이름만 추출
cols = list(iris.columns)

list(iris.columns).pop(2)

y_col = cols.pop(2) # 3칼럼 추출 & 제외 
y_col # 'Petal.Length'
type(y_col)

x_cols = cols[:-1]
x_cols # ['Sepal.Length', 'Sepal.Width', 'Petal.Width']
type(x_cols)

X = iris[x_cols] 
y = iris[y_col] 
type(X)
type(y)
X.shape # (150, 3)
y.shape # (150,)

# 3. train/val(검증) split 
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.3, random_state=123)


X_train.shape # (105, 3)
X_val.shape # (45, 3)


# 4. model 생성 : train set 
lr = LinearRegression()
model = lr.fit(X_train, y_train)


# 5. model 평가(검증) : test set 
y_pred = model.predict(X = X_val) # 예측치

# 1) MSE
mse = mean_squared_error(y_true = y_val, y_pred = y_pred)
print(mse)  # 0.12397491396059161

# 2) 결정계수
score = r2_score(y_true = y_val, y_pred = y_pred)
print(score) # 0.9643540833169766

# 과적합 유무 확인
model.score(X_train,y_train) # 0.9694825528782403
model.score(X_val,y_val) # 0.9643540833169766
# 두 결정계수 차이가 없기 때문에 일반화 가능

'''
model 평가1: train vs test (val+test)
model 평가2: train vs val vs test # 검증과 실제 구현 따로
'''

# 6. 실제 자료를 이용한 model test: 업무용 dataset 사용
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=100)

y_pred = model.predict(X = X_test) # (X=new_Data)

mse=mean_squared_error(y_true = y_test, y_pred = y_pred)
print(mse)

score = r2_score(y_true = y_test, y_pred = y_pred)
print(score)