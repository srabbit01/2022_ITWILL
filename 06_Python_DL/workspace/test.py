# -*- coding: utf-8 -*-
"""
tensorflow import test
"""

import tensorflow as tf

print(tf.__version__) # tensorflow 버전 출력 

mnist = tf.keras.datasets.mnist # dataset 로드 

train, test = mnist.load_data()

X_train, y_train = train
X_train.shape
y_train.shape

X_test, y_test = test
X_test.shape  
y_test.shape 

X_test.min()
X_test.max()



