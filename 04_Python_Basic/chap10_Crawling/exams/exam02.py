'''
 문2) urls 객체의 url을 대상으로 다음 조건에 맞게 웹 문서의 자료를 수집하시오.
    조건1> http:// 또는 https://으로 시작하는 url만을 대상으로 한다.
    조건2> url에 해당하는 웹 문서를 대상으로 <a> 태그(tag) 내용만 출력한다.
    조건3> <a> 태그 내용이 없는(None) 경우는 출력하지 않는다.

    <출력 결과 예시>
    a tag 내용 :  OTTOGI
    a tag 내용 :  NONGSHIM
       중간 생략
    a tag 내용 :  네이버 정책
    a tag 내용 :  고객센터
    a tag 내용 :  ⓒ NAVER Corp.
'''

from urllib.request import urlopen # 함수 : 원격 서버 url 요청 
from bs4 import BeautifulSoup # 클래스 : html 파싱
import re # 정규표현식

urls = ['https://www.daum.net', 'www.duam.net', 'http://www.naver.com']

# 단계1 : url 정제
ur=[]
for url in urls:
    if re.search('(^http[s]?://)',url):
        ur.append(url)

# 단계2 : url에서 a 태그 내용 수집 & 출력
atag=[]
for url in ur: # 자료 수집
    # url 요청
    gpage=urlopen(url) # url 요청
    pread=gpage.read() # data 읽기
    # 디코딩
    de=pread.decode('utf-8')
    # HTML 파싱
    soup=BeautifulSoup(de,'html.parser')
    # tag 수집
    at=soup.find_all('a')
    # tag 내용 수집
    t=[a.string for a in at if link != None]
    atag.append(t)

for tag in atag:
    print('a tag 내용 :',tag)
    
