# -*- coding: utf-8 -*-
"""
croped image resize(100x100)
"""

from glob import glob # (*.jpg)
from PIL import Image # image file read
import numpy as np

# 폴더 경로 
path = r'C:/work/Crystal/DataAnalysis/[ITWILL]BigDataAnalysis_ExpertTraining/06_Python_DL/workspace/chap08_Face_detection/lecture01_face_landmark'
fpath = path + "/croped_images" # image path 

# 모든 이미지 규격화 시키기
def imgReshape() :
    img_reshape = [] # image save 
    
    for file in glob(fpath + "/*.jpg") : # jpg file 선택 
        img = Image.open(file) # image read 
        
        # image 규격화 
        img = img.resize( (100, 100) ) # 세로 및 가로 100으로 조정
        # PIL -> numpy
        img_data = np.array(img) # 형변환
        print(img_data.shape)
        
        img_reshape.append(img_data) # list에 넣기
    
    return np.array(img_reshape) # list -> numpy

# 함수 호출         
img_reshape = imgReshape()    

print(img_reshape.shape) 
# resize 이전: (5, 150, 150, 3) - (size, h, w, c)
# resize 이후: (26, 100, 100, 3) -> (size, h, w, c) 
 
size = img_reshape.shape[0] # image size

for i in range(size):
    img = img_reshape[i] # 각 이미지 출력
    
    # image save
    io.imsave(fpath+'/croped'+str(i+101)+'_resize'+'.jpg',img) # croped101_resize.jpg
    
    
    