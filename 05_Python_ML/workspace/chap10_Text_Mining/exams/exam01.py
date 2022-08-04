'''
 문1) 아래 url을 이용하여 어린이날(20210505)에 제공된 뉴스 기사를 
   1~5페이지 크롤링하는 크롤러 함수를 정의하고 크롤링 결과를 확인하시오.    
   
   <조건1> 크롤러 함수 정의
   <조건2> 크롤링 대상  : <a> 태그의 'class=link_txt' 속성을 갖는 내용 
   <조건3> 크롤링 결과 확인  : news 개수와  news 출력  
'''

import urllib.request as req  # url 가져오기 
from bs4 import BeautifulSoup


# 클로러 함수(페이지수, 검색날짜) 
def crawler_func(pages, date):
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
        
        day_news.append(page_news) # 페이지 단위 저장
        # day_news.append: [[40],[40],[40],[40],...]
        # day_news.extend: [[200],...]
    return day_news   

# 클로러 함수 호출 
crawling_news = crawler_func(5, '20220505') # (페이지수, 검색날짜)
print(crawling_news)
len(crawling_news)

print('전체 자료 수 =', len(crawling_news)*40)
# 전체 자료 수 = 200