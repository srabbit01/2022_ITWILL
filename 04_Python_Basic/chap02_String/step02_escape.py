# -*- coding: utf-8 -*-
"""
2. escape 문자 
 escape 문자  : 특수기능의 문자(\n, \t, \b, \r, '', "")
 기능 차단: escape 문자의 기능 차단 (콘솔 출력, 파일 경로 사용)
"""

print('escape 문자')
print('\\n출력') # escape 기능 차단1 - \ 
print(r'\n출력') # escape 기능 차단2 - r 

# 경로 표현 
print('c:\python\test') # escape 문자
print('c:\\python\\test') # escape 문자 기능 차단
print(r'c:\python\test') # escape 문자 기능 차단 = /와 같은 기능

# 문) c:\'aa'\"abc.txt" 형식으로 출력되도록 하시오.
print('c:\\\'aa\'\\\"abc.txt\"')

# file read: text.txt
file=open(file='C:/work/Crystal/DataAnalysis/[ITWILL]BigDataAnalysis_ExpertTraining/04. Python Basic/workspace/chap02_String/text.txt',
     mode='r',encoding='UTF-8') # 객체 열기: 파일 읽어오기
# mode: 파일 읽기/쓰기 등 모드 설정
# 인코딩 기본: utf-8

print(file.read())
'''
우리나라 대한민국
나는 홍길동 입니다.
'''
# 객체 사용이 끝났으면 닫기
file.close()