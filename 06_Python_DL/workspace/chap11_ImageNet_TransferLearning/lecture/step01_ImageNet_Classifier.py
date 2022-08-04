# -*- coding: utf-8 -*-
"""
step01_ImageNet_Classifier.py

딥러닝 이미지넷 분류기 
 - ImageNet으로 학습된 이미지 분류기
"""

# 1. VGGNet(VGG16/VGG19) model 
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.applications.vgg19 import VGG19 

# 1) model load 
vgg16_model = VGG16(weights='imagenet') 
vgg19_model = VGG19(weights='imagenet') 
# weights: 이미 학습된 가중치 지정

# 2) model layer 
vgg19_model.summary()
vgg16_model.summary()
'''
Model: "vgg16"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
input_1 (InputLayer)         [(None, 224, 224, 3)]     0         
_________________________________________________________________
block1_conv1 (Conv2D)        (None, 224, 224, 64)      1792      
_________________________________________________________________
block1_conv2 (Conv2D)        (None, 224, 224, 64)      36928     
_________________________________________________________________
block1_pool (MaxPooling2D)   (None, 112, 112, 64)      0         
_________________________________________________________________
block2_conv1 (Conv2D)        (None, 112, 112, 128)     73856     
_________________________________________________________________
block2_conv2 (Conv2D)        (None, 112, 112, 128)     147584    
_________________________________________________________________
block2_pool (MaxPooling2D)   (None, 56, 56, 128)       0         
_________________________________________________________________
block3_conv1 (Conv2D)        (None, 56, 56, 256)       295168    
_________________________________________________________________
block3_conv2 (Conv2D)        (None, 56, 56, 256)       590080    
_________________________________________________________________
block3_conv3 (Conv2D)        (None, 56, 56, 256)       590080    
_________________________________________________________________
block3_pool (MaxPooling2D)   (None, 28, 28, 256)       0         
_________________________________________________________________
block4_conv1 (Conv2D)        (None, 28, 28, 512)       1180160   
_________________________________________________________________
block4_conv2 (Conv2D)        (None, 28, 28, 512)       2359808   
_________________________________________________________________
block4_conv3 (Conv2D)        (None, 28, 28, 512)       2359808   
_________________________________________________________________
block4_pool (MaxPooling2D)   (None, 14, 14, 512)       0         
_________________________________________________________________
block5_conv1 (Conv2D)        (None, 14, 14, 512)       2359808   
_________________________________________________________________
block5_conv2 (Conv2D)        (None, 14, 14, 512)       2359808   
_________________________________________________________________
block5_conv3 (Conv2D)        (None, 14, 14, 512)       2359808   
_________________________________________________________________
block5_pool (MaxPooling2D)   (None, 7, 7, 512)         0         
_________________________________________________________________
flatten (Flatten)            (None, 25088)             0          -> 평탄화
_________________________________________________________________
fc1 (Dense)                  (None, 4096)              102764544 
_________________________________________________________________
fc2 (Dense)                  (None, 4096)              16781312  
_________________________________________________________________
predictions (Dense)          (None, 1000)              4097000   
=================================================================
Total params: 138,357,544
Trainable params: 138,357,544
Non-trainable params: 0
_________________________________________________________________
'''


# 3) model test : 실제 image 적용 
from tensorflow.keras.preprocessing import image # image read 
from tensorflow.keras.applications.vgg16 import preprocess_input, decode_predictions
'''
- preprocess_input: 전처리 도구
- decode_predictions: 예측치 반환
'''

# 우산 이미지 로드 
path = 'C:/work/Crystal/DataAnalysis/[ITWILL]BigDataAnalysis_ExpertTraining/06_Python_DL/data/images'
img = image.load_img(path + '/volcano.jpg', target_size=(224, 224))
'''
target_size=(224, 224):vgg16 또는 vgg19 input_shape이 (224, 224)로
정해져 있기 때문에 일정하게 맞추기
'''
type(img)

