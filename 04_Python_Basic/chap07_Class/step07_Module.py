# -*- coding: utf-8 -*-
"""
step07.Module.py
"""
# __init__.py = 환경설정 파일

import os # file 경로 확인/변경

os.getcwd() # R의 getwd()와 같이 작업 경로 확인
# 'C:\\Users\\hsj\\Documents\\Crystal_TEMP'

# 사용할 모듈의 경로로 변경: 패키지/모듈이 포함된 상위 폴더 지정
os.chdir(r'C:\Users\hsj\Documents\Crystal_TEMP\chap07_Class') # 작업 경로 변경
os.getcwd()
# 'C:\\Users\\hsj\\Documents\\Crystal_TEMP\\chap07_Class'

# 사용할 모듈 import
# 방법1
from myPackage import module01
# 방법2
from myPackage.module01 import Adder, Mul # 클래스/함수 사용 시 모듈 명 사용 필요 없음
'''
myPackage.module01 = print(__name__)
add=30
'''

# 모듈의 함수 호출: 방법1
add = module01.Adder(10,20)
print('add=',add)

# 클래스 객체 생성
obj=module01.Mul(10,20)
print('mul=',obj.mul()) # mul = 200

# 모듈의 함수 호출: 방법1
add = Adder(10,20)
print('add=',add)