# -*- coding: utf-8 -*-
"""
step01_sigmiod_classfier.py

이항분류기 : : 테스트 데이터 적용
"""

import tensorflow as tf
from sklearn.metrics import accuracy_score #  model 평가 

# 1. x, y 공급 data 
# x변수 : [x1=hours, x2=video]
x_data = [[1, 2], [2, 3], [3, 1], [4, 3], [5, 3], [6, 2]] # [6, 2] = 2개 변수의 수

# y변수 : [fail(1), pass(1)] -> one-hot encoding
y_data = [[1,0], [1,0], [1,0], [0,1], [0,1], [0,1]] # [6, 2] = 2개 범주의 수 -> 이항분류 적합
#        -> 3개 실패(fail), 3개 성공(pass)

# 2. X, Y변수 정의 : type 일치 - float32
X = tf.constant(x_data, tf.float32) # [6, 2] = [관측치, X변수]
y = tf.constant(y_data, tf.float32) # [6, 2] = [관측치, y변수]


# 3. w, b변수 정의 : 초기값(난수) -> update 
# 기본 자료형: tf.float32
w = tf.Variable(tf.random.normal(shape=[2, 2])) # shape = [입력수, 출력수]
b = tf.Variable(tf.random.normal(shape=[2])) # shape = [출력수]


# 4. 회귀모델 
def linear_model(X) :
    model = tf.linalg.matmul(X, w) + b # 회귀방정식 
    '''
    X[6,2] @ w[2,2]
    '''
    return model 
    
# 5. sigmoid 함수 : 이항분류 활성함수
def sig_fn(X) :
    model = linear_model(X)
    y_pred = tf.nn.sigmoid(model) # sigmoid(y예측치) -> 0~1 확률
    return y_pred 
    
# 6. 손실함수 
def loss_fn() : # 인수 없음 
    y_pred = sig_fn(X)
    # loss value: Cross Entropy 손실 함수
    loss = -tf.reduce_mean(y * tf.math.log(y_pred) + (1-y) * tf.math.log(1-y_pred))
    return loss


# 7. 최적화 객체 
opt = tf.optimizers.Adam(learning_rate=0.5)


# 8. 반복학습 
for step in range(100) :
    opt.minimize(loss=loss_fn, var_list=[w, b])
    
    # 10배수 단위 출력 
    if (step+1) % 10 == 0 :
        print('step =', (step+1), ", loss val = ", loss_fn().numpy())
'''
step = 10 , loss val =  1.0114925
step = 20 , loss val =  0.46409345
step = 30 , loss val =  0.35252297
step = 40 , loss val =  0.2649679
step = 50 , loss val =  0.18138544
step = 60 , loss val =  0.13212407
step = 70 , loss val =  0.107801355
step = 80 , loss val =  0.09096158
step = 90 , loss val =  0.07803789
step = 100 , loss val =  0.068255484
'''

# 9. 모델 검정
y_pred = sig_fn(X) # sigmoid 함수 적용
print(y_pred)
'''
   fail(0)     pass(1)
[[0.9970443  0.00415954]
 [0.9238274  0.08652565]
 [0.9007742  0.11194944]
 [0.1060569  0.8803314 ]
 [0.01159793 0.9848093 ]
 [0.00318253 0.9955161 ]]
'''

# fail: [1, 0], pass: [0, 1]

# 확률예측치 -> 0 or 1 = 예측 결과 동일
# 0.5 초과면 1, 0.5 이하면 0으로 지정
y_pred=tf.cast(sig_fn(X).numpy()>0.5,dtype=tf.float32).numpy() # 자료형 변경
# T/F -> 1/0
print(y_pred)
'''
[[1., 0.],
 [1., 0.],
 [1., 0.],
 [0., 1.],
 [0., 1.],
 [0., 1.]]
'''

# 분류 정확도 확인
acc = accuracy_score(y, y_pred)
print('accuracy =', acc)
# accuracy = 1.0
