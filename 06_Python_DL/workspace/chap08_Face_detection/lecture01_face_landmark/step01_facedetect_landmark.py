# -*- coding: utf-8 -*-
"""
image 얼굴인식과 68 point landmark 인식 

패키지와  68 point 랜드마크 data

단계1 : 패키지 설치 
(base) > conda activate tensorfow

(1) cmake 설치 : dlib 의존성 패키지 설치 
(tensorflow) >pip install cmake

(2) dlib 설치 : 68 랜드마크 인식(얼굴인식)
(tensorflow) >pip install 파일경로/dlib
   
(3) scikit-image 설치 : image read/save
(tensorflow) >pip install scikit-image

단계2 : 68 point 랜드마크 data 다운로드 
(1) 다운로드 :http://dlib.net/files
    shape_predictor_68_face_landmarks.dat.bz2
(2) C:\6_Tensorflow\tools 압축풀기 
"""

import dlib # face detection/face landmark detection
from skimage import io # image read/save
from glob import glob # dir 패턴검색(*jpg)

# 1차 : 폴더 이동 
path = r'C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\06_Python_DL\workspace\chap08_Face_detection\lecture01_face_landmark'
image_path = path + '/images' # celeb image 위치 
croped_path = path + "/croped_images" # croped image 저장 위치


# 2차 : hog 얼굴 인식기(알고리즘)
face_detector = dlib.get_frontal_face_detector()


# 3차 : 얼굴 68개 landmark 객체 생성
# 학습된 데이터
landmark_path = 'C:/work/Crystal/DataAnalysis/[ITWILL]BigDataAnalysis_ExpertTraining/06_Python_DL/tools'
face_68_landmark = dlib.shape_predictor(landmark_path+'/shape_predictor_68_face_landmarks.dat')

image_path = r'C:\work\images'

i=100
for file in glob(image_path+'/*.jpg') : # 폴더에서 순서대로 jpg 파일 읽기 
    print('file=', file)
    image = io.imread(file) # image file 읽기 
    print(image.shape) # image 모양 

    # 1차 : 윈도에 image 표시 (창에다가 읽어온 이미지 띄우기)
    win = dlib.image_window() # 이미지 윈도 
    win.set_image(image) # 1차 : 윈도에 원본 이미지 표시 
    
    # 2차 : image에서 얼굴인식     
    faces = face_detector(image, 1) # 두번째 인수=1 : 업샘플링 횟수 
    print('인식한 face size =', len(faces))
    
    # 3차: 여러 이미지가 존재하는 경우, 인식된 얼굴 이미지 분리
    for face in faces:
        i+=1
        print(face) # 얼굴 사각점 위치(좌표)
        # [(133, 162) (169, 198)] = [(왼쪽상단,오른쪽하단) (왼쪽하단,오른쪽상단)]
        # [(L,T) (R,B)]
        
        # 1) 윈도에 인식된 얼굴 표시 
        win.add_overlay(face) # 원본 이미지 위에 얼굴만 인식한 사각점 face 겹치기
        
        # 2) 사각점 안에서 68개 point 겹치기
        face_landmark = face_68_landmark(image, face)
        win.add_overlay(face_landmark)
        
        # 3) 크롭(Crop): 얼굴 부분만 자르기: image[h, w]
        crop = image[face.top():face.bottom(),face.left():face.right()]
        # 세로: top -> bottom, 가로: left -> right
        
        # 4) image save: 크롭된 이미지 저장
        io.imsave(croped_path + '/croped'+str(i)+'.jpg',crop)



