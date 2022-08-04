'''
문제1) goods 테이블을 이용하여 다음과 같은 형식으로 출력하시오.  
 <조건1> 전자레인지 수량, 단가 수정 
 <조건2> HDTV 수량 수정 

    [ goods 테이블 현황 ]
1 냉장고 2 850000
2 세탁기 3 550000
3 전자레인지 5  400000 <- 수량, 단가 수정 또는 추가
4 HDTV 2 1500000  <- 수량 수정
전체 레코드 수 : 4


    [ 상품별 총금액 ]
냉장고 상품의 총금액은 1,700,000
세탁기 상품의 총금액은 1,650,000
전자레인지 상품의 총금액은 2,000,000
HDTV 상품의 총금액은 3,000,000
'''

import pymysql

config = {
    'host' : '127.0.0.1',
    'user' : 'scott',
    'password' : 'tiger',
    'database' : 'work',
    'port' : 3306,
    'charset':'utf8',
    'use_unicode' : True}

# 레코드 조회 함수
def SELECT():
    query = "select * from goods"
    cursor.execute(query)    
    dataset = cursor.fetchall() 
    
try :
    conn=pymysql.connect(**config)
    cursor=conn.cursor()
    
    # 테이블 조회
    SELECT()
    print('code\t name\t su\t dan')
    print('-'*40)
    for row in dataset :
        print("{0}      {1}     {2}    {3}".format(row[0],row[1],row[2],row[3]))
        
    print('-'*40)
    print('전체 레코드 수 : ', len(dataset),'\n')   
    
    # 테이블 수정/추가
    do=input('수정/추가하시겠습니까?(yes/no) ').lower()
    while do=='yes':
        code=int(input('code 입력하시오 : '))
        # 1) CODE 조회
        Oquery=f"SELECT * FROM goods WHERE code={code}"
        cursor.execute(Oquery)
        row=cursor.fetchone() # 레코드 1개
        # 2) 레코드 수정 or 추가
        if row: # null==False
            name=input('수정 name 입력하시오 : ')
            su=int(input('수정 수량 입력하시오 : '))
            dan=int(input('수정 단가 입력하시오 : '))
            Uquery=f"""UPDATE goods SET name='{name}', su={su}, dan={dan}
                WHERE code={code}"""
            cursor.execute(Uquery) # 레코드 수정
            conn.commit() # db 반영
        else:
            name=input('name 입력하시오 : ')
            su=int(input('수량 입력하시오 : '))
            dan=int(input('단가 입력하시오 : '))
            Iquery=f"INSERT INTO goods VALUES ({code},'{name}',{su},{dan})" # 문자열 따옴표 지정 필요
            cursor.execute(Iquery) # 레코드 추가
            conn.commit() # db 반영: 반드시 반영 필요
        do=input('계속 입력하시겠습니까?(yes/no) ').lower()  
    
    # 결과 출력
    SELECT()
    for row in dataset:
        print('{0} 상품의 총 금액은 {1:3,d}'.format(row[1],row[2]*row[3]))

except Exception as e :
    pass

finally:
    pass

