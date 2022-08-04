'''
- 현재 시각 news Crawling 
  1단계. 아래 url에서 news링크 url 수집
  2단계. 해당 url의 news 수집 (각 제목과 내용)
- url : http://media.daum.net
'''

import urllib.request as req  # url 가져오기 
from bs4 import BeautifulSoup # html 파싱 도구

url = "http://media.daum.net"

# 1. url 요청 
res = req.urlopen(url)
data = res.read() # 한글 깨짐 


# 2. 한글 디코딩 & html 파싱
src = data.decode('utf-8') # charset="utf-8" -> 디코딩 적용 
src # 한글 디코딩 
html = BeautifulSoup(src, 'html.parser') # 한글 디코딩
        

# 3. news 관련 url 수집  
# <ul class="list_newsissue"> <li>

# 1) list tag 수집: select('태그[속성="값"]')
lis = html.select('ul[class="list_newsissue"] > li') # list type
print(lis)
print('list 태그 개수 : ', len(lis)) 

# 2) url 추출 
urls = [] # url 저장 
for li in lis :    
    try :  
        a = li.select_one('a[class="link_txt"]') 
        print(a.attrs['href']) # url 출력 : attrs(속성)
        urls.append(a.attrs['href']) # url 저장
    except Exception as e :
        print('에외발생 :', e) 
 
print(urls) 

         
# 4. crawler 함수 정의
def crawler_fn(url): # 페이지 고정
    print('url :', url)
    try :
        # 1. url 요청 
        res = req.urlopen(url)
        data = res.read()  
        
        # 2. html 파싱
        src = data.decode('utf-8') # charset="utf-8" -> 디코딩 적용
        html = BeautifulSoup(src, 'html.parser')        
        
        # 3. 제목과 내용 수집 
        # 1) 제목 수집  
        title = str(html.select_one('h3[class="tit_view"]').text).strip()
        
        # 2) 내용 수집  
        article = html.select('div[class="news_view"] > div[class="article_view"] > section > p')
        
        # 4. 여러개 문단(p) -> 한 개의 변수로 묶음 
        conts = ""
        for p in article :
            text = str(p.text).strip()
            conts += text # 텍스트 누적
    except Exception as e: # url 없는 경우 
        print('예외 발생 :', e) 
    return title, conts 


# Crawler 함수 호출 
titles = [] # 제목 저장 
news = [] # 내용 저장 

for url in urls :  
    title, conts = crawler_fn(url) # 함수 호출 
    titles.append(title) # 제목 저장 
    news.append(conts) # 내용 저장


# 5. csv file save 
import pandas as pd 

daum_news = pd.DataFrame({'titles':titles, 'news':news}, columns=['titles','news'])

daum_news.info()
daum_news.head()
path=r"C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML\workspace\chap10_TextMining\data"
daum_news.to_csv(path + '/daum_news.csv', index=None)


