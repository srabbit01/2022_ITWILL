'''
KNN(K-Nearest Neighbor) 알고리즘
  - 학습과정 없음 
  - Euclidean 거리계산식
'''
import numpy as np
import tensorflow as tf

# 알려진 집단 
p1 = [1.2, 1.1] # A집단 
p2 = [1.0, 1.0] # A집단 
p3 = [1.8, 0.8] # B집단 
p4 = [2, 0.9]   # B집단 

x_data = np.array([p1, p2, p3, p4]) # 알려진 범주 
label = ['A','A','B','B'] # 분류범주(Y변수)

y_data = [1.6, 0.85] # 분류대상(알려지지 않은 집단)

# x,y 변수 선언 : tensor 생성 
X = tf.constant(x_data, tf.float32) # 알려진 집단 
Y = tf.constant(y_data, tf.float32) # 알려지지 않은 집단(분류대상)

# Euclidean 거리계산식 
distance = tf.math.sqrt(tf.math.reduce_sum(tf.math.square(X-Y),axis=1))
print(distance) 


# 가장 가까운 거리 index 반환 
idx = tf.argmin(distance) # input, dimension

print('분류 index :', idx.numpy()) # 가장 거리가까운 색인   
# 분류 index : 2
      
print('분류 결과 : ', label[idx]) # 분류 결과: B
idx = tf.argsort(distance)
print(idx) # [2 3 0 1]