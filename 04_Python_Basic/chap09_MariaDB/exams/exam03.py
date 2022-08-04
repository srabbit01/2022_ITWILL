# -*- coding: utf-8 -*-
"""
문제3) HidiSQL을 이용하여 다음과 같은 단계로 student 테이블을 만들고, 
      DB 연동 프로그램으로 레코드를 추가하고, 조회하시오.
  
단계1> HidiSQL 이용 : student 테이블 만들기(학번,이름,전화번호,학과,지도교수) 
create or replace table student( 
  sno int primary key,              
  sname varchar(10) not null,                        
  tel varchar(15),     
  deptno int,                
  profno  int                
);  


단계2> DB 연동 프로그램 : 테이블에 레코드가 없으면 레코드 추가(insert)  
insert into student values (9411,'서진수','055)381-2158',201,1001);
insert into student values (9413,'이미경','02)266-8947',103,3002);
insert into student values (9415,'박동호','031)740-6388',202,4003);

단계3> DB 연동 프로그램 : 테이블에 레코드가 있으면 레코드 조회(select)   
"""

import pymysql # driver = python + DB(Mysql)
import pandas as pd

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
    
    # 1. table 유무 판단 : student 
    cursor.execute("SHOW TABLES;")
    tables=cursor.fetchall()
    TIn=False
    for t in tables:
        if 'student' in t:
            TIn=True
    
    # 2. 레코드 추가 or 레코드 조회 
    if TIn:
        Aquery=f"SELECT * FROM student"
        cursor.execute(Aquery)
        AF=cursor.fetchall()
        if AF:
            print('레코드 조회')
            PD=pd.DataFrame(AF,columns=['sno','sname','tel','deptno','profno'])
            print(PD)
        else:
            print('레코드 추가')
            cursor.execute("insert into student values (9411,'서진수','055)381-2158',201,1001);")
            cursor.execute("insert into student values (9413,'이미경','02)266-8947',103,3002);")
            cursor.execute("insert into student values (9415,'박동호','031)740-6388',202,4003);")
            conn.commit() # db 반영

    else:
        print('student 테이블 생성 시작')
        cursor.execute("""create or replace table student( 
                        sno int primary key,              
                        sname varchar(10) not null,                        
                        tel varchar(15),     
                        deptno int,                
                        profno  int);""")
        print("student 테이블 생성 완료")
            
except Exception as e :
    print('db error : ', e)
finally :
    cursor.close(); conn.close()
    
    
    
    
    
    