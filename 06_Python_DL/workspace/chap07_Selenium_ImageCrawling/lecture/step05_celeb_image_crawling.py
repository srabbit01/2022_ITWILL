# -*- coding: utf-8 -*-
"""
step05_celeb_image_crawling.py

셀럽 이미지 수집 
 Selenium + Driver + BeautifulSoup
"""

from selenium import webdriver # 드라이버
from selenium.webdriver.common.keys import Keys # 엔터키 사용(Keys.ENTER) 
from bs4 import BeautifulSoup # 정적 페이지 element 처리
from urllib.request import urlretrieve # image save
import os # 파일경로/폴더생성/폴더이동

def celeb_crawler(name) :    
    # 1. dirver 경로 지정 & 객체 생성  
    path = r"C:/work/Crystal/DataAnalysis/[ITWILL]BigDataAnalysis_ExpertTraining/06_Python_DL/tools"
    driver = webdriver.Chrome(path + "/chromedriver.exe")
    
    # 1. 이미지 검색 url 
    driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
    
    # 2. 검색 입력상자 tag -> 검색어 입력   
    search_box = driver.find_element_by_name('q') # name='q'
    search_box.send_keys(name) # 검색어 입력
    
    # 3. [찾기] 버튼 클릭 ("//tag[@attr='value']/하위element")
    '''
    search_box.find_element_by_xpath("//div[@id='sbtc']/button").send_keys(Keys.ENTER)
    '''
    search_box.send_keys(Keys.ENTER) # 검색창에서 Enter -> 검색 페이지 이동
    driver.implicitly_wait(3) # 3초 대기(자원 loading)

    
    # 4. 이미지 div 태그 수집  
    image_url = []
    for i in range(50) : # image 개수 지정  
        # 정적 페이지 처리               
        src = driver.page_source # 현재페이지 source 수집 
        html = BeautifulSoup(src, "html.parser")
        # {i} = 0 ~ 49
        div_img = html.select_one(f'div[data-ri="{i}"]') # 이미지 div tag 1개 수집
    
        # 5. img 태그 수집 & image url 추출
        img_tag = div_img.select_one('img[class="rg_i Q4LuWd"]')
        try :
            image_url.append(img_tag.attrs['src'])
            print(str(i+1) + '번째 image url 추출')
        except :
            print(str(i+1) + '번째 image url 없음')      
    
            
    # 6. 중복 image url 삭제      
    print(len(image_url))       
    image_url = list(set(image_url)) # 중복 url  삭제 
    print(len(image_url))    
    
    driver.close() # driver 닫기 
    
    # 7. image 저장 폴더 생성 및 이동
    path=r'C:/work/Crystal/DataAnalysis/[ITWILL]BigDataAnalysis_ExpertTraining/06_Python_DL/workspace/chap07_Selenium_ImageCrawling'
    os.mkdir(path+'/'+'lecture')
    # 이미 존재하는 폴더는 중복 생성 불가
    # 지우고 재생성하기
    os.mkdir(path+'/'+celeb_filename) # 폴더 생성
    # os.chdir(path+'/celeb_filename') # 폴더 이동
    
    # 8. image save
    for i in range(len(image_url)):
        try:
            file_name=path+'/'+celeb_filename+'/'+celeb_filename+str(i+1)+'.jpg'
            urlretrieve(image_url[i],filename=file_name) # (url, filepath+filename)
            print(str(i+1)+'번째 image 저장 완료')
        except:
            print(str(i+1)+'번째 image 존재하지 않음')
            pass
            # 보이지 않는 오류로 인해 모든 이미지 추출 불가능
    
# 1차 테스트 함수 호출 
'''
celeb_input=input('수십할 이름을 입력하시오. ') # 블랙핑크 지수
celeb_filename='BlackPink_JiSoo' 
celeb_crawler(celeb_input)  
'''

# 2차 테스트 함수 호출
# 셀럽 명단 작성
name_list=['강동원', '박보검', '전지현']
for name in name_list:
    print(name,'image 저장 시작')
    celeb_filename=name
    celeb_crawler(name)