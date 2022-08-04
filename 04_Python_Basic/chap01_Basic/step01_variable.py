# -*- coding: utf-8 -*-
""" 
chap01_Basic

chapter: workspace 폴더에 하위 폴더 생성
lecture & exams: python 패키지 생성
file: python 파일 생성
"""

"""
변수(Variable)
- 자료가 저장된 메모리 이름
- 형식) 변수명=자료(상수값,수식,변수)
"""

# 단축키: F5(전체 실행), F9(줄 혹은 블럭 단위)

# 1. 변수와 자료형 
var1 = "Hello python"
var2 = 'Hello python'
print(var1)
print(var2)

# type : 객체 출처 확인(자료형 확인)
# mode함수와 유사
print(type(var1), type(var2)) # <class 'str'> <class 'str'>

var1 = 100 # 변수 수정
print(var1, type(var1)) # 100 <class 'int'>

var3 = 123.2345
print(var3, type(var3)) # 123.2345 <class 'float'>

var4 = True
print(var4, type(var4)) # TRUE <class 'bool'>


# 2. 변수명 작성 규칙(ppt.12)
'''
- 첫자 : 영문자 or _ 사용가능 
- 두번째 : 숫자 사용 가능 
- 대소문자 구분(Score, score)
- 낙타체 : 두 단어 결합(korScore)
- 키워드(클래스명, 함수명) 사용불가, 한글명 비권장
- 점(.) 사용 불가  
'''

_num10 = 10
_Num10 = 20
print(_num10 * 2) 
print(_Num10 * 2) 


# 낙타체
korScore = 89
matScore = 75
engScore = 55

tot = korScore + matScore + engScore
print('tot =', tot) # tot = 219

# member.id='hong' # error
member_id='hong'
print(member_id)

# 키워드 사용 불가
# True=10 # error 발생

# python 키워드 확인
import keyword # 모듈 임포트(포함) -> 메모리 상에 올림
# 키워드 확인 패키지
kword=keyword.kwlist # 파이썬의 키워드 제공
# '.'의 의미: 모듈명.멤버(모듈구성요소) 혹은 함수 이름 (약속된 연산자 표기)
'''
모듈구성요소 예시
- kwlist: 키워드 목록 가짐 (출처: keyword)
'''
print(kword)
'''
'False', 'None', 'True', 'and', 'as', 'assert',
'async', 'await', 'break', 'class', 'continue',
'def', 'del', 'elif', 'else', 'except', 'finally',
'for', 'from', 'global', 'if', 'import', 'in', 'is',
'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 
'return', 'try', 'while', 'with', 'yield'
'''
print('명령어 개수:',len(kword)) # 명령어 개수: 36
# len(): 변수의 길이(원소의 개수)

# 3. 참조변수: 객체가 저장된 메모리 주소 저장
x = 150 # x는 150 객체의 주소 저장 
x2 = x # x의 주소 복사 
x3=150

# 변수의 내용 출력
print(x) # x 주소 접근 -> 150 출력
print(x2) # 150

# id(): 해당 변수의 주소 출력
# 변수의 주소 출력
print(x) # x주소 접근 -> 150 출력 
print(id(x)) # 140727080663504
print(id(x2)) # 140727080663504
print(id(x3))
# 동일한 주소 저장

# 객체가 동일하면 주소도 동일
y=45.23
y2=45.23

print(y,id(y))
print(y2,id(y2))
