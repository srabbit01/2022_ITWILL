'''
Hyper parameter : 사용자가 지정하는 파라미터
 - learning rate : model 학습율(0.9 ~ 0.0001)
 - iteration size : model 반복학습 횟수(epoch)
 - batch size : model 공급 데이터 크기  
'''

import matplotlib.pyplot as plt
import tensorflow as tf # ver2.0
from sklearn.datasets import load_iris

iris = load_iris() # 0-1에 근사한 변수 선택
X = iris.data
y_data = X[:, 2] # 꽃잎 길이(3)
x_data = X[:, 3] # 꽃잎 넓이(4)


# Hyper parameter
learning_rate = 0.0001 # 학습율
# Full Batch: 매 학습마다 전체 데이터 공급
iter_size = 1000 # 학습횟수 = Epoch
'''
1차 테스트 : lr = 0.001, iter size = 100 -> 안정적인 형태   
 - L1 = [0.36129874, 0.36109656, 0.3608953, 0.36069494, 0.36049542]
 - L2 = [0.18794602, 0.18771458, 0.18748684, 0.18726258, 0.18704152]
2차 테스트 : lr = 0.05, iter size = 100 -> 최솟점 수렴 속도 빠름
 - L1 = [0.27116588, 0.27109993, 0.27106762, 0.27100962, 0.27097365]
 - L2 = [0.1208567, 0.12086859, 0.12090678, 0.12092358, 0.12095731]
3차 테스트 : lr = 0.0001, iter size = 100 -> 최솟점 수렴 속도 느림
 - L1 = [2.823856, 2.8115783, 2.7993445, 2.787155, 2.77501]
 - L2 = [10.860677, 10.773175, 10.686348, 10.600191, 10.514697]
4차 테스트 : lr = 0.0001, iter size = 1000 -> 최솟점 수렴 속도 느림, 학습횟수 늘
 - L1 = [0.36058658, 0.36056653, 0.3605465, 0.36052647, 0.36050647]
 - L2 = [0.18715276, 0.18713032, 0.1871079, 0.18708552, 0.18706317]
 -> 안정적인 그래프 생
'''

X = tf.constant(y_data, dtype=tf.float32) 
Y = tf.constant(x_data, dtype=tf.float32) 
X.dtype # tf.float32

tf.random.set_seed(123)
a = tf.Variable(tf.random.normal([1]))
b = tf.Variable(tf.random.normal([1]))
a.dtype # tf.float32


# 4. 회귀모델 
def linear_model(X) : # 입력 X
    y_pred = tf.multiply(X, a) + b # y_pred = X * a + b
    return y_pred

# 5. 비용 함수 정의 
def loss_fn_l1() : # MAE : L1 loss function : Lasso 회귀  
    y_pred = linear_model(X) # 예측치 : 회귀방정식  
    err = Y - y_pred # 오차 
    loss = tf.reduce_mean(tf.abs(err)) 
    return loss

def loss_fn_l2() : # MSE : L2 loss function : Lidge 회귀  
    y_pred = linear_model(X) # 예측치 : 회귀방정식  
    err = Y - y_pred # 오차 
    loss = tf.reduce_mean(tf.square(err)) 
    return loss

# 6. model 최적화 객체 : 오차의 최소점을 찾는 객체  
optimizer = tf.optimizers.SGD(lr = learning_rate) 


loss_l1_val = [] # L1 cost value
loss_l2_val = [] # L2 cost value


# 7. 반복학습 : 100회 
for step in range(iter_size) : 
    # 오차제곱평균 최적화 : 손실값 최소화 -> [a, b] 갱신(update)
    optimizer.minimize(loss_fn_l1, var_list=[a, b])#(손실값, 수정 대상)
    optimizer.minimize(loss_fn_l2, var_list=[a, b])#(손실값, 수정 대상)
    
    # loss value save
    loss_l1_val.append(loss_fn_l1().numpy())
    loss_l2_val.append(loss_fn_l2().numpy())
    
       
       
##### 최적화된 model(L1 vs L2) 비교 #####
''' loss values '''
print('loss values')
print('L1 =', loss_l1_val[-5:])
# L1 = [0.34367743, 0.34355515, 0.3433542, 0.34317678, 0.34303176]
print('L2 =', loss_l2_val[-5:])
# L2 = [0.16947874, 0.16927758, 0.16912143, 0.16896556, 0.16877592]

'''L1,L2 loss, learning rate, iteration '''
plt.plot(loss_l1_val, '-', label='loss L1')
plt.plot(loss_l2_val, '--', label='loss L2')
plt.title('L1 loss vs L2 loss')
plt.xlabel('Generation')
plt.ylabel('Loss values')
plt.legend(loc='best')
plt.show()

