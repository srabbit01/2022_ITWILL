'''
문제2) 다음과 같은 메뉴를 이용하여 goods 테이블을 관리하시오.
    [레코드 처리 메뉴 ]
1. 레코드 조회
2. 레코드 추가
3. 레코드 수정
4. 레코드 삭제
5. 프로그램 종료
    메뉴번호 입력 : 
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

try:
    # db 연결 객체 생성 
    conn = pymysql.connect(**config)
    # SQL 실행 객체 생성 
    cursor = conn.cursor()    
    
    while True :  # 무한루프 
        print('\n\t[레코드 처리 메뉴 ]')
        print('1. 레코드 조회')
        print('2. 레코드 추가')
        print('3. 레코드 수정')
        print('4. 레코드 삭제')
        print('5. 프로그램 종료')    
        menu = int(input('\t메뉴번호 입력 : '))
        
        if menu == 1 :
            query=f"SELECT * FROM goods;"
            cursor.execute(query)
            dataset=cursor.fetchall()
            for d in dataset:
                print('{} {} {} {}'.format(d[0],d[1],d[2],d[3]))
        elif menu == 2:
            code=int(input('code 입력하시오 : '))
            name=input('name 입력하시오 : ')
            su=int(input('수량 입력하시오 : '))
            dan=int(input('단가 입력하시오 : '))
            Iquery=f"INSERT INTO goods VALUES ({code},'{name}',{su},{dan})" # 문자열 따옴표 지정 필요
            cursor.execute(Iquery) # 레코드 추가
            conn.commit() # db 반영: 반드시 반영 필요
        elif menu == 3:
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
                print('\n*** 해당 레코드 없음 ***\n')
        elif menu == 4:
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
        elif menu == 5 :
            print('프로그램 종료')
            break # 반복 exit
        else :
            print('해당 메뉴는 없습니다.')
        
# DB 연결 예외 처리          
except Exception as e :
    print('db 연동 오류 : ', e)
    conn.rollback()
finally:
    cursor.close()
    conn.close() 
