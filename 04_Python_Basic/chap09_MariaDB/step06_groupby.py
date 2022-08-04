# -*- coding: utf-8 -*-
"""
step06_groupby.py

select 집계함수(avg, sum) from table
group by 집단변수(부서번호, 직책) 
having 조건식;
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
    
    # emp 테이블 : 부서번호 or 직책 
    gcol = int(input('그룹 칼럼 선택 : (1. 부서, 2. 직책) : '))
    if gcol > 2 or gcol < 1 :
        print('그룹 불가')
    else :
        if gcol == 1 : # dno
            sql = """select dno, sum(sal), round(avg(sal),2) 
                  from emp 
                  group by dno
                  order by dno"""
        else : # job
            sql = """select job, sum(sal), round(avg(sal),2) 
                  from emp 
                  group by job
                  having round(avg(sal),2)>=300"""
        
        cursor.execute(sql)    
        data = cursor.fetchall()
        
        for row in data :
            print(row[0], row[1], row[2])
            
        print('전체 레코드 수 : ', len(data))          
           
except Exception as e :
    print('db error : ', e)
finally :
    cursor.close(); conn.close()   
    
    
