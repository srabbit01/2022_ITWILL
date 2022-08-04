# -*- coding: utf-8 -*-
"""
step01_mariaDB_test.py

"""
import pymysql # driver: python + DB(Maria DB 연동)
# pip install pymysql

# print(pymysql.version_info) # version 확인 
pymysql.version_info #  (1, 4, 0, 'final', 0)

# DB 연동 환경변수 
config = { # 'key': 'value' = dict 형태
    'host' : '127.0.0.1', # DB가 설치된 서버 주소
    'user' : 'scott', # 접근 권한 가진 사용자 명
    'password' : 'tiger', # 사용자 비밀번호
    'database' : 'work', # 접근 데이터베이스명
    'port' : 3306, # DB 포트번호
    'charset':'utf8', # encoding 방식
    'use_unicode' : True} # 유니코드 사용 여부 (utf-8은 유니코드 형식)
    # 환경변수 이름들은 이미 정해짐
try :
    # 1. db 연동 객체 생성 
    conn = pymysql.connect(**config) # **: dict 내 내용을 문자형이 아닌 실인수로 넘김 의미
    
    # 2. sql문 실행 객체 
    cursor = conn.cursor() # object.method()
    
    # 3. sql문 작성
    query = 'select * from goods'
    cursor.execute(query) # query문 실행
    
    # 4. 전체 레코드 가져오기
    datas=cursor.fetchall()
    
    # 5. 레코드 출력
    for d in datas:
        print(d) # 행 단위: tuple
        print(d[0],d[1],d[2]) # 칼럼(열) 단위 -> 색인 이용
   
except Exception as e :
    print('db error : ', e)
finally :
    cursor.close(); conn.close() # 객체 닫기  -> 역순: 먼저 만들어진 것 나중, 나중 만들어진 것 먼저

## dict 함수에 입력
def test(**args): # dict형 가변인수
    print(args)
datas={'uid':'hong','pwd':'1234'} # dict
# 함수 호출
# test(datas) # TypeError
test(**datas) # 객체 자체가 실인수 임을 의미
test(**{'uid':'hong','pwd':'1234'})















