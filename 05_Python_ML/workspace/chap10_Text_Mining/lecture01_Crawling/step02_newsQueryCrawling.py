'''
url query 이용 뉴스 자료 수집 
   <작업절차> 
  1. http://media.daum.net -> 시작페이지 
  2. https://news.daum.net/newsbox -> 배열이력 클릭  
  3. https://news.daum.net/newsbox?regDate=20220505  -> 특정 날짜 선택
  4. https://news.daum.net/newsbox?regDate=20220505&tab_cate=NE&page=2 -> 특정 페이지

   <구성>: baseurl?변수1=값&변수2=값
   - base url: https://news.daum.net/newsbox
   - 쿼리 변수1: regDate=20220505 -> 조회 날짜
   - 퀴리 변수2: page=2 -> 조회 페이지 번호
   
   결과적으로,
   f"https://news.daum.net/newsbox?regDate={date}&page={page}"
   로 매 날짜 및 페이지 당 내용 확인
   - date: "2021-11-01" ~ "2022-03-31"
   - page: 1 ~ 5
'''

import urllib.request as req  # url 가져오기 
from bs4 import BeautifulSoup # html 파싱
import pandas as pd # 시계열 data 생성

# 1. 수집 기간 날짜 생성  
dates = pd.date_range("2021-11-01", "2022-03-31") # 5개월
print(dates) # "2021-11-01" ~ "2022-03-31"
len(dates) # 151
dates[0] # Timestamp('2021-11-01 00:00:00', freq='D')
type(dates)

# 2021-11-01 -> '20211101' 만들기
import re
kdates=[re.sub('-','',str(date))[:8] for date in dates]
kdates # '20211101' ~ '20220331'

# 총 수집 데이터 수 확인
len(kdates)*200 # 30200개 데이터 수집

# 2. Crawler 함수(페이지, 검색날짜) 
def crawler_func(date, pages=5):  
    day_news = [] # 1일 news 저장(1~5페이지)
    print('수집되는 날짜:',date)
    for page in range(1, pages+1) : # page = 1 ~ 5
        print('수집되는 페이지:',page)
        # 1) url 구성 : url + query 
        url = f"https://news.daum.net/newsbox?regDate={date}&page={page}"
        
        # 2) url 요청 -> html source          
        res = req.urlopen(url)
        data = res.read()
        
        # 3) html 파싱
        src = data.decode('utf-8') # charset='euc-kr'
        html = BeautifulSoup(src, 'html.parser')
        
        # 4) 선택자 기반 a 태그 수집                  
        links = html.select('ul[class="list_arrange"] > li > strong > a[class="link_txt"]') # 1) list tag 수집
            
        page_news = [] # 1 페이지 news 저장

        for a in links :
            news = str(a.text).strip() # 문장 끝 불용어 제거 
            page_news.append(news) # 1 페이지 news 저장 
        
        day_news.extend(page_news) # 1 day news 저장
        # day_news.append: [[40],[40],[40],[40],...]
        # day_news.extend: [[200],...]
    return day_news
    

# 3. 클로러 함수 호출 
crawling_news = [crawler_func(date) for date in kdates]
len(crawling_news) # 151 = [[1day],[2day],...,[151day]] 이때 [1day]=[200]

import numpy as np
crawling_news=np.array(crawling_news)
crawling_news.shape # (151, 200) -> (151일,1일당200개news)
crawling_news[0] # 1일째
crawling_news[-1] # 151일째

# 4. file save 
import pickle # object -> binary file 

path = r'C:\ITWILL\5_Python-II\workspace\chap10_TextMining\data'
file = open(path + '/news_data.pkl', mode='wb')
pickle.dump(crawling_news, file)
file.close()

# file load 
file = open(path + '/news_data.pkl', mode='rb')
news_data = pickle.load(file)
file.close()
print(news_data)
