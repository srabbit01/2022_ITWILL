"""
step05_newsCrawling.py

<작업 절차>
1. news Crawling
    url='http://media.daum.net/newsbox'
2. pickle file save
    news 자료: 이진 파일 저장
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup

## 1. news Crawling

url='http://media.daum.net/newsbox'

# 1. 원격 서버 url 요청
req=urlopen(url) # url 요청
byte_data=req.read() # data 읽기

# 2. html 파싱
text_data=byte_data.decode('utf-8') # 디코딩: charset='utf-8'
soup=BeautifulSoup(text_data,'html.parser') # html source 파싱
print(soup)

# 3. tag 찾기 -> 내용 수정
# 형식) soup.select('태그[속성="값"])'

# 1) element 수집
links=soup.select('a[class="link_txt"]') # list
# soup.select('a.link_txt')
len(links) # 32
print(links)
len(soup.find_all('a','link_txt')) # 45
len(soup.select('a.link_txt')) # 45
'''
1) soup.select('a[class="link_txt"]'): 32개 -> 속성 하나만 찾음
-> 예: <a class= "link_txt">인 것만 추출
2) soup.select('a.link_txt'): 45개
-> 예: <a class= "link_txt link_news"> 등 2개 이상 클래스 이름이 존재할 떄도 있음
'''

# 2) 내용 수집
news_data=[]
for l in links:
    tmp=l.string
    tmp=str(tmp).strip() # 문장 끝 불용어(띄어쓰기 혹은 줄바꿈)
    if tmp != None: # = not None
        news_data.append(tmp)
print(news_data)

len(news_data) # 32
'''
link=soup.select_one('a[class="link_txt"]')
link=link.string
link.strip()
= str(link).strip()
'''

## 2. pickle file save
import pickle

# 1) file save
# file 저장 경로
path = 'C:\\work\\Crystal\\DataAnalysis\\[ITWILL]BigDataAnalysis_ExpertTraining\\04. Python Basic\\workspace\\chap10_Crawling\\data'
file=open(path+'/news_data.pkl',mode='wb')
# 파일 저장
pickle.dump(news_data,file)
file.close()

# 2) file load
file=open(path+'/news_data.pkl',mode='rb')
news_data_load=pickle.load(file)
print(news_data_load)
news_data_load[0]
