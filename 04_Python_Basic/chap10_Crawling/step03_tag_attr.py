'''
tab 속성과 내용 가져오기
'''

from bs4 import BeautifulSoup

path = 'C:\\work\\Crystal\\DataAnalysis\\[ITWILL]BigDataAnalysis_ExpertTraining\\04. Python Basic\\workspace\\chap10_Crawling\\data'

# 1. html source 가져오기 
file = open(path + '/html02.html', mode='r', encoding='utf-8')
src = file.read()

# 2. html 파싱
html = BeautifulSoup(src, 'html.parser')
print(html)

# 3. 태그 속성과 내용 가져오기 
links = html.find_all('a') # list
print(links)
# [<a href="www.naver.com">네이버</a>,...<a href="http://www.duam.net">다음</a>]
print(len(links))

links[2]
# <a href="http://www.naver.com" target="_blank">네이버 새창으로</a>

print(links[0].get('href')) # 위치.get('속성값') = 'www.naver.com'

conts=[] # 내용 저장
urls=[] # url 저장
urls2=[] # url 저장
for link in links:
    # print('tag 내용')
    conts.append(link.string)
    # print('tag 내 href 속성')
    try:
        urls.append(link.get('href')) # 속성1 가져오기 방법1
        urls2.append(link.attrs['href']) # 속성1 가져오기 방법2
        print(link.get('target')) # 속성2 가져오기 -> 만일 속성이 존재하지 않으면 None(결측치) 출력
        print(link.attrs['target']) # 만일 속성이 존재하지 않으면 Error 발생 -> 예외처리 필요
        print(link.attrs) # 모든 속성 정보 딕셔너리 형태로 출력 = {속성명: '속성값'}
    except Exception as e:
        print('예외 발생 :',e)

print(conts) # 5개
print(urls) # 5개
print(urls2)
# ['www.naver.com', 'http://www.naver.com', 'http://www.naver.com', 'www.duam.net', 'http://www.duam.net']

# 정규 표현식으로 정상 url 추출: http://~
import re
urls_re=[]
http_pat=re.compile('^http://') # 패턴 객체
for url in urls:
    tmp=http_pat.search(url)
    if tmp:
        print(url)
        urls_re.append(url)
print(urls_re)
# ['http://www.naver.com', 'http://www.naver.com', 'http://www.duam.net']

# 중복되는 url 하나로 만들기
final_urls=list(set(urls_re))
final_urls
# ['http://www.duam.net', 'http://www.naver.com']