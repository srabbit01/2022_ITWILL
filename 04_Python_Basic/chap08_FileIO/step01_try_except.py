'''
예외처리: run time (실행 시점) error 발생 시 처리
  - file/DB 입출력 시 문제 발생  
  - 반복 수행 과정에서 계산이 불가능한 자료 포함
  - 웹문서 수집 : url 이용 문서 수집 시 url 없는 경우 

예외처리 형식)  
try :
    예외발생 코드 
except 예외처리클래스 as 변수: 
    예외처리 코드 
finally :
    항상 실행 코드

 
'''
# 1. 반복 수행 과정에서 계산이 불가능한 자료 포함

print('프로그램 시작 !!!')
x = [10, 20, 5, 30, 'num', 7 ] # List
'''
for i in x :
    print(i)    
    y = i**2  # 예외 발생 type(s) for ** or pow(): 'str' and 'int' = STOP
    print('y =', y)
'''
print('프로그램 종료') # 이후 과정이 이행되지 않음

# 예외 처리
for i in x:
    print(i)
    try:
        y=i**2
    except TypeError:
        print("예외 발생!!!") # 메시지
    else: print('y =',y)
print("프로그램 종료")

# 2. 문자열 처리과정에서 에러 처리   

import re 
texts = ["<span><h1>제목1</h1></span>", "<h1></h1>", "<p><h2>제목2</h2></p>"]

# 패턴를 찾아서 내용 출력 
'''
print(re.search("<h1>.+</h1>", texts[0]).group()) # <h1>제목1</h1>
print(re.search("<h1>.+</h1>", texts[1]).group()) # AttributeError
'''

tag=[] # tag 내용 저장
for st in texts:
    try:
        # print(re.search("<h.>.+</h.>", st).group()) # AttributeError
        tag.append(re.search("<h.>.+</h.>", st).group())
    except Exception as e: # 예외 전담 클래스
        # e 예외 정보 저장 클래스
        print('예외발생 :',e) # 예외 발생 이유 출력
'''
예외발생
'''
print(tag) # ['<h1>제목1</h1>', '<h2>제목2</h2>']

# 3. 다중 예외 처리
import os
os.getcwd() # 현재 경로 확인
try:
    fh=open('testfile.txt','w') # file 쓰기
    fh.write('테스트 데이터를 파일에 씁니다!!')
    # file=open('test.txt','r') # file 읽기
    # file.read()
    div=100/0 # 산술적 예외
    num=int(input('숫자 입력 : '))
    print('num =',num) # num = 10
except FileNotFoundError:
    print("Error: 파일을 찾을 수 없거나 데이터를 쓸 수 없습니다.")
except ValueError as e:
    print('예외처리 :', e)
    # 예외처리 : invalid literal for int() with base 10: 'hi'
except Exception as e:
    print('나머지 모든 예외처리 :',e)
    # 나머지 모든 예외처리 : division by zero
finally:
    print("프로그램 종료: 항상 실행되는 영역")


## My Code
try:
    print("안녕하세요")
    print("hello")
    li=['Hello']
    10/0
except:
    print('예외 발생')

    
    