# -*- coding: utf-8 -*-
"""
step04_movie_review_crawling.py

naver 영화 review 텍스트 수집 
 find_element_by : 1개 element 수집 -> 객체 하나 반환
 find_elements_by : n개 element 수집 -> list 반환
"""

from selenium import webdriver # module 
import time # 화면 일시 정지 

# 1. driver 객체 생성 
path = r"C:/work/Crystal/DataAnalysis/[ITWILL]BigDataAnalysis_ExpertTraining/06_Python_DL/tools"
driver = webdriver.Chrome(path + '/chromedriver.exe')

# 2. 대상 url 이동 
driver.get('https://movie.naver.com/') # naver 영화 검색 url 이동 

# 3. [평점.리뷰] 링크 클릭 : 절대경로 이용 1개 element 가져오기 
# <a href="/movie/point/af/list.naver" title="평점·리뷰" class="menu07"><strong>평점·리뷰</strong></a>
a_ele = driver.find_element_by_xpath('/html/body/div/div[3]/div/div[1]/div/div/ul/li[4]/a')
a_ele.click() # 페이지 이동 

print(driver.current_url) # 현재 페이지 url 출력 

# 4. 영화제목, 평점, 리뷰 수집 : 1page(10개)
title_txt = [] # 영화제목 저장
star_txt = [] # 평점 저장 
review_txt = [] # 영화리뷰 저장

'''
- https://movie.naver.com/movie/point/af/list.naver: base url
- https://movie.naver.com/movie/point/af/list.naver?&page={n}: base_url?page=번호
''' 

for n in range(1, 11) : # 10page 수집  
    url = f"https://movie.naver.com/movie/point/af/list.naver?&page={n}"
    driver.get(url) # page 번호 이동 
    time.sleep(1) # 1초 일시 정지 
    
    # 1) 영화제목 저장 : copy xpath
    titles = driver.find_elements_by_xpath('//*[@id="old_content"]/table/tbody/tr/td[2]/a[1]')
    '''
    # 태그는 1부터 시작
    //*[@id="old_content"]/table/tbody/tr[1]/td[2]/a[1]: 영화1 제목
    //*[@id="old_content"]/table/tbody/tr[2]/td[2]/a[1]: 영화2 제목
    ...
    //*[@id="old_content"]/table/tbody/tr[10]/td[2]/a[1]: 영화10 제목
    '''
    # //*[@id="old_content"]/table/tbody/tr[n]/td[2]/a[1]: n번째 영화 제목
    # //*[@id="old_content"]/table/tbody/tr/td[2]/a[1]: 영화 제목 패턴
    
    for title in titles:
        title_txt.append(title.text)
        
    # print(title_txt)
    
    # 2) 평점 저장  : copy xpath 
    '''
    //*[@id="old_content"]/table/tbody/tr[1]/td[2]/div/em: 영화1 평점
    //*[@id="old_content"]/table/tbody/tr[2]/td[2]/div/em: 영화2 평점
    //*[@id="old_content"]/table/tbody/tr[10]/td[2]/div/em: 영화10 평점
    '''
    # //*[@id="old_content"]/table/tbody/tr[n]/td[2]/div/em: n번째 영화 평점
    # //*[@id="old_content"]/table/tbody/tr/td[2]/div/em: 영화 평점 패턴
    stars = driver.find_elements_by_xpath('//*[@id="old_content"]/table/tbody/tr/td[2]/div/em')
    
    for star in stars :
        star_txt.append(star.text)
    
    # print(star_txt)    
        
    # 3) 리뷰 내용 저장: 단독 내용 수집 불가능
    # 전체 수집 -> 영화 리뷰 내용만 추출
    '''
    //*[@id="old_content"]/table/tbody/tr[1]/td[2]: 영화1
    //*[@id="old_content"]/table/tbody/tr[2]/td[2]: 영화2
    ...
    //*[@id="old_content"]/table/tbody/tr[10]/td[2]: 영화10
    '''
    # //*[@id="old_content"]/table/tbody/tr/td[2]: 전체 영화 패턴
    reviews = driver.find_elements_by_xpath('//*[@id="old_content"]/table/tbody/tr/td[2]')
    for review in reviews:
        # print(review.text)
        '''
        범죄도시2 -> 제목
        별점 - 총 10점 중 -> 별점
        10 -> 별점
        대존잼! 1이랑 똑같이 재밌어요! -> 리뷰 내용
        '''
        token = str(review.text).split('\n')
        review_token = token[3] # 4번째 줄
        review_txt.append(review_token[:-3]) # [:-3]: 마지막 '신고' 제외
    
    print('제목 개수 :', len(title_txt)) # 100
    print('평점 개수 :', len(star_txt)) # 100
    print('리뷰 개수 :', len(review_txt)) # 100
    
