# -*- coding: utf-8 -*-
"""
step02_CRUD.py

CRUD
- Create(Insert), Read(Select), Update, Delete
= 모든 데이터 베이스 제공
"""

import pymysql

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
            
    # 1. 레코드 추가: Create(Insert)
    '''
    do=input('레코드 입력하시겠습니까?(yes/no) ').lower()
    while do == 'yes':
        code=int(input('code 입력하시오 : '))
        name=input('name 입력하시오 : ')
        su=int(input('수량 입력하시오 : '))
        dan=int(input('단가 입력하시오 : '))
        Iquery=f"INSERT INTO goods VALUES ({code},'{name}',{su},{dan})" # 문자열 따옴표 지정 필요
        cursor.execute(Iquery) # 레코드 추가
        conn.commit() # db 반영: 반드시 반영 필요
        do=input('계속 입력하시겠습니까?(yes/no) ').lower()  
    '''
    
    # 2. 레코드 수정: Update = Code 조회 -> name, su, dan 조회 -> 수정
    code=int(input('수정 code 입력하시오 : '))
    name=input('수정 name 입력하시오 : ')
    su=int(input('수정 수량 입력하시오 : '))
    dan=int(input('수정 단가 입력하시오 : '))
    Uquery=f"""UPDATE goods SET name='{name}', su={su}, dan={dan}
            WHERE code={code}"""
    cursor.execute(Uquery) # 레코드 수정
    conn.commit() # db 반영
    # 문제 발생 시, ROLLBACK 필요
    
    
    # 3. 레코드 삭제: Delete
    '''
    code=int(input('삭제 code 입력하시오 : '))
    # 1) CODE 조회
    Oquery=f"SELECT * FROM goods WHERE code={code}"
    cursor.execute(Oquery)
    row=cursor.fetchone() # 레코드 1개
    # 2) 레코드 삭제 or 메시지 출력
    if row: # null==False
        Dquery=f"DELETE FROM goods WHERE code={code}"
        cursor.execute(Dquery) # 레코드 삭제
        conn.commit() # db 반영
    else:
        print('\n*** 해당 레코드 없음 ***\n')
    '''
    
    # 4. 레코드 조회 : Read   
    query = "select * from goods"
    cursor.execute(query)    
    dataset = cursor.fetchall() # 전체 레코드 가져오기 
    
    # 레코드 출력 
    print('code\t name\t su\t dan')
    print('-'*40)
    for row in dataset :
        print("{0}      {1}     {2}    {3}".format(row[0],row[1],row[2],row[3]))
        
    print('-'*40)
    print('전체 레코드 수 : ', len(dataset))      
    print()
    
    '''
    # 전체 데이블 조회
    Squery='SHOW TABLES'
    cursor.execute(Squery) # query 실행
    tables = cursor.fetchall() # 전체 레코드 가져오기
    for t in tables:
        print(t)
    print('work DB 내 전체 테이블 수 :',len(tables))
    '''
    
except Exception as e :
    print('db error :', e)
    # db error : (1146, "Table 'work.good' doesn't exist") -> 오티 확인
    conn.rollback() # commit 이전 상태로 되돌리기
finally :
    cursor.close(); conn.close()