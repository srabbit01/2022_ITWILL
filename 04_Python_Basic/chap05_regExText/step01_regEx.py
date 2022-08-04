# -*- coding: utf-8 -*-
"""
chap05_regExText > step01_regEx.py

정규 표현식(Regular Expressions)  
 - 특정한 규칙을 가진 메타문자를 이용하여 패턴을 지정한 문자열 표현 

[주요 메타문자]
.x : 임의의 한 문자 뒤에 x가 오는 문자열(예 : abc, mbc -> .bc) 
x. : x 다음에 임의의 한 문자가 오는 문자열(예 : t1, t2, ta -> t.) 
^x : x로 시작하는 문자열(접두어 추출)
x$ : x로 끝나는 문자열(접미어 추출)
x* : x가 0번 이상 반복(없는 경우 포함)
x+ : x가 1회 이상 반복
x? : x가 0 또는 1회 포함 
x{m, n} : x가 m~n 사이 연속 
x{m, } : x가 m 이상 연속
x{,n} : x가 n 이하 연속
[x] : x문자 한 개 일치
[^x] : x문자 제외 
| : or 조건식(예 : [a-z|A-Z]) 
\ : 이스케이프 문자 또는 일반문자를 메타문자로 변환(예: \d, \w, \s)
() : 그룹핑(예 : '([a-z]{3}|\d{3})' ) = 여러 개 패턴 묶기
"""

st1 = '1234 abc홍길동 ABC_555_6 이사도시'
st2 = 'test1abcABC 123mbc abbc,ac 45text'
st3 = 'test^홍길동 abc 대한*민국 123$tbc'


# 정규표현식 함수 제공  모듈 
import re # 모듈(re.py) - 방법1 
# import 모듈
# 반드시 모듈명.함수명()으로 호출

from re import findall, match, sub # 방법2
# from 모듈명 import 함수1, 함수2, 함수3
# 직접 호출 가능: 함수명() -> 편리하기 때문에 더 많이 사용

from re import * # 모든 함수 혹은 클래스 사용 의미

dir(re)
'''
 'compile',
 'copyreg',
 'enum',
 'error',
 'escape',
 'findall',
 'finditer',
 'fullmatch',
 'functools',
 'match',
 'purge',
 'search',
 'split',
 'sre_compile',
 'sre_parse',
 'sub',
 'subn',
 'template'
'''

# 1. re.findall('pattern', string) -> 모든 문자: list로 반환
# 패턴은 반드시 따옴표('') 안에 표현
# 1) 숫자 찾기  
print(re.findall('1234', st1)) # ['1234']
print(re.findall('[0-9]', st1)) # 숫자 조회: ['1', '2', '3', '4', '5', '5', '5', '6']
print(re.findall('[0-9]{3}', st1)) # ['123', '555']
print(re.findall('[0-9]{3,4}', st1)) # ['1234', '555']
print(re.findall('\d{3,4}', st1)) # ['1234', '555']

# 2) 문자열 찾기 
print(findall('[가-힣]{3}', st1)) # 국문자 조회: ['홍길동', '이사도']
print(findall('[a-z]{3}', st1)) # 영문자 조회: ['abc']
print(findall('[a-z|A-Z]{3}', st1)) # 영문자 조회: ['abc']
print(findall('[A-z]{3}', st1)) # 영문자 조회: ['abc']

st1 # '1234 abc홍길동 ABC_555_6 이사도시'
type(st1) # string: 순서가 있는 문자들의 집합

words=st1.split() # 공백 기준 단어
words

names=[] # 한글이름
for w in words:
    result=findall('[가-힣]{3,}',w) # 일치하는 것이 없으면 빈 리스트 출력
    print(result) # [] 또는 ['홍길동']
    if result: # []: FALSE, ['홍길동']: TRUE
        # names.append(result) # [['홍길동'], ['이사도시']]
        names.extend(result) # ['홍길동', '이사도시']
names

# 3) 접두어/접미어 문자열 찾기 
st2 = 'test1abcABC 123mbc abbc,ac 45text'

print(findall('^test', st2)) # ['test']
print(findall('^text', st2)) # []
print(findall('text$', st2))  # ['text']


# [문제] 'http://news'로 시작하는 url 추출하기  
urls = ['http://news.com/test', 'new.com','http://news.com/test2', 'http//~']
len(urls) # 4

result=[] # 올바른 url 저장하기
for i in urls:
    find=findall('^http://news',i)
    if find:
        # 리스트가 아닌 원소 하나기 때문에 append 활용
        result.append(i) # 해당 url 저장
