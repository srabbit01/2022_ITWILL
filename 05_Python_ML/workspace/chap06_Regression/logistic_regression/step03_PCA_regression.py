# -*- coding: utf-8 -*-
"""
step03_PCA_regression.py

주성분 분석(PCA : Principal Component Analysis)
 1. 다중회귀분석 
 2. 다중공선성의 진단
 3. 차원 축소 : 특징 수를 줄여서 다중공선성 문제 해결 
"""

from sklearn.decomposition import PCA # 주성분 분석
# decomposition: 분해 의미
from sklearn.datasets import load_iris # dataset
import matplotlib.pyplot as plt # 스크리 플롯 시각화
from statsmodels.formula.api import ols # formula 형식(추론 통계 방식) -> 다중회귀모델
import pandas as pd # numpy -> DataFrame 객체 변환

  
# 1.iris dataset load      
iris = load_iris()

X = iris.data
y = iris.target
type(X) # numpy.ndarray

# numpy -> pandas
df = pd.DataFrame(X, columns= ['x1', 'x2', 'x3', 'x4'])

# 상관계수 확인
corr = df.corr() # 상관계수 행렬 반환
print(corr)
'''
          x1        x2        x3        x4
x1  1.000000 -0.117570  0.871754  0.817941
x2 -0.117570  1.000000 -0.428440 -0.366126
x3  0.871754 -0.428440  1.000000  0.962865
x4  0.817941 -0.366126  0.962865  1.000000
# 모두 독립변수
'''

df['y'] = y 
df.columns  # ['x1', 'x2', 'x3', 'x4', 'y']


# 2. 다중선형회귀분석 
# 1)
from sklearn.linear_model import LinearRegression
model=LinearRegression().fit(X=df[['x1', 'x2', 'x3', 'x4']],y=df.y)

# 2)
ols_obj = ols(formula='y ~ x1 + x2 + x3 + x4', data = df).fit()
# 회귀분석 결과 제공  
print(ols_obj.summary()) # 결과(summary()) 제공하기 때문에 사용
'''
Model:                            OLS   Adj. R-squared:                  0.928
Method:                 Least Squares   F-statistic:                     484.5
Date:                Thu, 05 May 2022   Prob (F-statistic):           8.46e-83
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept      0.1865      0.205      0.910      0.364      -0.218       0.591
x1            -0.1119      0.058     -1.941      0.054      -0.226       0.002
x2            -0.0401      0.060     -0.671      0.503      -0.158       0.078
x3             0.2286      0.057      4.022      0.000       0.116       0.341
x4             0.6093      0.094      6.450      0.000       0.423       0.796
==============================================================================
# t: t검정통계량
# P>|t|: 유의확률 (0.05미만이면 영향력이 있음을 알 수 있음=귀무가설 기각, 이상은 영향력 없음)
'''


#  3. 다중공선성의 진단
'''
분산팽창계수(VIF, Variance Inflation Factor)으로 판단 
통상적으로 10보다 크면 다중공선성이 있다고 판단
''' 
from statsmodels.stats.outliers_influence import variance_inflation_factor

# 형식) variance_inflation_factor(exog, exog_idx)
dir(ols_obj)
'''
- endog(엔도): 모형에서 쓰이는 종속변수(y)
- endog_names: 모형에서 쓰이는 종속변수 이름
- exog(엑소): 모형에서 쓰이는 독립변수(X)와 y절편
- exog_names: 모형에서 쓰이는 독립변수(X) 이름과 y절편(Intercept)
'''

exog = ols_obj.exog # 엑소(exog): 독립변수(X)
type(exog) # numpy.ndarray

for i in range(1,5) : # 1 ~ 4 번째 독립변수(X)만 출력 (0번째는 절편)
    print(variance_inflation_factor(exog, i)) # idx=1~4
'''
7.072722013939539 - x1
2.100871676124253 - x2
31.26149777492164 - x3
16.090175419908462 - x4
'''
# variance_inflation_factor(독립변수,위치) = 분산팽창계수 출력

ols_obj.exog_names #  ['Intercept'=1, 'x1', 'x2', 'x3', 'x4']
# Intercept: 절편은 모두 1


# 4. 주성분분석(PCA): 상관성이 높은 변수끼리 묶기 -> 차원 축소
# 주성분분석: PCA(Principle Composition Analysis)
# - 상관성을 바탕으로 차원 축소 -> 회귀분석 혹은 분류분석의 독립변수로 사용

# 1) 주성분분석 모델 생성 
pca = PCA() # 객체 생성: random_state=123
X_pca = pca.fit_transform(X) # 주성분분석 실행: 4개의 데이터를 주성분분석의 모델에 맞게 변환
print(X_pca) # 주성분의 개수는 독립변수의 개수와 동일하게 생성
X_pca.shape # (150, 4) = (행, 열)
# 각 열이 주성분

# 2) 고유값이 설명가능한 분산비율(분산량): 클 수록 영향력 높음
var_ratio = pca.explained_variance_ratio_
print(var_ratio) 
# [0.92461872 0.05306648 0.01710261 0.00521218] = [PCA1 PCA2 PCA3 PCA4] 의미
# 주성분 분산비율의 합이 95% 이상이면 이에 해당하는 부분까지 주성분으로 지정
# 이때, PCA1 + PCA2 = 0.97로 95% 이상이기 때문에 2개 성분만 선택
# 4개 독립변수(X) -> 2개 독립변수(X) 차원 축소

# 3) 스크리 플롯 : 주성분 개수를 선택할 수 있는 그래프(Elbow Point : 완만해지기 이전 선택)
plt.bar(x = range(4), height=var_ratio)
plt.plot(var_ratio, color='r', linestyle='--', marker='o') ## 선 그래프 출력
plt.ylabel('Percentate of Variance Explained')
plt.xlabel('Principal Component')
plt.title('PCA Scree Plot')
plt.xticks(range(4), labels = range(1,5))
plt.show()
# [해설] 첫번째 분산 비율이 가장 높음
# PCA1 및 PCA2 두 독립변수(X)로 지정하는 것이 적절

# 4) 주성분 결정 : 분산비율(분산량) 95%에 해당하는 지점: PCA1 + PCA2 2번째 까지
X_pca=X_pca[:,:2] # PCA1 ~ PCA2
X_pca.shape # (150, 2)

##########################################
## 회귀분석과 분류분석에서 주성분 사용 예시
##########################################
from sklearn.linear_model import LinearRegression, LogisticRegression # model 생성
from sklearn.model_selection import train_test_split # dataset split
from sklearn.metrics import r2_score, mean_squared_error # 회귀분석 평가 도출
from sklearn.metrics import accuracy_score, confustion_matrix # 분류분석 평가 도출

X_pca # 회귀분석과 분류분석에서 사용되는 독립변수

# train_set, test_set 만들기
X_train, X_test, y_train, y_test = train_test_split(
    X_pca, y, test_size=0.3, random_state=123)

# 1) 회귀분석
linear_model=LinearRegression().fit(X_train,y_train)

# 모델 평가
r2_score=linear_model.score(X_test,y_test)
print('결정계수 =',r2_score)
# 결정계수 = 0.9230166602115436

# 2) 분류분석
logistic_model=LogisticRegression().fit(X_train,y_train)

# 모델 평가
acc_score=logistic_model.score(X_test,y_test)
print('분류 정확도 =',acc_score)
# 분류 정확도 = 0.9333333333333333
