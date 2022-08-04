'''
문2) 다음과 같이 Convolution layer와 Max Pooling layer를 정의하고, 실행하시오.
  <조건1> input image : volcano.jpg 파일 대상    
  <조건2> Convolution layer 정의 
    -> Filter : 6x6
    -> featuremap : 16개
    -> strides= 1x1, padding='SAME'  
  <조건3> Max Pooling layer 정의 
    -> ksize= 3x3, strides= 2x2, padding='SAME' 
'''

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread

# 화산 이미지
path=r'C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\06_Python_DL'
img = imread(path+'/data/images/volcano.jpg') # 이미지 읽어오기
plt.imshow(img)
plt.show()
print(img.shape) # (405, 720, 3)

# 모양 재생성
img = img.reshape(1,405, 720, 3)

# 1. Convolution Layer
# 필터 생성
Filter = tf.Variable(tf.random.normal([9,9,3,6]))
# convolution
conv2d = tf.nn.conv2d(img, Filter, strides=[1,1,1,1], padding='SAME')
print(conv2d.shape) # (1, 405, 720, 6)
# 시각화
conv2d_img = np.swapaxes(conv2d, 0, 3)
for i, img in enumerate(conv2d_img) :
    plt.subplot(1, 6, i+1)
    plt.imshow(img)
plt.show()


# 2. Pooling
pool = tf.nn.max_pool(conv2d, ksize=[1,2,2,1], strides=[1,2,2,1], padding='SAME')
print(pool.shape) # (1, 203, 360, 6)
pool_img = np.swapaxes(pool, 0, 3) 
for i, img in enumerate(pool_img) :
    plt.subplot(1,6, i+1)
    plt.imshow(img) 
plt.show()

