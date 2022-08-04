"""
step01_urlopen.py

< 작업 절차 >
1. url 요청 -> 응답 객체
2. 응답 객체 -> byte data
3. byte data -> 디코딩(해독)=한글 변환
4. 소스(source) -> html로 파싱(변환)
5. 태그(tag) 검색 -> 내용 가져오기(자료수집)
  -> 요소(element): <a href='www.naver.com'> 네이버 </a>

"""

# from 패키지.모듈 import 함수
from urllib.request import urlopen # 함수: 원격서버 url 요청 
# -> html 문서가 아니라 소스를 가져옴
from bs4 import BeautifulSoup # 클래스: html 파싱(parsing) = html 문서로 처리
# -> 소스를 html 문서로 변환

url = "http://www.naver.com/index.html"
 
# 1. 원격 서버 url 요청 
req = urlopen(url)  # url 요청
type(req)
req.geturl()
byte_data = req.read() # data 읽기
type(byte_data)
rd=req.readlines()
type(rd)

# 2. html 파싱 
text_data = byte_data.decode("utf-8") # 디코딩: meta charset="utf-8"
print(text_data)
html = BeautifulSoup(text_data, 'html.parser') # html source 파싱
# BeautifulSoup(데이터, '파싱도구') -> html.parser, lxml 등

# 3. 태그 수집: element 단위 수집
type(html) # bs4.BeautifulSoup

# a tag 1개: string 형태 반환
a=html.find('a') # 조건을 만족하는 태그/속성 최초로 발견된 요소 하나만 수집
# <a href="#newsstand"><span>뉴스스탠드 바로가기</span></a>
print('a 태그 내용 :',a.string) # 내용만 반환
# a 태그 내용 : 뉴스스탠드 바로가기
print('a 태그 내용:',a.text)

# a tag 여러개: list 형태 반환
# 1) element 수집
a2=html.find_all('a') # 전체 a tag -> list 형식로 반환
type(a2) # bs4.element.ResultSet: list 형식으로 반환
a2
len(a2) # 331
a2[0] # <a href="#newsstand"><span>뉴스스탠드 바로가기</span></a>
a2[-1] # 저작권 내용: <a data-clk="nhn" href="https://www.navercorp.com" target="_blank">ⓒ NAVER Corp.</a>
# 2) 내용만 반환
contents = [i.string for i in a2] # 태그/속성 외 내용만 저장
print(contents) # 자료 내용이 없는 태그/속성도 존재
