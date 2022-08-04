# -*- coding: utf-8 -*-
"""
step04_model_plot.py

 - 분석모델 관련 시각화
"""

import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sn

# seaborn 한글과 음수부호, 스타일 지원 
sn.set(font="Malgun Gothic", 
            rc={"axes.unicode_minus":False}, style="darkgrid")


# dataset 로드 
flights = sn.load_dataset('flights') # 탑긍 고객 관련 데이터
flights.info()
'''
 0   year        144 non-null    int64    -> x:시간축 
 1   month       144 non-null    category -> 집단변수 
 2   passengers  144 non-null    int64    -> y:탑승객 수
'''
1960-1945 # 15년 관측
15*12 # 180개 데이터

iris = sn.load_dataset('iris')
iris.info()

# 1. 오차대역폭을 갖는 시계열 : x:시간축, y:통계량 
sn.lineplot(x = 'year', y = 'passengers', data = flights)
plt.show()

# hue 추가 
sn.lineplot(x = 'year', y = 'passengers', hue='month',
            data = flights)
# 위: 상한값, 아래: 하한값 
plt.show()
 

# 2. 선형회귀모델 : 산점도 + 회귀선 
sn.regplot(x = 'sepal_length', y = 'petal_length',  data = iris)  
# hue가 제공되지 않음
plt.show()

# 산점도+ 회귀선 + hue 제공
sn.lmplot(x = 'sepal_length', y = 'petal_length', hue='species', data = iris)  

# 3. heatmap : 분류분석 평가 
y_true = pd.Series([1,0,1,1,0]) # 정답 -> 이항
y_pred = pd.Series([1,0,0,1,0]) # 예측치 
# 4개 정답 1개 오답

# 1) 교차분할표(혼동 행렬) 
tab = pd.crosstab(y_true, y_pred, 
            rownames=['관측치'], colnames=['예측치']) # 정답->정답 확인
'''
예측치  0  1
관측치       
   0    2  0
   1    1  2
'''
type(tab) # pandas.core.frame.DataFrame

# 분류정확도
score=(tab.iloc[0,0]+tab.iloc[1,1])/len(y_true) # 0.8
# 대각행렬 합 / 길이

import numpy as np # np.diag(): 대각선 원소만 추출
sum(np.diag(tab))/len(y_true)

# 2) heatmap
sn.heatmap(data=tab, annot = True) # annot = True : box에 빈도수 
acc_score=f'Accuracy Score: {score}'
plt.title(acc_score,size=18)
plt.show()






