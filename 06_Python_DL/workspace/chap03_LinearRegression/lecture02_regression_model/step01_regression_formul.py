# -*- coding: utf-8 -*-
"""
step01_regression_formul.py

단순 선형회귀방정식 
  y_pred = (w * X) + b
  - w: 기울기(가중치)
  - b: 편향(절편)
"""

import tensorflow as tf  # ver 2.3

# X, y 변수 : 상수 정의 -> 값 수정 불가능
X = tf.constant(6.5) # 독립변수
y = tf.constant(5.2) # 종속변수

# w, b 변수 : 변수 정의 -> 모델을 최적화하기 위해 수정 필요 (수정 가능)
w = tf.Variable(0.5) # 가중치(기울기)
b = tf.Variable(1.5) # 편향(절편)

# 단순선형회귀모델 
def linear_model(X) : # 입력(X) -> y 예측치 
    y_pred = tf.math.multiply(X, w) + b  # y = w * X + b
    return y_pred # y 예측치

# model 오차 : y - y 예측치
def model_err(X, y) : # 입력(X, y) -> y 오
    y_pred = linear_model(X) # 예측치 
    err = tf.math.subtract(y, y_pred) # 오차 = y - y 예측치
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
print('가중치(w) = %.3f, 편향(b) = %.3f'%(w, b))
# 가중치(w) = 0.500, 편향(b) = 1.500

print('model error =%.3f'%(model_err(X, y)))    
# model error =0.450
print('loss value = %.3f'%(loss_fn(X, y)))
# loss value = 0.202


# [2차] 가중치와 편향 수정
print('\n<<가중치, 편향 수정값>>')  
w.assign(0.6) # 0.5 -> 0.6 수정
b.assign(1.2) # 1.5 -> 1.2 수정

print('가중치(w) = %.3f, 편향(b) = %.3f'%(w, b))
# 가중치(w) = 0.600, 편향(b) = 1.200

print('model error =%.3f'%(model_err(X, y)))    
# model error =0.100
print('loss value = %.3f'%(loss_fn(X, y)))
# loss value = 0.010
# 손실이 감소했음
'''
딥러닝 최적화 알고리즘
 - 최적의 가중치(w)와 편향(b)로 수정(update) -> 손실(loss)이 0에 수렴
'''