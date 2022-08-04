# -*- coding: utf-8 -*-
"""
step02_regression_formul.py

다중선형회귀방정식 : X(입력) 2개 이상 
 y_pred = (X1 * w1 + X2 * w2) + b
 y_pred = tf.linalg.matmul(X, a) + b
"""

import tensorflow as tf 


# X, y 변수 정의 : 상수
X = [[1.0, 2.0], [1.2, 1.9]] # 독립변수 (2, 2)
y = 2.5  # 종속변수 (1)

# w, b 변수 정의 : 변수  
tf.random.set_seed(1) # 난수 seed값 
w = tf.Variable(tf.random.normal([2, 1])) # 2개 난수 
b = tf.Variable(tf.random.normal([1])) # 1개 난수 

print('w =',w)
'''
가중치:
[[-1.1012203],
 [ 1.5457517]]
'''
print('b =',b) # 편향: [0.40308788]

# 다중선형회귀모델 
def linear_model(X) : # 입력(X) -> y 예측치 
    y_pred = tf.linalg.matmul(X, w) + b  # 행렬곱 사용
    # y = w1 * X^2 + w2 * X + b
    return y_pred # y 예측치

# model 오차 : y - y 예측치
def model_err(X, y) : # 입력(X, y) -> y 오
    y_pred = linear_model(X) # 예측치 
    err = tf.math.subtract(y, y_pred) # 오차 = y - y 예측치
    '''
    X = [[1.0, 2.0]]
    w = [[-1.1012203],[ 1.5457517]]
    '''
    return err # 오차 반환


# 손실 함수 (Loss function = cost function) -> 손실값
def loss_fn(X, y) :
    err = model_err(X, y) # 오차 
    loss = tf.reduce_mean(tf.square(err)) # MSE  
    '''
    tf.square(): 부호 양수화, 패널티(오차 작으면 더 작게, 크면 더 크게)
    '''
    return loss

print('\n<<가중치, 편향 초기값>>')    
print('가중치(w) = %s, \n편향(b) = %.3f'%(w.numpy(), b))

for p in linear_model(X).numpy():
    print(p)

for i in range(len(X)): # 0 ~ 1
    print('y = %.3f'%y)
    print('y_pred = %.3f' %linear_model([X[i]]))
    print('model error =%.3f'%(model_err([X[i]], y))) # X변수: 1차원 -> 2차원 만들기    
    print('loss value = %s'%(loss_fn([X[i]], y).numpy()))
'''
# 1차
y = 2.500
y_pred = 2.393
model error =0.107
loss value = 0.011369721
# 2차
y = 2.500
y_pred = 2.019
model error =0.481
loss value = 0.23179235
'''
