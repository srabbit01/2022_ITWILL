# -*- coding: utf-8 -*-
"""
step04_emp_table.py

1. table 유무 판단 : show tables 
2. 레코드 추가/조회 & table 생성 
  -> table 있는 경우 : 레코드 추가/조회 (emp_tab.sql 참고)
  -> table 없는 경우 : 'table 생성' (emp_tab.sql 참고)
"""

import pymysql # driver = python + DB(Mysql)

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
    
    # 1. table 유무 판단 : emp 
    cursor.execute("show tables") # table 목록 조회 
    tables = cursor.fetchall() # table 목록 가져오기 

    # emp 테이블 조회 
    sw = False # off
    for table in tables : # ('goods','zipcode_tab','emp') : tuple
        if 'emp' in table :
            sw = True # on -> switch 기법
    # switch 기법: 특정 테이블이 존재하면 TRUE 전환, 존재하지 않으면 그대로 FASLE
    
    # 2. 레코드 조회/추가 or table 생성         
    if sw : # table 있는 경우        
        query = "select * from emp"
        cursor.execute(query)
        dataset = cursor.fetchall()
        
        if dataset : # 1) 레코드 있는 경우 : 조회 
            for row in dataset : 
                print(row) # tuple type 
            print('전체 레코드 수 : ', len(dataset))
            import pandas as pd
            pd.DataFrame(dataset,columns=['no','이름','고용날짜','급료','보너스','직책','부서번호'])
            

        else : # 2) 레코드 없는 경우 : 추가 
            print('레코드 추가')
            cursor.execute("""insert into emp(ename, hiredate, sal, bonus, job, dno) 
                                   values('홍길동','2008-10-20',300, 35,'관리자',10);""")
            cursor.execute("""insert into emp(ename, hiredate, sal, bonus, job, dno) 
                                   values('강호동', '2010-10-20', 250, 0,'사원', 20);""")
            cursor.execute("""insert into emp(ename, hiredate, sal, bonus, job, dno) 
                                   values('유관순', '2008-03-20', 200, 0,'사원', 10);""")
            cursor.execute("""insert into emp(ename, hiredate, sal, bonus, job, dno) 
                                   values('강감찬', '2007-01-20', 450, 100,'관리자', 20);""")
            conn.commit() # db 반영

    else : # table 없는 경우     
        print('테이블 생성')     
        cursor.execute(f"""create or replace table emp(
                    eno int auto_increment primary key,
                    ename varchar(20) not null,
                    hiredate date not null,
                    sal int not null,
                    bonus int default 0,
                    job varchar(20) not null,
                    dno int);""") # table 생성
        print('~~ emp 테이블 생성 완료 ~~')
    
except Exception as e :
    print('db error : ', e)
finally :
    cursor.close(); conn.close()    
    
# exam03.py    
    
    
    
    
    
    
    
    
    
    



