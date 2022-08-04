# -*- coding: utf-8 -*-
"""
scipy 패키지 이용 
 1. 단순선형회귀분석 
 2. 다중선형회귀분석 
"""

from scipy import stats # 회귀분석
import pandas as pd # csv file
import os # file path 설정

# os.chdir(r'C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML\data')
path=r'C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML\data'
score_iq = pd.read_csv(path+'/score_iq.csv')
score_iq.info()

# 1. 단순선형회귀분석 
'''
x -> y
'''

# 1) 변수 생성 
x = score_iq['iq'] # 독립변수 
y = score_iq['score'] # 종속변수 

# 2) model 생성 
model = stats.linregress(x, y)
print(model)
'''
LinregressResult(
    slope=0.6514309527270075, : x 기울기 
    intercept=-2.8564471221974657, : y 절편 
    rvalue=0.8822203446134699, : 설명력
    pvalue=2.8476895206683644e-50, : F검정 : 유의성검정 
    stderr=0.028577934409305443) : 표준오차 
'''

x[0] # 140
y[0] # 90

a = model.slope # x 기울기
b = model.intercept # y 절편 

# 회귀방정식 -> y 예측치 
X = 140; Y = 90 # 1개 관측치 

y_pred = (X*a) + b
print(y_pred) # 88.34388625958358

err = Y - y_pred # 실제 - 예측 = 오차
print('err=', err) # err= 1.6561137404164157

# 전체 관측치 대상 
len(x) # 150
y_pred = (x*a) + b # 예측치 
len(y_pred) # 150

# 관측치 vs 예측치 
print('관측치 평균 : ', y.mean())
print('예측치 평균 : ', y_pred.mean())

print(y[:10])
print(y_pred[:10])


# 2. 회귀모델 시각화 
from pylab import plot, title, legend, show # 회귀분석 시각화 함수
'''
plot : 산점도 
title, legend : 제목, 범례 
show : 차트 보이기 
'''

# 산점도 
plot(score_iq['iq'], score_iq['score'], 'b.')
# 회귀선 
plot(score_iq['iq'], y_pred, 'r.-')
title('line regression') # 제목 
legend(['x y scatter', 'line regression']) # 범례 
show()



# 3. 다중선형회귀분석 : formula 형식 
from statsmodels.formula.api import ols

# 상관계수 행렬 
corr = score_iq.corr()
print(corr['score'])
'''
sid       -0.014399
score      1.000000
iq         0.882220
academy    0.896265
game      -0.298193
tv        -0.819752
'''

obj = ols(formula='score ~ iq + academy + tv', data = score_iq)
dir(obj)

print(obj)
model = obj.fit() # 회귀모델 생성

# 회귀분석 결과 제공  
print(model.summary()) 
'''
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                  score   R-squared:                       0.946
Model:                            OLS   Adj. R-squared:                  0.945
Method:                 Least Squares   F-statistic:                     860.1
Date:                Tue, 03 May 2022   Prob (F-statistic):           1.50e-92
Time:                        12:42:54   Log-Likelihood:                -274.84
No. Observations:                 150   AIC:                             557.7
Df Residuals:                     146   BIC:                             569.7
Df Model:                           3                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept     24.7223      2.332     10.602      0.000      20.114      29.331
iq             0.3742      0.020     19.109      0.000       0.335       0.413
academy        3.2088      0.367      8.733      0.000       2.483       3.935
tv             0.1926      0.303      0.636      0.526      -0.406       0.791
==============================================================================
Omnibus:                       36.802   Durbin-Watson:                   1.905
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               57.833
Skew:                           1.252   Prob(JB):                     2.77e-13
Kurtosis:                       4.728   Cond. No.                     2.32e+03
==============================================================================
'''
# Adj. R-squared: 수정된 결정계수
# F-statistic: F 검정통계량, Prob: 확률값
# Intercept: 절편
# P>|t| 각 값의 p-value -> 영향을 미치는 요인인지 확인이 가능 (0.05 이상이면 영향 X)
# coef: 기울기

# 회귀계수값 반환 
print('회귀 계수값\n%s'%(model.params))
'''
Intercept    24.722251
iq            0.374196
academy       3.208802
tv            0.192573
dtype: float64
'''
model.params.iq

# 다중회귀방정식 : 첫번째 관측치 적용 예 
score_iq.head()
y = 90
x1 = 140
x2 = 2
x3 = 0

y_pred = (x1*0.374196 + x2*3.208802 + x3*0.192573) + 24.722251
print('예측치 :', y_pred) # 예측치 : 83.527295
print('관측치 :', y) # 관측치 : 90
print('오차(잔차) :', y - y_pred) # 6.472705000000005


# model의 적합치 
print('model 적합치')
print(model.fittedvalues) # 예측치
'''
0      83.527304
1      75.283280
2      73.604873
3      82.041469
4      64.783130
   
145    82.041469
146    64.783130
147    80.567345
148    64.783130
149    82.041469
'''
y_true=score_iq.score # 관측치
y_pred=model.fittedvalues # 예측치

df=pd.DataFrame({'y_true':y_true,'y_pred':y_pred},columns=['y_true','y_pred'])
df.head()
'''
   y_true     y_pred
0      90  83.527304
1      75  75.283280
2      77  73.604873
3      83  82.041469
4      65  64.783130
'''
df.tail()

df.mean(axis=0)
'''
실제 vs 예측 평균
y_true    77.773333
y_pred    77.773333
'''

# 차트 시각화
import matplotlib.pyplot as plt
plt.plot(y_pred[:50],label='predicted values')
plt.plot(y_true[:50],label='real values')
plt.legend(loc='best')
plt.show()