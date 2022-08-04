# -*- coding: utf-8 -*-
"""
step01_eager_execution.py

Tensorflow 2.x에서 변화된 실행방법

Tensorflow 2.x 특징 
1. 즉시 실행(eager execution) 모드
 - session 사용 없이 자동으로 컴파일 
 - python처럼 즉시 실행하는 모드 제공
 - API 정리 : tf.global_variables_initializer() 삭제됨 
"""

### 주의 : Spyder 재실행 

import tensorflow as tf # ver 2.x 최신버젼 사용 
# tensorflow 버전 확인
print(tf.__version__) # 2.3.0

# 즉시 실행 모드 
tf.executing_eagerly() # default 활성화


# 상수 정의   
a = tf.constant(value = [[1,2], [3,4]], dtype=tf.float32)
print(a) # tensor 정보 및 실행 결과 출력
a
'''
tf.Tensor(
[[1. 2.]
 [3. 4.]], shape=(2, 2), dtype=float32)
'''

# 식 정의 + 실행
b = tf.add(x=a, y=0.5) # b = a + 0.5
print(b)
'''
tf.Tensor(
[[1.5 2.5]
 [3.5 4.5]], shape=(2, 2), dtype=float32)
'''
print(b.numpy())
'''
[[1.5 2.5]
 [3.5 4.5]]
'''

# python 데이터 이용 
X = [[2.0, 3.0]] 
a = [[1.0], [1.5]] 

# 행렬곱(행렬내적)
mat = tf.linalg.matmul(X, a)
print(mat)
# tf.Tensor([[11. 16.]], shape=(1, 2), dtype=float32)

# tensor 정보 외 계산 결과만 반환 받고자 할 때
print(mat.numpy())
# [[11. 16.]]
# 별도로 해당 변수를 사용하기 위해 필요


# 변수 정의 + 초기화 + 실행: 수정 가능
c = tf.Variable([1.0, 2.0, 3.0]) # 1차원 변수
print(c)
# <tf.Variable 'Variable:0' shape=(3,) dtype=float32, numpy=array([1., 2., 3.], dtype=float32)>
print(c.numpy()) # [1. 2. 3.]

# 상수 정의 + 실행
d = tf.constant([1.5,3.5,4.5]) # 1차원 상수

# 식 정의 + 실행
mul = c * d
print(mul) # tf.Tensor([ 1.5  7.  13.5], shape=(3,), dtype=float32)
print(mul.numpy()) # [ 1.5  7.  13.5]
