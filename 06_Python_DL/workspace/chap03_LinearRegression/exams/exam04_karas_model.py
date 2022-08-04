# -*- coding: utf-8 -*-
"""
문4) boston 데이터셋을 이용하여 다음과 같이 Keras DNN model layer을 
    구축하고, model을 학습하고, 검증(evaluation)하시오. 
    <조건1> 4. DNN model layer 구축 
         1층(hidden layer1) : units = 64
         2층(hidden layer2) : units = 32
         3층(hidden layer3) : units = 16 
         4층(output layer) : units=1
    <조건2> 6. model training  : 훈련용 데이터셋 이용 
            epochs = 50
    <조건3> 7. model evaluation : 검증용 데이터셋 이용     
"""
from sklearn.datasets import load_boston  # dataset
from sklearn.model_selection import train_test_split # split
from sklearn.preprocessing import minmax_scale # 정규화(0~1) 
from sklearn.metrics import mean_squared_error, r2_score


# keras model 관련 API
import tensorflow as tf # ver 2.0
from tensorflow.keras import Sequential # model 생성 
from tensorflow.keras.layers import Dense # DNN layer
print(tf.keras.__version__) # 2.2.4-tg
# 2.4.0

# 1. x,y data 생성 
X, y = boston = load_boston(return_X_y=True)
X.shape # (442, 10)
y.shape # (442,)

# y 정규화 
X = minmax_scale(X)
y = minmax_scale(y)

# 2. 공급 data 생성 : 훈련용, 검증용 
x_train, x_val, y_train, y_val = train_test_split(
    X, y, test_size = 0.3, random_state=1)
x_train.shape 
y_train.shape 


# 3. keras model
model = Sequential() 
print(model) # object info


# 4. DNN model layer 구축 
'''
1층(hidden layer1) : units = 64
2층(hidden layer2) : units = 32
3층(hidden layer3) : units = 16 
4층(output layer) : units=1
'''
model.add(Dense(units=64, input_shape=(13,), activation='relu'))
model.add(Dense(units=32, activation='relu'))
model.add(Dense(units=16, activation='relu'))
model.add(Dense(units=1))

# 5. model compile : 학습과정 설정(다항 분류기)
model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# 6. model training 
'''epochs = 50'''
model.fit(x=x_train, y=y_train, # 훈련셋 
          epochs=50, # 학습횟수 : 50
          verbose=1,  # 출력여부 
          validation_data=(x_val, y_val)) # 검증셋  
'''
12/12 [==============================] - 0s 4ms/step - loss: 0.0051 - mae: 0.0476 - val_loss: 0.0041 - val_mae: 0.0486
'''

# 7. model evaluation : test dataset
model.evaluate(x_val,y_val,verbose=1)
'''
5/5 [==============================] - 0s 997us/step - loss: 0.0041 - mae: 0.0486
'''
# 출력 결과: [0.004099546931684017, 0.048553716391325] = [loss, mae]

# 8. model 평가: mean_squared_error, r2_score 
y_pred = model.predict(x_val)

# 1) mean_squared_error
mse = mean_squared_error(y_val,y_pred)
print('MSE =', mse)
# MSE = 0.004196297746606852

# 2) r2_score
r2 = r2_score(y_val,y_pred)
print('r2_score =', r2)
# r2_score = 0.9072876494585507