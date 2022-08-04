'''
수학 관련 주요 함수 
version 1.x   -> version 2.x
tf.add() -> tf.math.add() 변경 
tf.subtract() -> tf.math.subtract() 변경 
tf.multiply() -> tf.math.multiply() 변경 
tf.div() -> tf.math.divide() 변경 
tf.mod() : 나머지 -> tf.math.mod() 변경 
tf.abs() : 절대값 -> tf.math.abs() 변경 
tf.square() : 제곱  -> tf.math.square() 변경
tf.sqrt() : 제곱근  -> tf.math.sqrt() 변경
tf.round() : 반올림  -> tf.math.round() 변경
tf.pow() : 거듭제곱 -> tf.math.pow() 변경
tf.exp() : 지수값 -> tf.math.exp() 변경
tf.log() : 로그값 -> tf.math.log() 변경
'''

import tensorflow as tf

# 상수 정의 + 실행
x = tf.constant([1,2,-3,4])
y = tf.constant([5,6,7,8])


# 덧셈/뺄샘/나눗셈/곱셈
print(tf.math.add(x, y, name='adder'))
print(tf.math.subtract(x, y, name='adder'))
print(tf.math.multiply(x, y, name='adder'))
print(tf.math.divide(x, y, name='divide'))
print(tf.math.mod(x, y, name='mod')) # [1 2 4 4]

# 음수, 부호 반환 
print('tf.neg=', tf.math.negative(x)) # [-1 -2  3 -4]
print('tf.sign=', tf.math.sign(x)) # [ 1  1 -1  1]

# 제곱/제곱근/거듭제곱 
print(tf.math.abs(x)) # [1 2 3 4]
print(tf.math.square(x)) # 제곱 - [ 1  4  9 16]
print(tf.math.sqrt([4.0, 9.0, 6.0])) # 제곱근
print(tf.math.pow(x, 3)) # 거듭제곱-[  1   8 -27  64]

# 지수와 로그 
print('e=', tf.math.exp(1.0).numpy()) # e= 2.7182817
print(tf.math.exp(2.0))  # 7.389056
print(tf.math.log(8.0)) # e^? = 2.0794415

e= 2.7182817
print(tf.math.pow(e,2.0794415))


# sigmoind function: 활성함수(이항분류)
'''
f(x) = 1 / (1 + exp(-x))
'''
def sig_fn(x):
    exp=tf.math.exp(-x)
    y=1/(1+exp)
    return y.numpy()
# x = -5 ~ 5
for i in range(-5,6):
    y=sig_fn(float(i))
    print(f"x : {i} -> y : {y}")
'''
x : -5 -> y : 0.006692850962281227 -> 0 수렴
x : -4 -> y : 0.01798621006309986
x : -3 -> y : 0.04742587357759476
x : -2 -> y : 0.11920291930437088
x : -1 -> y : 0.2689414322376251
x : 0 -> y : 0.5                  -> cut off
x : 1 -> y : 0.7310585975646973
x : 2 -> y : 0.8807970285415649
x : 3 -> y : 0.9525741338729858
x : 4 -> y : 0.9820137619972229
x : 5 -> y : 0.9933071732521057   -> 1 수렴
'''
