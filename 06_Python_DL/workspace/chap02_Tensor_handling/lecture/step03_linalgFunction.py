'''
선형대수 연산 함수  
 ver 1.0          ->  ver 2.0 (출처와 이름이 조금 다름)
 tf.eye : 단위행렬 -> tf.linalg.eye(dim) 
 tf.diag : 대각행렬 -> tf.linalg.diag(x)  
 tf.matrix_determinant : 정방행렬의 행렬식 -> tf.linalg.det(x)
 tf.matrix_inverse : 정방행렬의 역행렬 -> tf.linalg.inv(x)
 tf.matmul : 두 텐서의 행렬곱 -> tf.linalg.matmul(x, y)

'''
dir(tf.linalg)

import tensorflow as tf
import numpy as np

# 정방행렬 데이터 생성 
x = np.random.rand(2, 2) # 지정한 shape에 따라서  0~1 난수 
y = np.random.rand(2, 2) # 지정한 shape에 따라서  0~1 난수 

print(x)
'''
[[0.06843783 0.71487126]
 [0.46407639 0.33219241]]
'''
print(y)
'''
[[0.09673592 0.73327855]
 [0.76694345 0.86786722]]
'''

eye = tf.linalg.eye(2) # 단위행렬
print(eye.numpy()) 
 
# 단위행렬 : one-hot-encoding(2진수)
'''
array([[1., 0.], - 'cat'
       [0., 1.]],- 'dog' dtype=float32)
'''

tf.linalg.eye(3).numpy()
'''
[[1., 0., 0.],
 [0., 1., 0.],
 [0., 0., 1.]]
'''

dia = tf.linalg.diag(x) # 대각행렬 
mat_deter = tf.linalg.det(x) # 정방행렬의 행렬식  
mat_inver = tf.linalg.inv(x) # 정방행렬의 역행렬

x.shape # (2 ,2)
y.shape # (2 ,2)
mat = tf.linalg.matmul(x, y) # 행렬곱 반환 

print(x)
print(dia.numpy()) 
print(mat_deter.numpy())
print(mat_inver.numpy())
print(mat.numpy())


## 행렬곱 
A = tf.constant([[1,2,3], [3,4,2], [3,2,5]]) # A행렬 
B = tf.constant([[15,3, 5], [3, 4, 2]]) # B행렬  

A.get_shape() # [3, 3]
B.get_shape() # [2, 3]

# 행렬곱 연산 
# mat_mul = tf.linalg.matmul(a=A, b=B)
'''
수일치 오류 발생  
InvalidArgumentError: Matrix size-incompatible: In[0]: [3,3], In[1]: [2,3] [Op:MatMul]
'''
mat_mul = tf.linalg.matmul(a=A, b=tf.transpose(B)) # A @ B.T
print(mat_mul.numpy()) # (3,2)
'''
[[36 17]
 [67 29]
 [76 27]]
'''



