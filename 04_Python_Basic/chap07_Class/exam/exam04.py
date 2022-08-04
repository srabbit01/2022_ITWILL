'''
문) 다음과 같은 조건으로 모듈을 추가하고, 결과를 확인하시오.
   모듈 위치 : myPackage 패키지 
   모듈명 : module02.py
   함수 정의 : 사칙연산 수행 함수 (Add, Sub, Mul, Div)   
   사칙연산 함수 호출하여 결과 확인
  
    <<출력 결과 예>>
  x = 10; y = 5 일 때
  Add= 15
  Sub= 5
  Mul= 50
  Div= 2.0
'''

# 모듈 로딩
import os
os.getcwd() # 'C:\\Users\\hsj\\Documents\\Crystal_TEMP'
os.chdir('C:\\Users\\hsj\\Documents\\Crystal_TEMP\\chap07_Class')

from myPackage import module02

# 입력 받기
a = int(input('x : '))
b = int(input('y : '))
print()

# 객체 생성
cal=module02.calculation(a,b)
print('x = %d; y = %d 일 때' %(a,b))
cal.add()
cal.sub()
cal.mul()
cal.div()
