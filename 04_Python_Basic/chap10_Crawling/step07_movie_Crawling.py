# -*- coding: utf-8 -*-
"""
상영중 영화 사이트에서 최신 30개 영화 제목과 줄거리 저장 
"""

# from 패키지.모듈 import 함수 
from urllib.request import urlopen # 함수 : 원격서버 url 요청  
from bs4 import BeautifulSoup # 클래스 : html 파싱 

# 상영중 영화 사이트 
url = 'https://movie.naver.com/movie/running/current.naver'

# 1. 원격 서버 url 요청 
req = urlopen(url)  # ulr 요청 
byte_data = req.read() # data 읽기   
print(byte_data)

# 2. html 파싱 
text_data = byte_data.decode("utf-8") # 디코딩 : charset="utf-8" 
print(text_data)
html = BeautifulSoup(text_data, 'html.parser') # html source 파싱
print(html)


# 3. 상영중 영화 주 정보 30개 element 수집(li 태그 30개 수집) 
movie_list = html.select('div[class="lst_wrap"] > ul[class="lst_detail_t1"] > li', limit=30)
print(movie_list) # <li> 하나의 영화 정보 </li> 30개 수집
len(movie_list) # 30
# <div class="thumb">

# 4. a 태그의 href 속성 수집
urls=[]
for li in movie_list:
    a_tag=li.select_one('div[class="thumb"] > a')
    # url 추출
    urls.append(a_tag.get('href')) # get('속성')
print(urls)
len(urls) # 30
urls[0] # '/movie/bi/mi/basic.naver?code=196362' -> 이상한 url?
# base url: https://movie.naver.com + /movie/bi/mi/basic.naver?code=196362
print('https://movie.naver.com'+urls[0])

urls2=['https://movie.naver.com'+urls[i] for i in range(len(urls))]

url='https://movie.naver.com/movie/bi/mi/basic.naver?code=196362'
# 5. 영화 사이트 이동: 영화 제목과 줄거리 저장
def crawler(url): # 자료 수집 함수
    from urllib.request import urlopen
    print('url :',url)
    # 1. url 요청
    req=urlopen(url) # url 요청
    byte_data=req.read()
    # 2. 디코딩
    text_data=byte_data.decode('utf-8')
    # 3. html 파싱
    soup=BeautifulSoup(text_data,'html.parser')
    # 4. Tag 및 내용 수집
    title=soup.select_one('div[class="mv_info"] > h3[class="h_movie"] > a').string
    summary=soup.select_one('div[class="story_area"] > p').text
    '''
    - string: 텍스트만 있는 경우
    - text: 텍스트와 다른 테그가 있는 경우, 텍스트만 추출
    '''
    # 5. 결과 반환
    return [title,summary] # ['제목','줄거리'] 반환

# 6. 함수 호출
movie_contents=[crawler(url) for url in urls2] # [['제목','줄거리'],['제목','줄거리'],...] 중첩 리스트
movie_contents[0]

# 7. DataFrame -> csv file 저장
import pandas as pd # DataFrame

print(movie_contents)
movie_df=pd.DataFrame(movie_contents,columns=['title','summary'])
movie_df.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 30 entries, 0 to 29
Data columns (total 2 columns):
 #   Column   Non-Null Count  Dtype 
---  ------   --------------  ----- 
 0   title    30 non-null     object
 1   summary  30 non-null     object
dtypes: object(2)
memory usage: 608.0+ bytes
'''
print(movie_df) # csv file or table

# csv 파일 저장
path = 'C:\\work\\Crystal\\DataAnalysis\\[ITWILL]BigDataAnalysis_ExpertTraining\\04. Python Basic\\workspace\\chap10_Crawling\\data'
moive_load=movie_df.to_csv(path+'/movie_df_20220422.csv',index=None)

# csv 파일 읽기
move_df_load = pd.read_csv(path + '/movie_df_20220422.csv',header=True)
move_df_load
