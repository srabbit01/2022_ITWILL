# -*- coding: utf-8 -*-
"""
step03_text_input.py

<작업순서> 
입력상자 -> 검색어 입력 -> [검색 페이지 이동] -> element 수집 
"""

from selenium import webdriver # driver 생성  
from selenium.webdriver.common.keys import Keys # 엔터키 역할 

# 키워드 관련 url 수집 함수 
def keyword_search(keyword) :
    # 1. driver 객체 생성 
    path = r"C:/work/Crystal/DataAnalysis/[ITWILL]BigDataAnalysis_ExpertTraining/06_Python_DL/tools"
    driver = webdriver.Chrome(path + '/chromedriver.exe')
    
    # 2. 대상 url 이동 
    driver.get('https://www.google.com/') # url 이동   
    
    # 3. 검색어 입력상자 : name 속성으로 가져오기 
    # <input id="input" type="search" autocomplete="off" spellcheck="false" role="combobox" placeholder="Google 검색 또는 URL 입력" aria-live="polite">
    input_ele = driver.find_element_by_name('q') # 1개 element 
    
    # 4. 검색어 입력 -> 엔터 
    input_ele.send_keys(keyword) # 검색어 입력
    input_ele.send_keys(Keys.ENTER) # 엔터키 누름 -> 검색 페이지 이동 
    
    # 5. 검색 페이지 element 수집 : tag 이름으로 가져오기 
    a_elems = driver.find_elements_by_tag_name('a') # list 반환    
    # print('---a태그 출력---')
    # print(a_elems) # element 객체 수집 
    print('수집 elements 개수 =', len(a_elems),'\n')
    '''
    <a href='url'> 내용 </a>
    '''
    
    # 6. element 속성 (href) 수집: url 수집
    urls = [] # url 저장
    for a in a_elems:
        url = a.get_attribute('href') # element -> 속성 추출
        urls.append(url) # url 저장
    # print('---url 출력---')
    # print(urls)
    
    # 7. element 내용
    conts = [] # 내용 저장
    for a in a_elems:
        conts.append(a.text) # element -> 내용 수집
    # print('---내용 출력---')
    # print(conts)
    
    driver.close()
    
    return urls, conts

# 함수 호출 
urls, conts = keyword_search('홍길동')

# 결과 출력
print('url 개수 :',len(urls)) # 111
print('내용 개수 :',len(conts)) # 111
