# -*- coding: utf-8 -*-
"""
step03_scaling_linearRegression.py

특징변수 데이터변환(features scaling) : 5장 참고  
 1. 특징변수(x변수) : 값의 크기(scale)에 따라 model 영향을 미치는 경우
   1) 정규화 : 변수의 값을 일정 범위로 조정(0~1, -1~+1) 
   2) 표준화 : 표준화 공식 Z이용(평균=0, 표준편차=1) 
             Z = (X - mu) / sigma
   3) 로그변환 = log()함수 이용 
   - model 성능 평가로 데이터변환 방법 결정 

 2. 타깃변수(y변수) : 로그변환 
"""

from sklearn.datasets import load_boston # dataset 
from sklearn.model_selection import train_test_split # split 
from sklearn.linear_model import LinearRegression # model 
from sklearn.metrics import mean_squared_error, r2_score # 평가 

from sklearn.preprocessing import minmax_scale # 정규화(0~1)
from sklearn.preprocessing import scale # 표준화(평균: 0, 표준편차: 1)
# from scipy.stats import zscore # 위와 동일
import numpy as np # 로그변환: np.log1p(np.abs(x))

# 1. dataset load
X, y = load_boston(return_X_y = True)
X.shape # (506, 13)

# x,y변수 스케일링 안됨 
X.mean() # 70.07396704469443
X.max() # 711.0
X.min() # 0.0

y.mean() # 22.532806324110677

# 2. 피처 스케일링(features scaling)  
def scaling(X, y, kind='none') : # kind: 스케일링 방법 지정 (기본: none)
    # x변수 스케일링  
    if kind == 'minmax_scale' : # 정규화
        from sklearn.preprocessing import minmax_scale 
        X_trans = minmax_scale(X) 
    elif kind == 'zscore' : # 표준화
        from sklearn.preprocessing import scale
        X_trans = scale(X) # zscore(X)
    elif kind == 'log' :  
        import numpy as np 
        X_trans = np.log1p(np.abs(X)) 
    else : # 기본: 스케일링하지 않음
        X_trans = X 
    
    # y변수 로그변환 
    if kind != 'none' : # kind=none이 아니면 로그변환하기
        import numpy as np 
        y = np.log1p(np.abs(y))   
    
    # train/test split 
    X_train,X_test,y_train,y_test = train_test_split(
        X_trans, y, test_size = 30, random_state=1)   
    
    print(f"scaling 방법 : {kind}, X 평균 = {X_trans.mean()}")
    return X_train,X_test,y_train, y_test


# 함수 호출 
# X_train,X_test,y_train,y_test = scaling(X, y,'none') # 1. 스케일링하지 않음
# X_train,X_test,y_train,y_test = scaling(X, y,'minmax_scale') # 2. 정규화
# X_train,X_test,y_train,y_test = scaling(X, y,'zscore') # 3. 표준화
# X_train,X_test,y_train,y_test = scaling(X, y,'log') # 4. 로그화

# 3. model 생성하기
model = LinearRegression().fit(X=X_train, y=y_train)  


# 4. model 평가하기
model_train_score = model.score(X_train, y_train) 
model_test_score = model.score(X_test, y_test) 
print('model train score =', model_train_score)
print('model test score =', model_test_score)


y_pred = model.predict(X_test)
y_true = y_test
print('R2 score =',r2_score(y_true, y_pred))  
mse = mean_squared_error(y_true, y_pred)
print('MSE =', mse)

'''
# 1. 스케일링하지 않은 기본: X와 y는 스케일링 전
scaling 방법 : none, X 평균 = 70.07396704469443
model train score = 0.7410721208614651
model test score = 0.7170463430870486
R2 score = 0.7170463430870486
MSE = 20.200831829748306

# 2. X: 정규화, y: 로그화
scaling 방법 : minmax_scale, X 평균 = 0.3862566314283195
model train score = 0.7910245321591743
model test score = 0.7633961405434471
R2 score = 0.7633961405434471
MSE = 0.027922682660046303
# 이전보다 성능이 더 높아짐을 알 수 있음
# [해설] 정확도 향상, MSE: 0 수렴정도 평가 가능

# 3. X: 표준화, y: 로그화
scaling 방법 : zscore, X 평균 = -1.1147462804871136e-15
model train score = 0.7910245321591743
model test score = 0.7633961405434475
R2 score = 0.7633961405434475
MSE = 0.027922682660046248
# [해설] 정규화와 정확도 및 MSE 결과 동일 -> 둘 중 하나만 하면 됨

# 4. X: 로그화, y: 로그화
scaling 방법 : log, X 평균 = 2.408779096889065
model train score = 0.7971243680501753
model test score = 0.8217362767578846
R2 score = 0.8217362767578846
MSE = 0.021037701520680113
# [해설] 기존의 정규화나 표준화보다 결과가 더 좋음
# 주의: 그러나, Test 점수가 높은 불완전한 결과가 나타남
# 따라서, 대부분 X변수는 표준화 혹은 정규화, y변수는 로그화 적용
'''

