'''
문) bmi.csv 데이터셋을 이용하여 다음과 같이 sigmoid classifier의 모델을 생성하시오. 
   조건1> bmi.csv 데이터셋 
       -> x변수 : 1,2번째 칼럼(height, weight) 
       -> y변수 : 3번째 칼럼(label)
   조건2> 딥러닝 최적화 알고리즘 : Adam
   조건3> learning rage = 0.01    
   조건4> 반복학습 : 2,000번, 200 step 단위로 loss 출력 
   조건5> 최적화 모델 테스트 :  분류정확도(Accuracy report) 출력 
   
 <출력결과>
step = 200 , loss = 0.532565
step = 400 , loss = 0.41763392
step = 600 , loss = 0.34404162
step = 800 , loss = 0.29450226
step = 1000 , loss = 0.25899038
step = 1200 , loss = 0.23218009
step = 1400 , loss = 0.2111086
step = 1600 , loss = 0.19401966
step = 1800 , loss = 0.17981105
step = 2000 , loss = 0.16775638
========================================
accuracy = 0.9601377301019732  
'''
import tensorflow as tf 
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import minmax_scale # x변수 정규화 
from sklearn.preprocessing import OneHotEncoder # y data -> one hot
import numpy as np
import pandas as pd
 
# csv file load
path = r'C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\06_Python_DL'
bmi = pd.read_csv(path+'/data/bmi.csv')
print(bmi.info())

bmi.label.value_counts()
'''
normal    7677
fat       7425
thin      4898 -> 제외
'''

# subset 생성 : label에서 normal, fat 추출 
bmi = bmi[bmi.label.isin(['normal','fat'])] # thin 범주 제외 
print(bmi.head())
print(bmi.info())

# x,y 변수 추출 
X = bmi[['height','weight']] # x변수(1,2칼럼)
y = bmi['label'] # y변수(3칼럼)
X.shape # (15102, 2)
y.shape # (15102,)


# 1. X, y변수 전처리 
x_data = minmax_scale(X) # x_data 정규화 

# y변수 : one-hot encoding 
y_arr = np.array(y) # numpy 변환 
obj = OneHotEncoder()
y_data = obj.fit_transform(y_arr.reshape([-1, 1])).toarray()
# 1차원 -> 2차원으로 수
y_data.shape # (15102, 2)
y_data # fat 0 -> [1., 0.], normal -> [0., 1.]

# 2. X,Y 변수 정의   
X = tf.constant(x_data, tf.float32) 
y = tf.constant(y_data, tf.float32)
 

# 3. w,b 변수 정의 : 초기값(정규분포 난수 )
w = tf.Variable(tf.random.normal([2, 2]))# [입력수,출력수]
b = tf.Variable(tf.random.normal([2])) # [출력수] 


# 4. 회귀방정식 
def linear_model(X) : # train, test
    y_pred = tf.linalg.matmul(X, w) + b 
    return y_pred # 2차원 


# 5. sigmoid 활성함수 적용 
def sig_fn(X):
    y_pred = linear_model(X)
    sig = tf.nn.sigmoid(y_pred) 
    return sig

# 6. 손실 함수 정의 : 손실계산식 수정 
def loss_fn() : #  인수 없음 
    sig = sig_fn(X) 
    loss = -tf.reduce_mean(y*tf.math.log(sig)+(1-y)*tf.math.log(1-sig))
    return loss


# 7. 최적화 객체 : learning_rate= 0.01
optimize=tf.optimizers.Adam(learning_rate=0.01)

# 8. 반복학습 : 반복학습 : 2,000번, 200 step 단위로 loss 출력 
for step in range(2000):
    optimize.minimize(loss=loss_fn, var_list=[w, b])
    # 200배수 단위 출력 
    if (step+1) % 200 == 0 :
        print('step =', (step+1), ", loss val = ", loss_fn().numpy())
'''
step = 200 , loss val =  0.46829262
step = 400 , loss val =  0.36844715
step = 600 , loss val =  0.30647874
step = 800 , loss val =  0.26450184
step = 1000 , loss val =  0.23409909
step = 1200 , loss val =  0.2109373
step = 1400 , loss val =  0.19259572
step = 1600 , loss val =  0.17762613
step = 1800 , loss val =  0.16511178
step = 2000 , loss val =  0.15444428
'''

# 9. model 최적화 테스트
y_pred = sig_fn(X) # sigmoid 함수 호출
print(y_pred) # 0~1 확률값
'''
[[0.21018824 0.7785534 ]
 [0.0610612  0.94931644]
 [0.00385016 0.9964119 ]
 ...
 [0.27426887 0.7139228 ]
 [0.6412116  0.3696376 ]
 [0.51976186 0.47160235]]
'''

# T/F -> 1/0
y_pred=tf.cast(sig_fn(X).numpy()>0.5,dtype=tf.float32).numpy()
print(y_pred)
'''
[[0. 1.]
 [0. 1.]
 [0. 1.]
 ...
 [0. 1.]
 [1. 0.]
 [1. 0.]]
'''

# 분류 정확도 확인
acc = accuracy_score(y, y_pred)
print('accuracy =', acc)
# accuracy = 0.9837107667858562

# 분류 평가지표 확인
report = classification_report(y, y_pred)
print(report)
'''
              precision    recall  f1-score   support

           0       0.99      0.97      0.98      7425
           1       0.97      0.99      0.98      7677

   micro avg       0.98      0.98      0.98     15102
   macro avg       0.98      0.98      0.98     15102
weighted avg       0.98      0.98      0.98     15102
 samples avg       0.97      0.98      0.98     15102
'''
