'''
문2) bmi.csv 데이터셋을 이용하여 다음과 같이 softmax classifier 모델을 생성하시오. 
   조건1> bmi.csv 데이터셋 
       -> x변수 : height, weight 칼럼 
       -> y변수 : label(3개 범주) 칼럼
    조건2> w,b 변수 정의    
    조건3> 딥러닝 최적화 알고리즘 : Adam
    조건4> learning rage : 0.001 or 0.005 선택(분류정확도 높은것) 
    조건5> 반복학습, step 단위로 loss : <출력결과> 참고 
    조건6> 분류정확도 출력
    조건7> 앞쪽 예측치와 정답 15개 출력   
    
  <출력 결과>
step = 500 , loss = 0.44498476
step = 1000 , loss = 0.34861678
step = 1500 , loss = 0.28995454
step = 2000 , loss = 0.24887484
step = 2500 , loss = 0.2177721
step = 3000 , loss = 0.19313334
step = 3500 , loss = 0.17303815
step = 4000 , loss = 0.15629826
step = 4500 , loss = 0.1421249
step = 5000 , loss = 0.12996733
========================================
accuracy = 0.9769
========================================
y_pred :  [0 0 1 1 1 1 0 2 0 2 1 2 1 0 2]
y_true :  [0 0 1 1 1 1 0 2 0 2 1 2 1 0 2]  
========================================
'''

import tensorflow as tf # ver1.x
from sklearn.preprocessing import minmax_scale # x data 정규화(0~1)
from sklearn.preprocessing import OneHotEncoder # y data -> one hot
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd
 
# dataset load 
path = r'C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\06_Python_DL'
bmi = pd.read_csv(path+'/data/bmi.csv')
print(bmi.info())

# 칼럼 추출 
col = list(bmi.columns)
print(col) 

# X, y 변수 추출 
X = bmi[col[:2]] # x변수
y = bmi[col[2]] # y변수 

# 1. X, y변수 전처리 

# x_data 정규화 
x_data = minmax_scale(X)


# y변수 : one-hot encoding 
y_arr = np.array(y) # numpy 변환 
obj = OneHotEncoder()
y_data = obj.fit_transform(y_arr.reshape([-1, 1])).toarray()


# 1. X,Y변수 정의 : 공급형 변수 
X = tf.constant(x_data, tf.float32) # (20000, 2)
y = tf.constant(y_data, tf.float32) # (20000, 3)

# 2. w,b 변수 정의 
tf.random.set_seed(123)
w = tf.Variable(tf.random.normal(shape=[2, 3])) # [입력수, 출력수]
b = tf.Variable(tf.random.normal(shape=[3])) # [출력수]

# 3. 회귀방정식 
def linear_model(X) : # train, test
    y_pred = tf.matmul(X, w) + b  
    return y_pred

# 4. softmax 활성함수 적용 
def soft_fn(X):
    y_pred = linear_model(X)
    soft = tf.nn.softmax(y_pred)
    return soft

# 5. 손실 함수 정의  
def loss_fn() : #  인수 없음 
    soft = soft_fn(X) 
    loss = -tf.reduce_mean(y*tf.math.log(soft)+(1-y)*tf.math.log(1-soft))
    return loss


# 6. 최적화 객체 : learning rage = 0.001 or 0.005 선택(분류정확도 높은것) 
optimizer = tf.optimizers.Adam(learning_rate=0.001)

# 7. 반복학습 
for step in range(5000):
    optimizer.minimize(loss_fn, var_list=[w, b])
    if (step+1) % 500 == 0:
        print(f'step = {step+1}, loss = {loss_fn().numpy()}')
'''
step = 500, loss = 0.6323778033256531
step = 1000, loss = 0.5689172148704529
step = 1500, loss = 0.5200457572937012
step = 2000, loss = 0.4799061417579651
step = 2500, loss = 0.44606998562812805
step = 3000, loss = 0.41715019941329956
step = 3500, loss = 0.392038494348526
step = 4000, loss = 0.36987239122390747
step = 4500, loss = 0.350014865398407
step = 5000, loss = 0.3320111930370331
'''

# 8. 최적화된 model 검정 

# 1) 예측 확률
y_probs = soft_fn(X)
print(y_probs)
'''
[[0.04223554 0.42750597 0.5302585 ]
 [0.01226277 0.2930148  0.6947224 ]
 [0.2548348  0.5566307  0.18853453]
 ...
 [0.3013982  0.5354648  0.16313697]
 [0.62201816 0.31960487 0.05837692]
 [0.46127322 0.44095582 0.09777091]]
'''

# 2) 예측값 전환cast()
y_pred = tf.argmax(y_probs,axis=1)
print(y_pred)
# [2 2 1 ... 1 0 0]
y = tf.argmax(y,axis=1)

# 3) 분류 정확도 확인
acc = accuracy_score(y,y_pred)
print('accuracy =', acc)
# accuracy = 0.88855