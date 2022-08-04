'''
chap02_String > step01_string.py

문자열(string)의 특징
- 문자열: 순서가 있는 문자들의 집합
- 순서가 존재 (순서가 존재하지 않으면 인덱싱 불가능)
- 인덱싱/슬라이싱
- 수정불가: 새로운 객체 생성
'''
# 1. 문자열 유형 

# 1) 한 줄 문자열 
lineStr = "this is one line string" 
print(type(lineStr)) # <class 'str'>

# 2) 여러줄 문자열 
multiLine = """This
is multi line
string"""
print(multiLine)
# This
# is multi line
# string -> 줄 단위 출력 가능
print(type(multiLine)) # <class 'str'>

'''
classs: 객체를 생성하는 도구
objec: class에 의해 만들어진 결과물
'''

# 3) sql문 
query ="""select * from emp
where deptno = 1001
order by sal desc"""
print(query)


# 2. indexing/slicing 가능 
'''
R index: 1부터 -> 변수[1]
Python index: 0부터 -> 변수[0]
'''
# 1) indexing: 특정 문자 참조
# 왼쪽 기준 색인 
print('왼쪽의 첫번째 문자 : ', lineStr[0]) 
print(lineStr[0:4]) # 0~3 
print(lineStr[:4]) # 0~3

# 오른쪽 기준 색인 
print(lineStr[-1]) 
print(lineStr[-6:]) # string
print(lineStr[-6:-1]) # strin

# 2) slicing: 특정 문자 집합 자르기 -> 새로운 객체 생성
subStr = lineStr[:4]
print(subStr) # this
type(subStr) # str


# 3. 문자열 연산 
print('python' + ' program') # 결합연산자 
print('python'' program')

print('-'*50) # 반복연산자 


# 4. 문자열 처리 함수 
'''
dir(): 객체 처리 함수 (매서드) 확인
'''
dir(testStr)
'''
count, find, index, isalpha, isascii,lower,replce,split,strip,upper
'''

# 형식) 스트링객체.메서드()
'''
함수(function) vs 메서드(method)
- 공통점: 기능 제공
- 차이점
  - 함수: 단독 호출
  - 메서드: 자체 제공은 안되고, 해당 객체가 존재하여야 점(.)을 이용하여 호출
'''
help(len) # 단독 함수: Help on built-in function len in module builtins:
# help(split) # Error 발생 -> 단독 사용 불가능
help(multiLine.split) # 메서드: 도움말 확인 시, 객체와 함께 호출

testStr = " My name is hong!! "  # 스트링객체
# testStr = str(" My name is hong!! ")
print(type(testStr)) # <class 'str'>
len(testStr) # 19: 공백 포함 원소 개수

# 1) 문자 찾기 : 해당 문자의 색인 반환
print(testStr.find('z')) # -1: 문자 없는 경우
print(testStr.find('m')) # 6
testStr[6] # 'm'
print(testStr.find('M')) # 1 
'''
find(): 색인 반환, 문자 없는 경우 -1 반환
index(): 색인 반환, 문자 없는 경우 error 발생
'''
print(testStr.index('i')) # 9
print(testStr.index('is')) # 9
print(testStr.index('be')) # ValueError

# 2) 문자 개수 반환  
print(testStr.count('n')) # 2

# 3) 문자 유형 구분 
testStr.isalpha() # False # 알파벳으로만 구성 여부 -> 객체 내에 숫자, 공백, 특수 문자등 포함 시
testStr.isascii() # True # 아스키 코드로만 구성 여부
"hello!".islower()
testStr.islower() # False  # 소문자로만 구성 여부
'1234'.isnumeric() # TRUE # 문자열이 숫자로만 구성 여부

# 4) 대소문 처리 
testStr.upper() # ' MY NAME IS HONG!! '
testStr.lower() # ' my name is hong!! '

# 5) 접두어 판단 -> T/F
testStr.startswith(' My') # True
testStr.startswith('My') # FALSE
testStr.startswith(' ') # True

# 6) 단어 교체 
testStr = testStr.replace('!', '') # replace('old','new')
testStr # ! 제거
testStr=testStr.replace(' ','') # 모든 공백 제거: 'Mynameishong'
testStr.isalpha() # True: 영문자만 존재

# 7) 문장 앞 뒤 공백 제거
newTestStr=testStr.strip()
newTestStr # 새로운 객체에 저장 -> 기존 내용 수정 X

# 8) 문자 결합
'*'.join(testStr)

# 5. 문자열 분리(split) 및 결합(join)
'''
split: 문단 -> 문장, 문장 -> 딘아
join: 단어 -> 문장
'''
print(multiLine)
'''
This
is multi line
string
'''

# 1) split: 문자열 분리
# 문단 -> 문장
sents=multiLine.split(sep='\n')
sents # ['This', 'is multi line', 'string']
len(sents) # 3

# 문장 -> 단어 split
words=multiLine.split() # split(sep='')
words # ['This', 'is', 'multi', 'line', 'string']

# 최대 split 개수 지정
multiLine.split(sep=' ',maxsplit=1) # ['This\nis', 'multi line\nstring']

# 여러 개의 구분자로 split: 정규 표현식 사용
string='우리나라 대한,민국'
import re # 정규표현식 함수 제공

re.findall('[^,\s]+',string)
# ['우리나라', '대한', '민국']

hi='나는    마라탕이,먹고싶다'
re.findall('[^,\s]+',hi)
re.findall('[^,\s]',hi)
re.findall('[,\s]+',hi)
re.findall('[,\s]',hi)

# 2) join: 문자열 결합
# 단어 -> 문장

# 형식) '구분자.join(스트링객체)
sent=' '.join(words)
sent # 'This is multi line string'