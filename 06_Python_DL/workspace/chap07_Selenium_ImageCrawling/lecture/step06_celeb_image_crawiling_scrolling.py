# -*- coding: utf-8 -*-
"""
step05_celeb_image_crawling.py

셀럽 이미지 수집 
 Selenium + Driver + BeautifulSoup + 화면 스크롤링
 -> 화면 스크롤링은 많은 자료 수집 시 사용
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys # 엔터키 사용(Keys.ENTER) 
from bs4 import BeautifulSoup
from urllib.request import urlretrieve # server image -> local save
import os # dir 경로/생성/이동
import time # 시간 확인

def celeb_crawler(name) :    
    # 1. dirver 경로 지정 & 객체 생성  
    path=r'C:/work/Crystal/DataAnalysis/[ITWILL]BigDataAnalysis_ExpertTraining/06_Python_DL/tools'
    driver = webdriver.Chrome(path + "/chromedriver.exe")
    
    # 1. 이미지 검색 url 
    driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
    
    # 2. 검색 입력상자 tag -> 검색어 입력   
    search_box = driver.find_element_by_name('q')
    search_box.send_keys(name) # 검색어 입력  
    search_box.send_keys(Keys.ENTER) # 검색창에서 엔터 
    
    driver.implicitly_wait(3) # 3초 대기(자원 loading)
    
    # [추가]
    # ------------ 스크롤바 내림 ------------------------------------------------------ 
    last_height = driver.execute_script("return document.body.scrollHeight") #현재 스크롤 높이 계산
    # .execute_script: 현재 보이는 표면의 높이 계산
    while True: # 무한반복
        # 브라우저 끝까지 스크롤바 내리기
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 
        
        time.sleep(1) # 1초 대기 - 화면 스크롤 확인
    
        # 화면 갱신된 화면의 스크롤 높이 계산
        new_height = driver.execute_script("return document.body.scrollHeight")

        # 새로 계산한 스크롤 높이와 같으면 stop
        if new_height == last_height: 
            try: # [결과 더보기] : 없는 경우 - 예외처리             
                driver.find_element_by_class_name("mye4qd").click() # 버튼 클릭 
            except:
                break # 만일 스크롤링이 되지 않으면 중지
        last_height = new_height # 새로 계산한 스크롤 높이로 대체 
    #-------------------------------------------------------------------------
    
    
    # 3. 이미지 div 태그 수집  
    image_url = []
    for i in range(50) : # image 개수 지정(중복 image 고려) : 35/50                 
        src = driver.page_source # 현재페이지 source 수집 
        html = BeautifulSoup(src, "html.parser")
        div_img = html.select_one(f'div[data-ri="{i}"]') # 이미지 div tag 1개 수집
    
        # 4. img 태그 수집 & image url 추출
        # copy element : <img src="data:image/jpeg;base64, class="rg_i Q4LuWd" jsname="Q4LuWd" width="145" height="218" alt="하정우 (r1464 판) - 나무위키" data-iml="741.1999999992549" data-atf="true">
        img_tag = div_img.select_one('img[class="rg_i Q4LuWd"]')
        try :
            image_url.append(img_tag.attrs['src'])
            print(str(i+1) + '번째 image url 추출')
        except :
            print(str(i+1) + '번째 image url 없음')
      
            
    # 5. 중복 image url 삭제      
    print(len(image_url)) # 43      
    image_url = list(set(image_url)) # 중복 url  삭제 
    print(len(image_url)) # 43
   
    # 6. image 저장 폴더 생성과 이동 
    path=r'C:/work/Crystal/DataAnalysis/[ITWILL]BigDataAnalysis_ExpertTraining/06_Python_DL/workspace/chap07_Selenium_ImageCrawling' 
    os.mkdir(path + '/' + name) # pwd 위치에 폴더 생성(셀럽이름) 
    # os.chdir(path+"/"+name) # 폴더 이동(현재경로/셀럽이름)
        
    # 7. image url -> image save
    for i in range(len(image_url)) :
        try : # 예외처리 : server file 없음 예외처리 
            file_name=path+'/'+name+'/'+name+str(i+1)+'.jpg'
            urlretrieve(image_url[i],filename=file_name) # (url, filepath+filename)
            print(str(i+1)+'번째 image 저장 완료')
        except :
            print('해당 url에 image 없음 : ', image_url[i])        
    
    driver.close() # driver 닫기 
    
    
# 1차 테스트 함수 호출 
# celeb_crawler("하정우")   

# 여러 셀럽 이미지 수집  
namelist = ["강동원", "송강", "김지원", "전지현", "김영대"] 

for name in namelist :
    celeb_crawler(name) # image crawling

    