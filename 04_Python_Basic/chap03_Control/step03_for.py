'''
반복문(for)

형식) 
for  변수 in 반복가능객체 :
    실행문
    실행문
    
변수 in 반복가능객체: 객체의 원소 순회 -> 변수 넘김
반복가능(iterable) 객체: string, list, tuple, set, dict
'''


# 1. 문자열 객체
string = "나는 홍길동 입니다."
len(string) # 11

# 문자 -> 변수 넘김
for s in string : # 11회 반복
    print(s, end = '') 
print()

# 단어 -> 변수 넣기: 단어 단위 list 넣기
for w in string.split():
    print(w) # 3회 반복: 나는, 홍길동, 입니다.

import random # random module: 난수 생성


# 2. list 객체 : 1차원 벡터 생성 
help(list) # Help on class list in module builtins: (기본 클래스)

'''
builtins: import 없이 사용 가능한 모듈
모듈(module): 일종의 패키지 -> 함수(function)와 클래스(class)를 제공하는 파이썬(*.py)
함수(function): 기능 제공 도구
클래스(class): 객체 생성 도구
'''

lst = list([1, 2, 3, 4, 5]) # class -> object # list() 생략 가능
lst = [1, 2, 3, 4, 5]  # 1차원(vector) = 리스트 객체
print(lst) # 5

for i in lst:
    if i % 2 == 0: # 짝수인 원소만 출력
        print('원소 : ', i)    

# 3. range 객체 : 순서 있는 정수 생성   # range class(객체)
help(range) # Help on class range in module builtins: (기본 클래스)
'''
class range(object)
 |  range(stop) -> range object
 |  range(start, stop[, step]) -> range object
 range(stop): 0~stop-1 점수
 range(start,stop): start~stop-1 점수
 range(start,stop,step): start~strop-1 점수 중 step 단위로 증가/감소
'''

num1 = range(10) # range(stop) 
print('num1 : ', num1)  # range(0, 10) : object info

num2 = range(1, 10) # range(start,stop)
print('num2 : ', num2)  # range(1, 10)

num3=range(1,10,2) # range(start,stop,step)
print('num3 : ',num3) # range(1,10,2)

# 객체 내용 출력

for n in num1:
    print(n, end=' ') # 0 1 2 3 4 5 6 7 8 9 
print()

for n in num2:
    print(n, end=' ') # 1 2 3 4 5 6 7 8 9 
print()

for n in num3:
    print(n, end=' ') # 1 3 5 7 9 
print()


# 4. list + range 객체 : 순서 있는 정수 -> 1차원 벡터 생성  
num2 = range(1, 5)  # 1~4
print('num2 : ', num2)  # num2 :  range(1, 5)

num2 = list(num2) # range -> list형 변환 
print(num2)  # [1, 2, 3, 4]

lst = list(range(1,5))
print(lst) # for문 없이 내용 반환

lst = list(range(1, 101))  # 1 ~ 100
for i in lst:  # 100회
    if i % 5 == 0:
        print(i, end=' ')      
  
print()

# 문) lst(1~100)에서 3의 배수이면서 5의 배수만 출력
for i in lst:
    if i % 3 == 0 and i % 5 == 0:
        print(i)

# 5. 중첩 반복문
'''
for i in 열거형객체 :
   for j in 열거형객체 :
      실행문
'''

# 1) 구구단
print('구구단')
for a in range(2,10):
    # 바깥쪽 영역
    print('~~~ {}단 ~~~'.format(a))
    for b in range(1,10):
        # 안쪽 영역
        print('%d * %d = %d' %(a,b,a*b))
        
# 2) 문자열 처리
string="""나는 홍길동 입니다.
주소는 서울시 입니다.
나이는 35세 입니다."""

# 빈 벡터 선언
sents=[] # 문장 저장
words=[] # 단어 저장

# 문단 > 문장 > 단어
for sent in string.split('\n'): # 문단 -> 문장
    sents.append(sent)
    for word in sent.split(' '): # 문장 -> 단어
        words.append(word)
        
    
print('문장:',sents)
print('문장 길이:',len(sents)) # 문장 길이: 24
print('단어:',words)
print('단어 길이:',len(words)) # 단어 길이: 9