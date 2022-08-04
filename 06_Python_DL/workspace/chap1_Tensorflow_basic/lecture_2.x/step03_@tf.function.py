# -*- coding: utf-8 -*-
"""
step06_@tf.function_ver2_x.py

3. @tf.function 함수 장식자
 - 대상 함수에서 python code 작성 지원 
 - tensorflow 환경에서 python code 사용할 수 있도록 함
"""

import tensorflow as tf 

# if 처리 
@tf.function # 함수장식자  
def if_fn(x) :
    # python code 작성 
    if x > 100 :
        y = x * 10
    else :
        y = x + 10
    return y


# while 처리 
@tf.function # tensorflow로 바꿈
def while_fn(i) :
    # python code
    while i < 100 :
        i += 1
    return i 

print(if_fn(10)) # 20
# tf.Tensor(20, shape=(), dtype=int32)

print(while_fn(0))
# tf.Tensor(100, shape=(), dtype=int32)















