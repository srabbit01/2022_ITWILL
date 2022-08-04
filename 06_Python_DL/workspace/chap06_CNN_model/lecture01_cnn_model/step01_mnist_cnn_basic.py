# -*- coding: utf-8 -*-
"""
MNIST + CNN basic
 Convolution layer : 이미지 특징 추출
 Pooling layer : 이미지 픽셀 축소
"""
import tensorflow as tf # ver2.x
from tensorflow.keras.datasets.mnist import load_data # ver2.0 dataset
import numpy as np
import matplotlib.pyplot as plt

# 1. image read  
(x_train, y_train), (x_test, y_test) = load_data()
print(x_train.shape) # (60000, 28, 28)
print(y_train.shape) # (60000,) : 10진수 


# 2. 실수형 변환 : int -> float
x_train = x_train.astype('float32') # type 일치 
x_test = x_test.astype('float32')


# 3. 정규화 
x_train /= 255 # x_train = x_train / 255
x_test /= 255
print(x_train[0])
# 실수형인지, 정규화되었는지 확인


# first image : 첫번째 이미지 출력
img = x_train[0]
plt.imshow(img, cmap='gray') # 숫자 5 형상화
# cmap='gray': 흑백 이미지 시각화
plt.show() 
img.shape # (28, 28)


# input image reshape : 2d -> 4d
# [image size, h, w, color] = [이미지 n장, 세로, 가로, 색상]
# color = 1(흑백)/3(컬러)
firstImg = img.reshape(1,28,28,1) # [size, h, w, color]

# Filter(W) 정의 
Filter = tf.Variable(tf.random.normal([3,3,1,5])) # 난수 
# [row(h), column(w), color, feature size] = [행, 열, 색상, 특징 m개]
 
# 1. Convolution layer : First Img @ Filter
conv2d = tf.nn.conv2d(firstImg, Filter, strides=[1,1,1,1], padding='SAME')
conv2d.shape # TensorShape([1, 28, 28, 5]) -> [image size, h, w, color]
# 이미지 축소 X
'''
- FirstImg: Input Image
- Filter: Input Image 대상, 특징 추출하는 필터
- strides=[1,1,1,1]: 필터 이동 정도 (1칸씩 필터 이동) -> 이미지 1개기 때문에 1 입력
- padding='SAME': Input Image와 크기가 동일한 Image 출력
  -> 'SAME'이면 zero padding 생성
# 단, 우선순위: strides > padding
'''


# 합성곱 연산 결과  : Input image에서 5장의 특징 Image 추출
print(conv2d.shape) # (1, 28, 28, 5) = (이미지수, 세로, 가로, 특징수) = input image와 동일
conv2d_img = np.swapaxes(conv2d, 0, 3) # 4차원 축 1과 4 위치 교환 
# np.swapaxes(conv2d,0,3): 축 교환 -> (5, 28, 28, 1)

for i, img in enumerate(conv2d_img) : 
    plt.subplot(1, 5, i+1) # 1행5열 이미지 생성, 1~5 각 위치 지정 
    plt.imshow(img, cmap='gray')  # 각 이미지 한 줄 출력
plt.show()
# enumerate(변수): (index, pixcel) 변환
# 각 특징 Image 출력 (각 특징이 다르게 보임)


# 2. Pool layer 
pool = tf.nn.max_pool(conv2d, ksize=[1,2,2,1], strides=[1,2,2,1], padding='SAME')
'''
- conv2d: 합성곱층에 의해 생성된 이미지 특징 맵
- ksize=[1,2,2,1]: window size (윈도우 크기)
- strides=[1,2,2,1]: down sampling(2배 감소)
- padding='SAME': 동일 출력 여부 (대개, zero-padding 생성 여부와 비슷)
'''
# 픽셀의 수를 2배 감소 -> 해상도 감소하나, 특징 부각 증가

# 폴링 연산 결과 
print(pool.shape) # (1, 14, 14, 5)
pool_img = np.swapaxes(pool, 0, 3) 

for i, img in enumerate(pool_img) :
    plt.subplot(1,5, i+1)
    plt.imshow(img, cmap='gray') 
plt.show()













