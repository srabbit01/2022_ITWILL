# -*- coding: utf-8 -*-
"""
step05_image_reshape.py

1. image shape & reshape 
2. image file read & show
3. image resize 

reshape vs resize
- 공통점: 모양 변경
- 차이점:
    - reshape: 크기(size) 변경 불가
    - resize: 크기(size) 변경 가능
    
- 전처리(resize) -> 이미지 학습 -> 새로운 이미지가 무엇인지 예측
- 모든 이미지의 픽셀 사이즈(size)가 모두 다름 -> 모두 동일한 사이즈로 맞춰야 함
"""
import numpy as np 
import matplotlib.pyplot as plt # image show
from sklearn.datasets import load_digits # dataset load
# 여러 실습용 데이터셋 제공: iris 등 -> 함수 형식으로 제공 가능
# sklearn 머신러닝에 필요한 도구 제공

# 1. image shape & reshape

# 1) dataset load 
digits = load_digits() # 머신러닝 모델에서 사용되는 데이터셋 
'''
입력변수(X) : 숫자(0~9) 필기체의 흑백 이미지 = 문제 (이미지 자료)
출력변수(y) : 10진 정수(0~9) = 정답 (이미지에 대한 정답)
'''
X = digits.data # 입력변수(X) 추출 
y = digits.target # 출력변수(y) 추출 

type(X) # numpy.ndarray
type(y) # numpy.ndarray

X.shape # (1797, 67)=(행,열)=(size,pixel) # 64 = 1차원픽셀
# 행: 그림 개수, 열: 크기
X[0] # 기본: 행(index) 출력
X[0].max # 15.0 -> 픽셀 값 최대
X[0].min # 0
# 픽셀 값 범위: 0 ~ 15
# 픽셀: 클 수록 black, 작을 수록 white -> 흑백 이미지 변경하는 grace k

X[1].min()
X[1].max() # 16

# 2) image reshape 
# 1차원 픽셀 -> 2원 픽셀로 만들어야 함
first_img = X[0].reshape(8,8) # 모양변경 (1d -> 2d)
first_img.shape # (8, 8) = (세로픽셀,가로픽셀) = 정사각형 변경
first_img2 = X[1].reshape(8,8) 

# 3) image show 
plt.imshow(X=first_img, cmap='gray') # grace k = 흰색, 검정색, 회색으로 이미지 형성하기
# 밝은색 = 검정색, 어두운색 = 흰색으로 바꿔서 변경
# 이미지 그리기: imshow(X=데이터셋,cmap='gray')
plt.show()

y[0] # 0

plt.imshow(X=first_img2, cmap='gray')
# 0: 검은 색 ~ 16: 흰색 
y[1] # 1

# 전체 image reshape
X_3d=X.reshape(1797,8,8) # 픽셀의 모양 변환
X_3d=X.reshape(-1,8,8) # 위와 동일
# 2차원 모양을 3차원으로 변경한 것
X_3d.shape # (1797,8,8)
# -1 = 전체 size 의미

# 마지막 image
plt.imshow(X=X_3d[-1],cmap='gray')
plt.show()
y[-1] # 8 -> 출력 데이터 (지도 학습에서의 정답)

# (1797,8,8) = (1797,8,8,1) = 흑백 이미지
# (1797,8,8,3) = 컬러 이미지

# 2. image file read & show -> 실제 이미지 가져오기
import matplotlib.image as img # 이미지 읽기 

# image file path 
path = r'C:/work/Crystal/DataAnalysis/[ITWILL]BigDataAnalysis_ExpertTraining/05. Python ML/workspace/chap03_Numpy/images' # 경로 지정

# 1) image 읽기 
img_arr = img.imread(path + "/test1.jpg")
type(img_arr) # numpy.ndarray -> numpy 수치로 변환하여 반환
img_arr.shape # (360,540,3) # (h,w,color) -> 3원색에 의해 이미지 생성

# 2) image 출력 
plt.imshow(img_arr)
plt.show()

# img_arr.reshape(120,150,3) # 모양 변경 -> resize 제공 X

# 3. image resize
from PIL import Image # PIL(Python Image Lib) -> 이미지 사이즈 변경
# PIL: Python Image Library
# 이미지 파일 열 것임 의미
# open(), resize() 등 제공

# 1) image read 
img = Image.open(path+'/test1.jpg')
type(img) # PIL.JpegImagePlugin.JpegImageFile
# PIL 객체를 생성하여 이미지 reshape

np.shape(img) # (183, 275, 3) - (세로, 가로, 색상)

# 2) image resize 
img_re = img.resize( (150, 120) ) # (가로, 세로)
np.shape(img_re) # (120, 150, 3)
plt.imshow(img_re)
plt.show()
# 픽셀 수가 많을 수록 화질의 선명도 증가


# 4. 특정 폴더 내 전체 이미지 크기 규격화
from glob import glob
# 파일의 검색 패턴 사용 (경로, ?, * 이용 가능) -> 파일을 패턴화하여 지정 가능

img_size=[] # image 저장하는 리스트
img_w=150 # 가로픽셀
img_h=120 # 세로 픽셀

path = r'C:/work/Crystal/DataAnalysis/[ITWILL]BigDataAnalysis_ExpertTraining/05_Python ML/workspace/chap03_Numpy' # 경로 지정

# path + file이름.jpg
for file in glob(path+'/images/*.jpg'): # jpg 내 모든 파일을 읽을 것 임을 의미
    # 1단계: image 읽기 -> object    
    img = Image.open(file) # 첫번째 파일 읽어오기
    # 2단계: image resize
    img_re=img.resize((img_w,img_h)) # (가로,세로)
    # 3단계: PIL -> numpy -> list save
    img_size.append(np.array(img_re))

# list -> numpy
img_arr=np.array(img_size)
img_arr.shape # (2,120,150,3) - (size,h,w,c)

for i in range(img_arr.shape[0]):
    plt.imshow(img_arr[i])
    plt.show()
