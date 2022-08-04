# -*- coding: utf-8 -*-
"""
step04_regression_model_iris.py
- 단순선형회귀모델

tensorflow 가상환경에서 scikit-learn 설치   
(base) > conda activate tensorflow  
(tensorflow) > conda install -c conda-forge scikit-learn

- c: 채널 지정 옵
     특정 conda-forge라는 channel에서 다운받을 것 임을 의미
- conda-forage: anaconda에서 python 패키지를 모아놓은 채널
- 지정하지 않으면 기본 channel에서 다운
"""

import tensorflow as tf # 최적화 알고리즘 
import pandas as pd  # csv file 
from sklearn.preprocessing import minmax_scale # 정규화 (최소: 0 ~ 최대: 1)
from sklearn.metrics import mean_squared_error # model 평가


path=r'C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\06_Python_DL'
iris = pd.read_csv(path+'/data/iris.csv')
print(iris.info())

# 1. X, y data 생성
x_data = iris['Sepal.Length'] 
y_data = iris['Petal.Length']

x_data.dtype # dtype('float64')
x_data.mean() # 5.84
x_data.max() # 7.9
x_data.min() # 4.3

# [추가] x, y 변수 스케일링: 전처리
x_data = minmax_scale(x_data) # 함수 이용
y_data.max() # 6.9
y_data = y_data / 6.9 # 최댓값 이용


# 2. X, y변수 만들기     
X = tf.constant(x_data, dtype=tf.float32) # dtype 지정 
y = tf.constant(y_data, dtype=tf.float32) # dtype 지정 
X.dtype # tf.float32
y.dtype # tf.float32


# 3. a,b 변수 정의 : 초기값 - 난수  
tf.random.set_seed(123)
w = tf.Variable(tf.random.normal([1])) # 가중치 
b = tf.Variable(tf.random.normal([1])) # 편향 


# 4. 회귀모델 
def linear_model(X) : # 입력 : X -> y예측치 
    y_pred = tf.math.multiply(X, w) + b # 회귀방정식 
    return y_pred 


# 5. 손실/비용 함수(loss/cost function) : 손실반환(MSE)
def loss_fn() : # 인수 없음 
    y_pred = linear_model(X) # 예측치 
    err = tf.math.subtract(y, y_pred) # 오차 = 정답 - 예측치  
    loss = tf.reduce_mean(tf.square(err)) # MSE  
    return loss

# mean_squared_error() 함수 사용하기
y_pred = linear_model(X)
mean_squared_error(y,y_pred)

# 6. model 최적화 객체 : 오차의 최소점을 찾는 객체 
help(tf.optimizers.Adam) # 클래스
'''
tf.optimizers.Adam(learning_rate=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-07,
                   amsgrad=False, name='Adam', **kwargs)
'''
optimizer = tf.optimizers.Adam(learning_rate=0.5) # lr : 0.9 ~ 0.0001(e-04)

print(f'기울기(w) 초기값 = {w.numpy()}, 절편(b) 초기값 = {b.numpy()}')

# 7. 반복학습 : 100회
for step in range(100) :
    optimizer.minimize(loss=loss_fn, var_list=[w, b])#(손실값,update 대상변수)
    
    # step 단위 -> 손실값 -> a,b 출력 
    print('step =', (step+1), ", loss value =", loss_fn().numpy())
    # a, b 변수 update 
    print(f'기울기(w) = {w.numpy()}, 절편(b) = {b.numpy()}')
'''
< 스케일링 이전 >
- step = 100 , loss value = 1.4621327
- 기울기(w) = [0.84485525], 절편(b) = [-1.0397471]
< 스케일링 이후 >
- step = 100 , loss value = 0.015607685
- 기울기(w) = [0.9687343], 절편(b) = [0.12870644]
'''    

###################################################
### Best Learning Rate 찾기 (0.01 ~ 0.9)
###################################################
lr_list = [0.001, 0.01, 0.05, 0.1, 0.5, 0.9]

loss_value = [] # 각 모델의 손실 저장

for lr in lr_list:
    print('learning_rate =', lr)
    optimizer = tf.optimizers.Adam(learning_rate=lr)
    tf.random.set_seed(123)
    w = tf.Variable(tf.random.normal([1])) # 가중치 
    b = tf.Variable(tf.random.normal([1])) # 편향 
    for step in range(100) :
        optimizer.minimize(loss=loss_fn, var_list=[w, b])#(손실값,update 대상변수)
        '''
        # step == 100 인 손실 저장
        if (step+1) % 100 == 0:
            loss_value.append(loss_fn().numpy())
        '''
    print('loss_value =',loss_fn().numpy())
    loss_value.append(loss_fn().numpy())
    print('')
# 결과
print(loss_value)
# [0.38647237, 0.10009663, 0.017051268, 0.0156188505, 0.015607685, 0.01560764]

min(loss_value) # 1.1405457
'''
learning_rate = 0.01
loss_value = 0.10009663

learning_rate = 0.05
loss_value = 0.017051268

learning_rate = 0.1
loss_value = 0.0156188505

learning_rate = 0.5
loss_value = 0.015607685

learning_rate = 0.9
loss_value = 0.01560764
'''
# 가장 손실이 적은 것은 "learning_rate == 0.9" 이다.
# 그러나, learning_rate이 너무 작으면 과적합 발생 우려 존재


# 8. 최적화된 model 검증

# 1) 회귀선
import matplotlib.pyplot as plt

y_pred = linear_model(X) # 예측치

plt.plot(X, y, 'b--') # 산점도
plt.plot(X, y_pred, 'r-') # 회귀선
plt.show()

# 2) 평균제곱오차(MSE) 계산
mse = mean_squared_error(y, y_pred) # MSE
print('MES =', mse) # MES = 0.015607638

