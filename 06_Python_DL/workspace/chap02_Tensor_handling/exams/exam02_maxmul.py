'''
문2) 다음과 같이 X, a 행렬을 상수로 정의하고 행렬곱으로 연산하시오.
    단계1 : X, a 행렬 
        X 행렬 : iris 2~4번 칼럼으로 상수 정의 (tf.constant 이용)
        a 행렬 : [[0.2],[0.1],[0.3]] 값으로 상수 정의 (tf.constant 이용) 

    단계2 : 행렬곱 이용 y 계산하기  (tf.linalg.matmul 이용)

    단계3 : y 결과 출력
'''

import tensorflow as tf
import pandas as pd # ModuleNotFoundError
'''
가상환경에 pandas 설치
(base) > conda activate tensorflow
(tensorflow) > pip install pandas
'''

path=r"C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\06. Python DL"
iris = pd.read_csv(path+'\\data\\iris.csv')
iris.info()

#  단계1 : X, a 상수 정의 
X=iris.iloc[:,1:4]
X=tf.constant(X)
a=tf.constant([[0.2],[0.1],[0.3]])

# 단계2 : 행렬곱 식 정의 
X.get_shape() # TensorShape([150, 3])
a.get_shape() # TensorShape([3, 1])
mat=tf.linalg.matmul(X.numpy(),a.numpy()) # y = X * a
 
# 단계3 : 행렬곱 결과 출력 
print(mat.numpy())
mat.get_shape() # TensorShape([150, 1])
# 150행 1열
