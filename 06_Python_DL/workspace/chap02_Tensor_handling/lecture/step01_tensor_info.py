'''
Tensor 정보 제공 함수 
 1. tensor shape
 2. tensor rank
 3. tensor size
 4. tensor reshape 
'''

import tensorflow as tf
print(tf.__version__) # 2.3.0

# 프로그램 정의 및 실행
# tf.constant(value, dtype, shape, name) # name: tensorboard 시각화 시 이름
scala = tf.constant(1234) # 상수 
vector = tf.constant([1,2,3,4,5]) # 1차원 
matrix = tf.constant([ [1,2,3], [4,5,6] ]) # 2차원
cube = tf.constant([[ [1,2,3], [4,5,6], [7,8,9] ]]) # 3차원 

print(scala) # shape=()
print(vector) # shape=(5,)
print(matrix) # shape=(2, 3)
print(cube) # shape=(1, 3, 3)

# 1. tensor shape : 객체의 모양 확인
print('\ntensor shape')
print(scala.get_shape()) # () scalar.shape
print(vector.get_shape()) # (5,)
print(matrix.get_shape()) # (2, 3)
print(cube.get_shape()) # (1, 3, 3)
vector.shape # TensorShape([5])
matrix.shape # TensorShape([2, 3])
  
# 2. tensor rank : 객체의 차원 확인
print('\ntensor rank')
print(tf.rank(scala)) # 0
print(tf.rank(vector)) # 1
print(tf.rank(matrix)) # 2
print(tf.rank(cube)) # 3

# 3. tensor size : 객체 내 원소 크기(개수) 확인
print('\ntensor size')
print(tf.size(scala)) # 1
print(tf.size(vector)) # 5
print(tf.size(matrix)) # 6
print(tf.size(cube)) # 9

# 4. tensor reshape : 모양은 바꿀 수 있으나, 원소의 크기 수정 X
cube_2d = tf.reshape(tensor=cube,shape=(3,3)) # 3d -> 2d
print(cube_2d)
'''
[[1 2 3]
 [4 5 6]
 [7 8 9]]
'''