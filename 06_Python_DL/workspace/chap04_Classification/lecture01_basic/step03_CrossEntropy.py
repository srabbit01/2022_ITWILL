"""
Entropy : 일반 용어 
 - 확률변수 p에 대한 불확실성의 측정 지수 
 - 값이 클 수록 일정한 방향성과 규칙성이 없는 무질서(chaos)를 의미
 - Entropy = -sum(p * log(p))
"""

import numpy as np

# 1. 불확실성이 큰 경우(p1: 앞면, p2: 뒷면)
p1 = 0.5; p2 = 0.5

entropy = -(p1 * np.log2(p1) + p2 * np.log2(p2)) 
print('entropy =', entropy) # entropy = 1.0


# 2. 불확실성이 작은 경우(x1: 앞면, x2: 뒷면) 
p1 = 0.9; p2 = 0.1

entropy = -(p1 * np.log2(p1) + p2 * np.log2(p2)) # 공통부호 정리
print('entropy =', entropy) # entropy = 1.0



'''
Cross Entropy  
  - 두 확률변수 x, y가 있을 때 x를 관찰한 후 y에 대한 불확실성 측정
  - 딥러닝 분류기 : 정답(y)을 관찰한 후 예측치(y_pred)의 손실 계산
  - Cross 의미 :  y=1과  y=0 일때 서로 교차하여 손실 계산 
  - 식 = -( y * log(y_pred) + (1-y) * log(1-y_pred))
    
  왼쪽 식   : y * log(y_pred) -> y=1 일때 손실값 계산 
  오른쪽 식 : (1-y) * log(1-y_pred) -> y=0 일때 손실값 계산 
'''

import tensorflow as tf

y_pred = [0.02, 0.98] # model 예측치

y = 1 # 정답(y)
# y_pred = [손실큼, 손실작음]
for pred in y_pred:
    loss_val = -(y * tf.math.log(pred))
    print(loss_val.numpy())
'''
실제 y=1인 경우,
y_pred=0.02 -> 3.912023
y_pred=0.98 -> 0.020202687
'''

y = 0 # 정답(y)
for pred in y_pred:
    loss_val = -((1-y)*tf.math.log(1-pred))
    print(loss_val.numpy())
'''
실제 y=0인 경우,
y_pred=0.02 -> 0.020202687
y_pred=0.98 -> 3.912023
'''

# Cross Entropy: -( y * log(y_pred) + (1-y) * log(1-y_pred))

y = 0; y = 1# 정답(y): y = 0인 경우, y = 1인 경우 모두 구하기
for pred in y_pred:
    loss_val = -tf.reduce_sum((y*tf.math.log(pred)+(1-y)*tf.math.log(1-pred)))
    print(loss_val.numpy())
'''
1) 실제 y=1인 경우,
   y_pred=0.02 -> 3.912023
   y_pred=0.98 -> 0.020202687
2) 실제 y=0인 경우,
   y_pred=0.02 -> 0.020202687
   y_pred=0.98 -> 3.912023
'''



