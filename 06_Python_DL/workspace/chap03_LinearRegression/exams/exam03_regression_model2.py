'''
문3) load_boston 데이터셋을 이용하여 다음과 같이 선형회귀모델 생성하시오.
     <조건1> x변수 : boston.data,  y변수 : boston.target
     <조건2> w변수, b변수 정의 : tf.random.normal() 이용 
     <조건3> learning_rate=0.5
     <조건4> 최적화함수 : Adam
     <조건5> 학습 횟수 1,000회
     <조건6> 학습과정과 MSE 출력 : <출력결과> 참고 
     
 <출력결과>
step = 100 , loss = 4.646641273041386
step = 200 , loss = 1.1614418341428459
step = 300 , loss = 0.40125618834653615
step = 400 , loss = 0.21101471610402903
step = 500 , loss = 0.13666187210671069
step = 600 , loss = 0.09779346604325287
step = 700 , loss = 0.07608768653282329
step = 800 , loss = 0.06372023833861612
step = 900 , loss = 0.0566559217407318
step = 1000 , loss = 0.05266675679250506
=============================================
MSE= 0.04122129293175945
'''
import tensorflow as tf # ver2.0
# pip install sklearn
from sklearn.model_selection import train_test_split # datast splits
from sklearn.metrics import mean_squared_error # model 평가 
from sklearn.datasets import load_boston
from sklearn.preprocessing import minmax_scale # 정규화(0~1) 
import numpy as np

# 1. data loading
boston = load_boston()

# 변수 선택 
X = boston.data # x
y = boston.target # y : 숫자 class(0~2)

print(X.shape) # (506, 13)
print(y.shape) # (506,)

# y변수 정규화 
X = minmax_scale(X)
y = minmax_scale(y)

# 2. train/test split(70 vs 30)
X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=123)
X_train = tf.constant(X_train,dtype=tf.float64)
X_test = tf.constant(X_test,dtype=tf.float64)
y_train = tf.constant(y_train,dtype=tf.float64)
y_test = tf.constant(y_test,dtype=tf.float64)

# 3. w, b변수 정의 : tf.random.normal() 함수 이용 
tf.random.set_seed(123)
w =tf.Variable(tf.random.normal([13,1], 0.1, 1.0,dtype=tf.float64))
b = tf.Variable(tf.random.normal([1], 0.1, 1.0,dtype=tf.float64))

# 4. 회귀모델 : 행렬곱
def linear_model(X):
    y_pred = tf.linalg.matmul(X, w) + b
    return y_pred

# 5. 비용 함수 정의 : 예측치 > 오차 > 손실함수 
def loss_fn():
    # y_pred = tf.squeeze(linear_model(X_train))
    y_pred = linear_model(X_train)
    err = y_train - y_pred
    loss = tf.reduce_mean(tf.square(err))
    return loss

# 6. 최적화 객체
optimize = tf.optimizers.Adam(learning_rate=0.5) 

# 7. 반복학습 
loss_value=[]
for step in range(1000) :
    optimize.minimize(loss=loss_fn,var_list=[w,b])
    if (step+1) % 100 == 0:
        print(f"{step+1}. loss_value={loss_fn().numpy()}")
        # print(f"기울기(w)={w.numpy()}, y절편(b)={b.numpy()}")
    loss_value.append(loss_fn().numpy())
'''
100. loss_value=0.01183322217483741
200. loss_value=0.010339088513099799
300. loss_value=0.010056763558146473
400. loss_value=0.009983022293345665
500. loss_value=0.009969510261967983
600. loss_value=0.00996774943528779
700. loss_value=0.00996758512501668
800. loss_value=0.00996757418138966
900. loss_value=0.009967573666528123
1000. loss_value=0.00996757364969917
'''

# 8. 최적화된 model 평가

# 1) MSE 계산
y_pred = tf.squeeze(linear_model(X_test))

mse = mean_squared_error(y_test,y_pred)
print('MSE =', mse)
# MSE = 0.014027555676469282

# 2) 손실 시각화
import matplotlib.pyplot as plt
plt.plot(loss_value,'b-')
plt.show()