print(result)

# 문자열 중간에서 문자 찾기
findall('.bc',st2) # ['abc', 'mbc', 'bbc']
findall('b.',st2) # ['bc', 'bc', 'bb']

# 4) 단어(word) : \w = 한글, 영문자, 숫자 (특수문자, 문장부호, 공백 제외)
# 불용어 처리
st3 = 'test^홍길동 abc 대한*민국 123$tbc'

words = findall('\w{3,}', st3)
print(words) # ['test', '홍길동', 'abc', '123', 'tbc']

wo='   this is me    '
findall('\b',wo)

# 5) 문자열 제외 : [^제외문자]
print(findall('[^t]+', st3)) # t를 제외한 나머지 문자가 1회 이상 연속된 경우 
# t외 문자열 출력
# ['es', '^홍길동 abc 대한*민국 123$', 'bc']

# 불용어: 특수문자(^, *, $)
findall('[^^*$\s]+',st3)
# ['test', '홍길동', 'abc', '대한', '민국', '123', 'tbc']

# 6) x문자 반복: *, +, ?
st2 # 'test1abcABC 123mbc abbc,ac 45text'

# x가 0번 이상 반복: *
findall('ab*c',st2) # Out[112]: ['abc', 'abbc', 'ac'] - [1회,2회,0회]
# *의 target: b -> b가 한번도 안나와도 출력

# x가 1번 이상 반복: +
findall('ab+c',st2) # ['abc', 'abbc'] - [1회,2회]

# x가 0번 혹은 1번: ?
findall('ab?c',st2) # ['abc', 'ac'] - [1회, 0회]

# 2. re.match(pattern, string) 
# 양식이 올바른지 확인하기 위해 사용
jumin = '123456-3234567'
len(jumin)
match('^d',jumin)
match('6',jumin)
result = match('\d{6}-[1-4]\d{6}', jumin) 
result # <re.Match object; span=(0, 14), match='123456-3234567'>
# match에 의해 만들어진 객체; 객체 정보
# 일치하지 X: none(아무것도 출력되지 않음)

if result : # Object 반환 = TRUE, None = FALSE
    print('주민번호 양식')
else :
    print('잘못된 양식')
# 매칭된 텍스트 반환
result.group()


# 3. re.sub(pattern, rep, string)  -> r의 gsub와 비슷
st3 = 'test^홍길동 abc 대한*민국 123$tbc'

text = sub('[\^*$]', '', st3)
print(text) 

# findall() vs sub()
sub('[\^*$\s]','',st3) # 교체(제거)
# 'test홍길동abc대한민국123tbc'
findall('[^^*$\s]+',st3) # 모든 문자 찾기
# ['test', '홍길동', 'abc', '대한', '민국', '123', 'tbc']
split('[\^*$\s]',st3)

# 4. re.search(pattern, string)
# 해당하는 문자 하나만 찾기
'''
.*: 임의의 문자 0번 이상 반복 의미
.+: 임의의 문자 1번 이상 반복 의미
'''
text = "<span> <head> 안녕하세요. </head> </span>"
head = re.search("<head>.*</head>", text) 
head = search("<head>.+</head>", text) 
head.group() # '<head> 안녕하세요. </head>'

text2 = "<span> <head></head> </span>"
head2 = search("<head>.+</head>", text2) 
head2.group() # AttributeError: 문자열을 찾지 못하면 Error 발생

he=search('[^<]+',text)
he.group()

he2=findall('[^<]+',text)
print(he2)

# 5. compile(pattern): 패턴 객체 생성 -> 반복 사용
# 패턴을 반복적으로 사용 시 이용
urls = ['http://news.com/test', 'new.com','http://news.com/test2', 'http//~']

url_pat=compile('^http://news.+')
str(url_pat)
print(url_pat)
'''
 'findall',
 'finditer',
 'flags',
 'fullmatch',
 'groupindex',
 'groups',
 'match',
 'pattern',
 'scanner',
 'search',
 'split',
 'sub',
 'subn'
'''
url_pat.findall(urls[0]) # ['http://news.com/test'] -> TRUE
url_pat.findall(urls[1]) # [] -> FALSE
urls_re=[]
for url in urls:
    if url_pat.findall(url):
        print(url)
        urls_re.append(url)
'''
http://news.com/test
http://news.com/test2
'''
for url in urls:
    print(url_pat.findall(url))

# list 내포
urls_re=[url for url in urls if url_pat.findall(url)]
urls_re
