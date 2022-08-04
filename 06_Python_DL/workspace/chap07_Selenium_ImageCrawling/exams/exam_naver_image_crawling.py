# -*- coding: utf-8 -*-
"""
문) 네이버 url(https://naver.com)을 대상으로 검색 입력 상자에 임의의 '동물' 이름을
    입력하여 이미지 10장을 '동물' 이름의 폴더에 저장하시오.  
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys # 엔터키 
from urllib.request import urlretrieve # image save
import os # 폴더 생성 및 이동 
import time

def naver_img_crawler(search_name) :
    # 1. driver 객체 생성 
    path = r"C:/work/Crystal/DataAnalysis/[ITWILL]BigDataAnalysis_ExpertTraining/06_Python_DL/tools" # driver 경로
    driver = webdriver.Chrome(path + "/chromedriver.exe")
    
    # 2. 대상 url 
    driver.get("https://naver.com") # naver 영화 검색 url 이동 
    
    # 3. name 속성으로 element 가져오기 
    query_input = driver.find_element_by_name("query") # 입력상자  
    query_input.send_keys(search_name)
    query_input.send_keys(Keys.ENTER)
    driver.implicitly_wait(1)
    
    # 4. image 페이지로 들어가기
    image = driver.find_element_by_link_text('이미지') 
    image.click()
    time.sleep(3) # 3초 대기
    # = driver.implicitly_wait(3)
    
    # 5. 이미지 url 저장
    # 1) 방법 1
    '''
    from bs4 import BeautifulSoup
    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')
    imgs = soup.select('img[class="_image _listImage"]')
    img_url = []
    for img in imgs:
        if len(img_url) < 10:
            try:
                img_url.append(img.attrs['src'])
                print('이미지 주소 추출 완료')
            except:
                print("이미지 주소 추출 실패")
    '''
    # 2) 방법 2
    '''
    이미지 상대경로
    //*[@id="main_pack"]/section[2]/div/div[1]/div[1]/div[1]/div/div[1]/a/img # 1번 이미지
    //*[@id="main_pack"]/section[2]/div/div[1]/div[1]/div[2]/div/div[1]/a/img # 2번 이미지
    ...
    //*[@id="main_pack"]/section[2]/div/div[1]/div[1]/div/div/div[1]/a/img # 전체 이미지
    '''
    img_url = []
    for i in range(1,11):
        img = driver.find_element_by_xpath(f'//*[@id="main_pack"]/section[2]/div/div[1]/div[1]/div[{i}]/div/div[1]/a/img')
        img_url.append(img.get_attribute('src'))
        print(f'{i}번째 이미지 주소 추출 완료')
    print('수집된 이미지 개수 :',len(img_url))
    
    driver.close()
    
    # 6. 이미지 폴더 생성 및 이미지 저장
    # 이미지 폴더 생성
    path=r'C:/work/Crystal/DataAnalysis/[ITWILL]BigDataAnalysis_ExpertTraining/06_Python_DL/workspace/chap07_Selenium_ImageCrawling'
    path=path+"/"+name
    try:
        os.mkdir(path)
        # os.chdir(path)
    except:
        pass
    # 이미지 저장
    for i in range(len(img_url)):
        try: # 예외처리 : server file 없음 예외처리 
            file_name=path+'/'+name+str(i+1)+'.jpg'
            urlretrieve(img_url[i],filename=file_name) # (url, filepath+filename)
            print(str(i+1)+'번째 image 저장 완료')
        except :
            print('해당 url에 image 없음')  


# 함수 호출 
name = input('검색어 입력 : ')
naver_img_crawler(name) # 호랑이
