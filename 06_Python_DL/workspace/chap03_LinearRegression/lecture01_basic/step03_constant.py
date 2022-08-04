'''
 - 상수 생성 함수 
'''

import tensorflow as tf # ver2.x

'''
1. 상수 생성 함수
 tf.constant(value, dtype, shape) : 지정한 값(value)으로 상수 텐서 생성   
 tf.zeros(shape, dtype) : 모양과 타입으로 모든 원소가 0으로 초기화된 텐서 생성 
 tf.ones(shape, dtype) : 모양과 타입으로 모든 원소가 1로 초기화된 텐서 생성
 tf.identity(input) : 내용과 모양이 동일한 텐서 생성   
 tf.fill(shape, value) : 주어진 scalar값으로 초기화된 텐서 생성 
 tf.linspace(start, stop, num) : start~stop 범위에서 num수 만큼 텐서 생성  
 tf.range(start, limit, delta) : 시작, 종료, 증감 으로 텐서 생성 
'''
a = tf.constant(10, tf.int32, (2, 3)) # 상수 생성
print(a)

b = tf.zeros( (2, 3) ) # 0차원 생
print(b) # sess.run()
# dtype=tf.float32

c = tf.ones( (2, 3) )
print(c)

d = tf.identity(c)
print(d)

e = tf.fill((2, 3), 5) # (shape, value)
print(e) # sess.run(c)

f = tf.linspace(15.2, 22.3, 5) # (start, stop, num)
print(f) 
# tf.Tensor([15.2   16.975 18.75  20.525 22.3  ], shape=(5,), dtype=float32)

g = tf.range(10, 1.5, -2.5) # (start, stop, step)
print(g)