driver.close() 

# 결과 출력
'''
print('영화 제목')
print(title_txt)
print('영화 평점')
print(star_txt)
영화 제목
['쥬라기 월드: 도미니언', '쥬라기 월드: 도미니언', '미나리', '쥬라기 월드: 도미니언', '쥬라기 월드: 도미니언', '쥬라기 월드: 도미니언', '범죄도시2', '쥬라기 월드: 도미니언', '카시오페아', '범죄도시2', '쥬라기 월드: 도미니언', '범죄도시2', '26년', '그대가 조국', '범죄도시2', '닥터 스트레인지: 대혼돈의 멀티버스', '쥬라기 공원 3', '이 안에 외계인이 있다', '쥬라기 월드: 도미니언', '특수요원 빼꼼', '쥬라기 월드: 도미니언', '그대가 조국', '그대가 조국', '특수요원 빼꼼', '그대가 조국', '쥬라기 월드: 도미니언', '범죄도시2', '쥬라기 월드: 도미니언', '쥬라기 월드: 도미니언', '그대가 조국', '그대가 조국', '그대가 조국', '그대가 조국', '닥터 스트레인지: 대혼돈의 멀티버스', '쥬라기 월드: 도미니언', '쥬라기 월드: 도미니언', '쥬라기 월드: 도미니언', '범죄도시2', '쥬라기 월드: 도미니언', '닥터 스트레인지: 대혼돈의 멀티버스', '쥬라기 월드: 도미니언', '쥬라기 월드: 도미니언', '올리 마키의 가장 행복한 날', '쥬라기 월드: 도미니언', '그대가 조국', '폴레트의 수상한 베이커리', '공동경비구역 JSA', '범죄도시2', '쥬라기 월드: 도미니언', '메멘토', '그대가 조국', '애프터 양', '쥬라기 월드: 도미니언', '범죄도시2', '쥬라기 월드: 도미니언', '범죄도시2', '그대가 조국', '그대가 조국', '카시오페아', '범죄도시2', '나를 만나는 길', '쥬라기 월드: 도미니언', '특수요원 빼꼼', '쥬라기 월드: 도미니언', '세 얼간이', '늑대아이', '쥬라기 월드: 도미니언', '특수요원 빼꼼', '범죄도시2', '그대가 조국', '그대가 조국', '그대가 조국', '모비우스', '쥬라기 월드: 도미니언', '범죄도시2', '쥬라기 월드: 도미니언', '그대가 조국', '연애 빠진 로맨스', '특수요원 빼꼼', '범죄도시2', '쥬라기 월드: 도미니언', '범죄도시2', '범죄도시2', '닥터 스트레인지: 대혼돈의 멀티버스', '쥬라기 월드: 도미니언', '쥬라기 월드: 도미니언', '쥬라기 월드: 도미니언', '바람', '쥬라기 월드: 도미니언', '쥬라기 월드: 도미니언', '쥬라기 월드: 도미니언', '쥬라기 월드: 도미니언', '쥬라기 월드: 도미니언', '쥬라기 월드: 도미니언', '범죄도시2', '범죄도시2', '쥬라기 월드: 도미니언', '특수요원 빼꼼', '쥬라기 월드: 도미니언', '쥬라기 월드: 도미니언']
영화 평점
['10', '10', '9', '10', '10', '10', '10', '10', '10', '10', '5', '10', '6', '10', '10', '2', '2', '2', '4', '10', '10', '10', '2', '8', '1', '6', '10', '6', '6', '2', '9', '2', '10', '8', '10', '10', '10', '10', '4', '10', '10', '6', '10', '2', '10', '9', '10', '10', '6', '8', '10', '2', '10', '10', '6', '10', '10', '4', '6', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '1', '7', '10', '10', '10', '10', '10', '10', '8', '10', '10', '10', '10', '10', '10', '10', '7', '1', '10', '1', '10', '10', '10', '10', '1', '10', '2', '10']
'''
print('영화 리뷰')
print(review_txt)


# 5. file save

# 1) DataFrame
import pandas as pd
df=pd.DataFrame({'title':title_txt,'star':star_txt,'review':review_txt},
                columns=['title','star','review'])

df.info()
'''
RangeIndex: 100 entries, 0 to 99
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   title   100 non-null    object
 1   star    100 non-null    object
 2   review  100 non-null    object
dtypes: object(3)
'''

# 2) csv file save
path=r'C:/work/Crystal/DataAnalysis/[ITWILL]BigDataAnalysis_ExpertTraining/06_Python_DL/workspace/chap07_Selenium_ImageCrawling'
df.to_csv(path+'/crawling/movie.csv')