X = image.img_to_array(img) # image 데이터 생성 
X = X.reshape(1, 224, 224, 3) # 모양 변경 

# image 전처리 : vgg 사용하기 위해 전처리
X = preprocess_input(X)

# image 예측치 
# 1) vgg16
pred_vgg16 = vgg16_model.predict(X) # 이미치 X를 입력으로 하여 결과 예측
pred_vgg16.shape # (1, 1000) = 1,000개의 범주 중 하나 예측함을 의미

print('predicted :', decode_predictions(pred_vgg16, top=3))
# top=3: 가장 유사한 3개 순서대로 출력
'''
1) umberalla
predicted : [[('n04507155', 'umbrella', 0.9776497), 
              ('n03944341', 'pinwheel', 0.021190464), 
              ('n03888257', 'parachute', 0.0008389075)]]
2) volcano
predicted : [[('n03788365', 'mosquito_net', 0.14106381), 
              ('n04209239', 'shower_curtain', 0.026998967), 
              ('n15075141', 'toilet_tissue', 0.020353168)]]
'''
# 학습되지 않은 이미지의 경우, 정확한 분류 불가능

# 2) vgg19
pred_vgg19 = vgg19_model.predict(X)
pred_vgg19.shape # (1, 1000)
print('predicted :', decode_predictions(pred_vgg19, top=3))
'''
1) umbrella
predicted : [[('n04507155', 'umbrella', 0.9505589), 
              ('n03944341', 'pinwheel', 0.03373873), 
              ('n03888257', 'parachute', 0.011896612)]]
2) volcano
predicted : [[('n03788365', 'mosquito_net', 0.15037344), 
              ('n04209239', 'shower_curtain', 0.030134376), 
              ('n15075141', 'toilet_tissue', 0.01644279)]]
'''

# 2. ResNet50 model 
from tensorflow.keras.applications.resnet50 import ResNet50 
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions


# 1) model load 
resnet50_model = ResNet50(weights='imagenet') 

# 2) model layer 
resnet50_model.summary()


# 이미지 로드 
path = 'C:/work/Crystal/DataAnalysis/[ITWILL]BigDataAnalysis_ExpertTraining/06_Python_DL/data/images'
img = image.load_img(path + '/Tank.jpeg', target_size=(224, 224))

X = image.img_to_array(img) # image 데이터 생성 
X = X.reshape(1, 224, 224, 3)

# image 전처리 
X = preprocess_input(X)

# image 예측치 
pred = resnet50_model.predict(X)
pred.shape # (1, 1000)


print('predicted :', decode_predictions(pred, top=3))
'''
predicted : [[('n01930112', 'nematode', 0.10286027), 
              ('n03804744', 'nail', 0.04231833), 
              ('n04153751', 'screw', 0.040280912)]]
'''


# 3. Inception_v3 model
from tensorflow.keras.applications.inception_v3 import InceptionV3 
from tensorflow.keras.applications.inception_v3 import preprocess_input, decode_predictions


# 1) model load 
inception_v3_model = InceptionV3(weights='imagenet') 

# 2) model layer 
inception_v3_model.summary()

# input layer
inception_v3_model.layers[0].output # 1층 정보 출력


# 이미지 로드 
path = 'C:/work/Crystal/DataAnalysis/[ITWILL]BigDataAnalysis_ExpertTraining/06_Python_DL/data/images'
img = image.load_img(path + '/Tank.jpeg', target_size=(299, 299))

X = image.img_to_array(img) # image 데이터 생성 
X = X.reshape(1, 299, 299, 3)

# image 전처리 
X = preprocess_input(X)

# image 예측치 
pred = inception_v3_model.predict(X)
pred.shape # (1, 1000)


print('predicted :', decode_predictions(pred, top=3))
'''
predicted : [[('n04389033', 'tank', 0.8859344), 
              ('n02950826', 'cannon', 0.002795746), 
              ('n04008634', 'projectile', 0.0014633609)]]
'''














