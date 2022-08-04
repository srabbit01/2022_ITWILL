# -*- coding: utf-8 -*-
"""
step03_zipcode_table.py

<< 작업순서 >>
1. table 생성 : HidiSQL 이용(zipcode.sql 파일 참고) 
2. zipcode.txt -> 서울 지역 -> 레코드 추가    
3. 레코드 조회(동 or 구 검색)
"""

import pymysql # driver 

path = 'C:\\work\\Crystal\\DataAnalysis\\[ITWILL]BigDataAnalysis_ExpertTraining\\04. Python Basic\\workspace\\chap08_FileIO\\data'

config = {
    'host' : '127.0.0.1',
    'user' : 'scott',
    'password' : 'tiger',
    'database' : 'work',
    'port' : 3306,
    'charset':'utf8',
    'use_unicode' : True}
               
try :
    # db 연동 객체 생성 
    conn = pymysql.connect(**config)
    # sql문 실행 객체 
    cursor = conn.cursor() 
    
    # 1. 레코드 조회 
    cursor.execute("select * from zipcode_tab")
    datasest = cursor.fetchall()
    
    # 2. 레코드 추가 or 조회 	
    if not(datasest) : # False -> True: 테이블은 존재하나 레코드 없는 상태
        print('1) 레코드 추가')
        file=open(path+'\zipcode.txt',mode='r',encoding='utf-8')
        line=file.readline()
        while line: # line = EOR('') # 끝 임을 의미하며 반복문 중단
            token=line.split('\t') # token
            if token[1]=='서울':
                zipcode=str(token[0]) # '123-456'
                city=token[1]; gu=token[2]; dong=token[3]; detail=token[4]
            if detail: # 상세 주소 존재할 시 실행
                query=f"""INSERT INTO zipcode_tab 
                    VALUES ('{zipcode}','{city}','{gu}','{dong}','{detail}')"""
            else: # 상세 주소 존재하지 않을 시 실행 -> NULL값 입력
                query=f"""INSERT INTO zipcode_tab(zipcode,city,gu,dong)
                    VALUES ('{zipcode}','{city}','{gu}','{dong}')"""
            cursor.execute(query) # 레코드 추가
            conn.commit() # db 반영
            line=file.readline() # 2번줄 ~ EOF
            
    else : # 테이블 및 레코드 모두 존재
        print('2) 레코드 조회')
        choice=int(input('1. 동 검색, 2. 구 검색 : '))
        if choice==1:
            dong=input('검색할 동 입력 : ')
            query=f"SELECT * FROM zipcode_tab WHERE dong LIKE '%{dong}%'"
            cursor.execute(query)
            dataset=cursor.fetchall()
            if dataset: # 조회된 레코드가 존재하는 경우
                for row in dataset:
                    print(row)
                print('검색된 주소 개수 :',len(dataset))
            else: # 조회된 레코드가 존재하지 않는 경우
                print("~~해당 동 존재하지 않음~~")
        else:
            gu=input('검색할 구 입력 : ')
            query=f"SELECT * FROM zipcode_tab WHERE gu LIKE '%{gu}%'"
            cursor.execute(query)
            dataset=cursor.fetchall()
            if dataset: # 조회된 레코드가 존재하는 경우
                for row in dataset:
                    print(row)
                print('검색된 주소 개수 :',len(dataset))
            else: # 조회된 레코드가 존재하지 않는 경우
                print("~~해당 구 존재하지 않음~~")
            

except Exception as e :
    print('db error : ', e)
    conn.rollback() 
finally :
    cursor.close(); conn.close()
    
    
    
    
    
    
    