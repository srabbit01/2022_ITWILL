# -*- coding: utf-8 -*-
"""
real image + CNN basic
1. Convolution layer : image 특징 추출  
  -> Filter : 9x9 
  -> 특징맵 : 5개 
  -> strides = 2x2, padding='SAME'
2. Pooling layer : image 축소 
  -> ksize : 7x7
  -> strides : 4x4
  -> padding='SAME' 
"""

import tensorflow as tf # ver2.x
import numpy as np
import matplotlib.pyplot as plt # image print
from matplotlib.image import imread # image read
# 외부 이미지 출력하는 경우, imread로 이미지 읽기

# 1. image load 
path=r'C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\06_Python_DL'
img = imread(path+"/data/images/parrots.png")
plt.imshow(img)
plt.show()

# 2. RGB 픽셀값 
print(img.shape) # (512, 768, 3) - (h, w, c) = (세로, 가로, 색상 수(컬러))
print(img)

# 정규화
from sklearn.preprocessing import minmax_scale
# img=minmax_scale(img)
# 정규화 2차원 이하만 가능
 
# 3. image reshape : 3d -> 4d 변환
Img = img.reshape(1, 512, 768, 3) # (size, h, w, c)
# c = 3: 컬러기 때문에 3(rgb) 지정


# Filter : 난수로 필터 생성
Filter = tf.Variable(tf.random.normal([9,9,3,5])) #[h, w, c, map_size]
# 가로, 세로가 크기 때문에, 비교적 큰 필터 생성
# map_size도 사용자 임의 지정

# 1. Convolution layer 
conv2d = tf.nn.conv2d(Img, Filter, 
                      strides=[1,2,2,1], padding='SAME')
# Convolution Layer에서도 이미지 축소 가능

# 합성곱 연산 결과 
conv2d.shape # [1, 256, 384, 5]
conv2d_img = np.swapaxes(conv2d, 0, 3)
conv2d_img.shape # (5, 256, 384, 1) -> 특징 5개 생성

fig = plt.figure(figsize = (20, 6))  
for i, img in enumerate(conv2d_img) :
    fig.add_subplot(1, 5, i+1) 
    plt.imshow(img) 
plt.show()


# 2. Pool layer 
pool = tf.nn.max_pool(conv2d, ksize=[1,7,7,1], 
                      strides=[1,4,4,1], padding='SAME')
'''
- ksize: 윈도우 크기 7 x 7
- strides: 칸 이동 정도
- padding='SAME': zero-padding 생성
'''

 
# 폴링 연산 결과 
pool.shape # [1, 64, 96, 5]
pool_img = np.swapaxes(pool, 0, 3)

fig = plt.figure(figsize = (20, 6))    
for i, img in enumerate(pool_img) :
    fig.add_subplot(1,5, i+1)
    plt.imshow(img) 
plt.show()


    