# -*- coding: utf-8 -*-
"""
step05_join_subquery.py

- HidiSQL SQL 파일 불러오기 실습
  -> [파일] > [SQL 파일 불러오기] > dept_tab.sql 파일 선택  
  -> SQL 실행 방법 : [실행] 
  
1. table 생성 : HidiSQL 이용(dept_tab.sql 참고)   
2. join & subquery : emp vs dept 
  -> ANSI 표준 JOIN 
  -> subquery : 부호번호(dept) -> 사원정보(emp)
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
    
    # 1. ANSI inner join 
    sql = """SELECT e.eno, e.ename, e.sal, d.dno
    FROM emp e INNER JOIN dept d # 두 테이블의 교집합 구하기
    ON e.dno = d.dno and e.sal >= 250""" # JOIN 조건 AND 일반 조건
    
    cursor.execute(sql)
    dataset = cursor.fetchall()
    
    # 레코드 조회 
    for row in dataset :
        print(row[0], row[1], row[2], row[3])   
    
    # 2. subquery: 부서 테이블(dno) -> 사원 정보(emp)
    dno=int(input('조회할 부서 번호 : '))
    sql=f"""SELECT * FROM emp
        WHERE dno = (SELECT dno FROM dept WHERE dno={dno})"""
    cursor.execute(sql)
    dataset=cursor.fetchall()
    if dataset:
        for row in dataset:
            print(row[0],row[1],row[5])
    else:
        print("조회되는 레코드 없음")
    
        
except Exception as e :
    print('db error : ', e)
finally :
    cursor.close(); conn.close()
    
    
    
    
    
    
    
    
    
    
    