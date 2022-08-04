# -*- coding: utf-8 -*-
"""
비선형회귀모형 만들기  
 - X와 y변수가 비선형관계를 가지는 경우 고차항 적용 
 - 1차항 : 선형관계
 - 2차항 : U자 관계
 - 3차항 : S자 관계
 - 이 이상은 과적합 문제로 사용하지 않음 
"""

import pandas as pd # csv file load 
import numpy as np # np.nan
from sklearn.model_selection import train_test_split # 데이터 split
import matplotlib.pyplot as plt # 회귀선 시각화 
import seaborn as sns # 비선형모형 예측치 시각화 


### 단계1 : 데이터 준비
## auto-mpg.csv : 카페에서 다운로드 
path = r'C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML\data' # file path 
df = pd.read_csv(path+r'\data\auto-mpg.csv',header=None)
df.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 398 entries, 0 to 397
Data columns (total 9 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   0       398 non-null    float64
 1   1       398 non-null    int64  
 2   2       398 non-null    float64
 3   3       398 non-null    object 
 4   4       398 non-null    float64
 5   5       398 non-null    float64
 6   6       398 non-null    int64  
 7   7       398 non-null    int64  
 8   8       398 non-null    object 
dtypes: float64(4), int64(3), object(2)
'''

# 1) 열 이름 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight','acceleration','model_year','origin','name']
df.info()


# 2) horsepower 칼럼 결측치 제거 -> 마력
# '?'로 표기된 결측치 -> np.nan 결측치로 변환
df['horsepower'].replace('?', np.nan, inplace=True) # '?'을 np.nan으로 변경

# 결측치 제거 
df.dropna(subset=['horsepower'], axis=0, inplace=True) # 누락데이터 행을 삭제
df.info()

# object -> float
df['horsepower'] = df['horsepower'].astype('float') # 문자열을 실수형으로 변환
df.info() # X변수 전처리 완료 


# 3) 분석에 필요한 변수 선택 : 연비, 실린더, 출력, 중량
new_df = df[['mpg', 'cylinders', 'horsepower', 'weight']]

X=new_df[['weight']] #독립 변수 X
y=new_df['mpg'] #종속 변수 Y

# 4) X, y변수 분포 
plt.plot(X, y, 'o', label='Train Data') # 데이터 분포
plt.legend(loc='best')
plt.xlabel('weight')
plt.ylabel('mpg')
plt.show()

# 4) train data 와 test data로 구분(7:3 비율)
X_train, X_test, y_train, y_test = train_test_split(
                        X, y, test_size=0.3, random_state=10)
print('훈련 데이터: ', X_train.shape)
print('검증 데이터: ', X_test.shape)
'''
훈련 데이터:  (274, 1)
검증 데이터:  (118, 1)
'''


### 단계2 : 선형회귀분석 모형 (1차 방정식)
from sklearn.linear_model import LinearRegression #선형회귀분석

# 단순선형회귀모형 & 평가 
model = LinearRegression().fit(X_train, y_train)

score = model.score(X_test, y_test)
print('단순선형회귀모델 score :', score) # 0.6822458558299325


# 1) 산점도와 선형회귀모델 회귀선 시각화 -> 산점도 확인
linear_model_pred = model.predict(X_test) # 선형회귀모델 예측치 
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot()
ax.plot(X_test, y_test, 'b.', label='real value') # 데이터 분포
ax.plot(X_test, linear_model_pred, 'r', label='linear model Predicted Value') # 모형 학습한 회귀선
ax.legend(loc='best')
plt.xlabel('weight')
plt.ylabel('mpg')
plt.show()

# 2) 실제값과 예측값 비교 : 분포곡선 
plt.figure(figsize=(10, 5))
sns.distplot(y_test, hist=False, label="y true")
sns.distplot(linear_model_pred, hist=False, label="y_pred")
plt.legend(loc='best')
plt.show()

#
import matplotlib.pyplot as plt
plt.plot(linear_model_pred,color='r',linestyle='--',label='y_predict')
plt.plot(y_test,color='b',linestyle='-.',label='y_true')
plt.legend(loc='best')
plt.show()


### 단계3 : 비선형회귀분석 모형 (다차 방정식)
from sklearn.preprocessing import PolynomialFeatures # x변수 다항식 변환

# X변수 다항식 변환
poly = PolynomialFeatures(degree=2) # 2차항 적용
type(poly) # sklearn.preprocessing._data.PolynomialFeatures

# X_train 데이터 2차항 변형
X_train_poly = poly.fit_transform(X_train) 
print('원 데이터: ', X_train.shape) # (274, 1)
print('2차항 변환 데이터: ', X_train_poly.shape)# (274, 3)
# 엑소: 모형식에서 사용되는 독립변수(X)
# 1차 -> 2차로 변환됨을 볼 수 있음
# [1.0000000e+00, 2.3790000e+03, 5.6596410e+06] = [절편,X기울기,X^2기울기,...]
'''
다항식(2차항) 엑소(exog): 모형식에서 사용되는 독립변수
2차 회귀반정식: y = a1*x + a2*x^2 + b
'''

#X_test 데이터 2차항 변형
X_test_poly = poly.fit_transform(X_test) 
print('원 데이터: ', X_test.shape) # (118, 1)
print('2차항 변환 데이터: ', X_test_poly.shape)# (118, 3)


# 비선형회귀모형 & 평가(결정계수) 
poly_model = LinearRegression().fit(X_train_poly, y_train) 

X_train_poly 
poly_model.coef_ # 회귀계수 
# array([ 0.00000000e+00, -1.85768289e-02,  1.70491223e-06]) = [의미X,X기울기,X^2기울기]
poly_model.intercept_

poly_score = poly_model.score(X_test_poly, y_test)
print('단순비선형회귀모델 score :', poly_score) 
# 단순비선형회귀모델 score : 0.7087009262975685
# 비선형 모델의 정확도가 더 높음

# 산점도와 비선형회귀모형 회귀선 시각화 : 2차항 적용  
linear_model_pred = model.predict(X_test) # 선형회귀모델 예측치 
poly_model_pred = poly_model.predict(X_test_poly) # 비선형회귀모델 예측치 
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot()
ax.plot(X_test, y_test, 'b.', label='real value') # 산점도 
ax.plot(X_test, linear_model_pred, 'g', label='linear model Predicted Value') # 선형모형 회귀선
ax.plot(X_test, poly_model_pred, 'ro', label='poly model Predicted Value') # 비선형 모형 회귀선
ax.legend(loc='best')
plt.xlabel('weight')
plt.ylabel('mpg')
plt.show()


# 실제값과 예측값 비교 : 분포곡선 
plt.figure(figsize=(10, 5))
sns.distplot(y_test, hist=False, label="y true")
sns.distplot(poly_model_pred, hist=False, label="y_pred")
plt.legend(loc='best')
plt.show()

