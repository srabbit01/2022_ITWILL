'''
문2) 다음과 같은 상수와 사칙연산 함수를 이용하여 dataflow의 graph를 작성하여 
    tensorboard로 출력하시오.
    조건1> 상수 : x = 100, y = 50
    조건2> 계산식 : result = ((x - 5) * y) / (y + 20)
       -> 사칙연산 함수 이용 계산식 작성  
        1. sub = (x - 5) : tf.subtract(x, 5)
        2. mul = ((x - 5) * y) : tf.multiply(sub, y)
        3. add = (y + 20) : tf.add(y, 20)
        4. div = mul / add : tf.div(mul, add)
   조건3> 출력 graph : 첨부파일 참고      
'''
import tensorflow.compat.v1 as tf # ver 1.x
tf.disable_v2_behavior() # ver 2.x 사용안함 

# tensorboard 초기화 
tf.reset_default_graph()

# 1. 프로그램 정의

# 1) 상수 정의 
x = tf.constant(100, name = 'x')
y = tf.constant(50, name = 'y')

# 2) 계산식 정의 



# 2. 프로그램 실행


# 3. graph 시각화
