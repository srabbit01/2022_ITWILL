# -*- coding: utf-8 -*-
"""
step05_regression_model_iris2

다중선형회귀모델 : iris dataset 
 - y변수 : 1칼럼, X변수 : 2~4칼럼 
"""

import tensorflow as tf  # 딥러닝 최적화 알고리즘
from sklearn.datasets import load_iris # dataset 
from sklearn.model_selection import train_test_split # dataset split 
from sklearn.metrics import mean_squared_error # 평가 
from sklearn.preprocessing import minmax_scale # 정규화(0~1)

# 1. dataset load 
X, y = load_iris(return_X_y=True)

# X변수 정규화 
X_nor = minmax_scale(X)
type(X_nor) # numpy.ndarray

# y변수 : 1칼럼, X변수 : 2~4칼럼 
y_data = X_nor[:,0] # 1칼럼  - y변수 
x_data = X_nor[:,1:] # 2~4칼럼 - x변수 


# 2. train_test_split
x_train, x_test, y_train, y_test = train_test_split(
    x_data, y_data, test_size=0.3, random_state=123)
X_train.dtype # dtype('float64')


# 3. w, b 변수 정의 : update 대상 
tf.random.set_seed(123) # w,b 난수 seed값 지정 
w = tf.Variable(tf.random.normal(shape=[3, 1], dtype=tf.float64))
# [입력수, 출력수] = [독립변수 개수, 종속변수 개수]
# X변수 개수 3개
b = tf.Variable(tf.random.normal(shape=[1], dtype=tf.float64)) # [출력수]

w.dtype # tf.float32 -> tf.float64 변환 필요

# 4. 회귀모델 정의 : 행렬곱 이용 
def linear_model(X) : # X:입력 -> y 예측치 : 출력 
    y_pred = tf.linalg.matmul(X, w) + b 
    return y_pred 

'''
InvalidArgumentError:
    -> double tensor but is a float tensor
# type의 불일치로 발생
# 즉, X vs w 자료형 불일치 오류 -> 해결방법: 자료형 일치
'''

# 5. 손실/비용 함수 정의 - MSE
def loss_fn() : # 인수 없음 
    y_pred = linear_model(x_train) # y 예측치
    err = tf.math.subtract(y_train, y_pred) # y - y_pred 
    loss = tf.reduce_mean(tf.square(err)) # MSE 
    return loss 


# 6. 최적화 객체 생성 
optimize = tf.optimizers.Adam(learning_rate=0.1) 
'''
learning_rate=0.1: 빠른 속도 최소점 수렴 (step=100)
                  -> 30번 정도에 0에 거의 수렴 (불안정)
learning_rate=0.01: 안정적으로 최소점 수렴 (step=500)
                  -> 400번 정도에 0에 거의 수렴 (수렴 시간 증가)
'''
print('초기값 : w =', w.numpy(), ", b =", b.numpy())


# 7. 반복학습
loss_value = [] # step 단위 손실 저장

for step in range(100) : 
    optimize.minimize(loss=loss_fn, var_list=[w, b]) 
    
    # 10배수 단위 출력 
    if (step+1) % 10 == 0 :
        print('step =', (step+1), ', loss value =', loss_fn().numpy())
    
    # step 단위 손실 저장
    loss_value.append(loss_fn().numpy())
    '''
    step = 100 , loss value = 0.05592662787911901
    '''
    
# 8. 최적화된 model 검증: test_set 사용

# 1) MSE 계산
y_test_pred = linear_model(x_test)
mse = mean_squared_error(y_test, y_test_pred)
print("MSE =", mse)
# MSE = 0.07703066016380891

# 2) 손실(loss value) 시각화
import matplotlib.pyplot as plt
plt.plot(loss_value,'r-')
plt.ylabel('loss value')
plt.xlabel('epochs')
plt.show()
# 학습량이 늘어날 수록 0의 수렴정도가 높음을 볼 수 있음
# 너무 학습을 많이하면 과적합 우려가 있기 때문에 비슷한 값에서 멈추거나
# 그러러는 것이 좋음 -> 어느 순간 비슷한 값이기 때문
# 또한, 오차가 증가할 수도 있음

# 3) 실제값 및 예측값 시각화
plt.plot(x_test, y_test, 'y--')
plt.plot(x_test, y_test_pred, 'g-')
plt.show()



