# -*- coding: utf-8 -*-
"""
셀레리움 설치 
(base) conda activate tensorflow 
(tensorflow) pip install selenium 
"""
from selenium import webdriver # 드라이버  
import time # 화면 일시 정지

# 1. driver 객체 생성 
path = r"C:/work/Crystal/DataAnalysis/[ITWILL]BigDataAnalysis_ExpertTraining/06_Python_DL/tools" # driver 경로 
driver = webdriver.Chrome(path + '/chromedriver.exe') # driver 객체 생성 

dir(driver)
'''
- get(url): url 이동
- close(): 현재 브라우저 창 닫기
'''

# 2. 대상 url 이동 
driver.get('https://www.naver.com/') # url 이동 

# 3. 일시 중지 & driver 종료 
time.sleep(3) # 3초 일시 중지 
driver.close() # 현재 창 닫기  


















