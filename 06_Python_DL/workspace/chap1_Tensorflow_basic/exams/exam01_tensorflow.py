'''
문1) 두 상수를 정의하고, 사칙연산(+,-,*,/)을 정의하여 결과를 출력하시오.
  조건1> 두 상수 이름 : a, b
  조건2> 변수 이름 : adder,subtract,multiply,divide
  조건3> 출력 : 출력결과 예시 참고
  
<<출력결과>>
a= 100
b= 20
===============
덧셈 = 120
뺄셈 = 80
곱셈 = 2000
나눗셈 = 5.0
'''

import tensorflow.compat.v1 as tf # ver1.x
tf.disable_v2_behavior() # ver2.0 사용안함 

'''프로그램 정의 영역'''

# 상수 정의 
a = tf.constant(100)
b = tf.constant(20) 

# 식 정의 
adder = a + b

# 변수 정의 
subtract = tf.Variable(a - b)
multiply = tf.Variable(a * b)
divide = tf.Variable(a / b)


'''프로그램 실행 영역'''
# session object 생성 
with tf.Session() as sess:
    # 상수 할당
    print('a =', sess.run(a))
    print('b =', sess.run(b))
    print('===============')
    # 식 할당
    print('덧셈 =', sess.run(adder))
    # 변수 초기화
    sess.run(tf.global_variables_initializer())
    # 변수 식 할당
    print('뺄셈 =', sess.run(subtract))
    print('곱셈 =', sess.run(multiply))
    print('나눗셈 =', sess.run(divide))
'''
a = 100
b = 20
===============
덧셈 = 120
뺄셈 = 80
곱셈 = 2000
나눗셈 = 5.0
'''








