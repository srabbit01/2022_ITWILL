# -*- coding: utf-8 -*-
"""
step02_button_click.py

1. naver page 이동 
2. login 버튼 클릭 
"""
from selenium import webdriver # driver  
import time # 화면 일시 정지 

# 1. driver 객체 생성 
path = r'C:/work/Crystal/DataAnalysis/[ITWILL]BigDataAnalysis_ExpertTraining/06_Python_DL/tools'
driver = webdriver.Chrome(path + '/chromedriver.exe')

dir(driver)
'''
- find_element: 1개의 element(tag) 수집
  - find_element_by_class_name
  - find_element_by_css_selector: #old_content > table > tbody > tr:nth-child(3) > td.title
  - find_element_by_id
  - find_element_by_link_text
  - find_element_by_xpath
- find_elements: 2개 이상의 element(tag) 수집
- get: 특정 url로 이동
- back: 뒤로 가기 (현재 -> 이전으로)
- forward: 앞으로 가기 (이전 -> 앞으로)
- refresh: 새로고침(F5) = 화면 갱신

# element 구성: <시작tag 속성="값" 속성="값">내용</종료tag>
'''

# 2. 대상 url 이동 
driver.get('https://www.naver.com/') # url 이동 

# 3. 로그인 버튼 element 가져오기 

# 1) class name으로 가져오기 
'''
login_ele = driver.find_element_by_class_name("link_login")
login_ele.click() # 버튼 클릭 
time.sleep(2) # 2초 일시 중지 
'''

# 2) xpath로 가져오기: Copy > Copy_XPath(상대) or Copy_Full_XPath(절대)
# //*[@id="account"]/a = //*[@속성="값"]/현재(하위)태그 (*: 전체 태그)
login_ele = diver.find_element_by_xpath('//*[@id="account"]/a')
login_ele.click() # 버튼 클릭 

# /html/body/div[2]/div[3]/div[3]/div/div[2]/a
login_ele = diver.find_element_by_xpath('/html/body/div[2]/div[3]/div[3]/div/div[2]/a')
login_ele.click() # 버튼 클릭 

'''
- 상대경로: '상위태그/현재태그'
  - 예시: //*[@id="account"]/a
- 절대경로: 시작 태그(/)부터 현재태그까지 경로 = '전체태그/.../현재태그'
  - 내용 파악이 쉽지 않으나, 상대태그 사용이 어려운 경우 사용
  - 예시: /html/body/div[2]/div[3]/div[3]/div/div[2]/a
'''
time.sleep(2) # 2초 일시 중지 

driver.back() # 현재페이지 -> 이전으로
time.sleep(2) # 2초 일시 중지 
  
driver.forward() # 이전 -> 앞으로 
driver.refresh() # 페이지 새로고침(F5)
time.sleep(2) # 2초 일시 중지 

driver.close() # 현재 창 닫기  


















