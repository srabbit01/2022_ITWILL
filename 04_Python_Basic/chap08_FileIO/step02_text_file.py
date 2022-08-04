'''
텍스트 파일 입출력(file input/output)
 - 데이터 입출력 시(file, db) 예외 처리한다.
 형식) open('파일경로/파일명', mode='r'/'w'/'a')
        mode = 'r' : 파일 읽기
        mode = 'w' : 파일 쓰기
        mode = 'a' : 파일 쓰기 + 추가
'''

import os 

try :
    # 1. 파일 읽기
    # print('\n현재 경로 :', os.getcwd())    
    # C:\\work\\Crystal\\DataAnalysis\\[ITWILL]BigDataAnalysis_ExpertTraining\\04. Python Basic
    
    # 파일 경로 설정 
    os.chdir('C:\\work\\Crystal\\DataAnalysis\\[ITWILL]BigDataAnalysis_ExpertTraining\\04. Python Basic\\workspace\\chap08_FileIO\\data')
    
    # 2. 파일 읽기
    file = open("ftest.txt", mode = 'r') # file 객체 생성
    print(file.read()) # 파일 전체 읽기
    file.close() # 객체 닫기 = 객체 메모리상 소멸     

    # 3. 파일 쓰기
    file2=open('fwrite.txt',mode='w') # file 객체 생성(쓰기)
    file2.write('    My First Text~~~\n') # 파일 기록
    file2.close() # 객체 닫기
    
    # 4. 파일 추가
    file3=open('fwrite.txt',mode='a') # file 객체 생성(쓰기+추가)
    file3.write('My Second Text~~~') # 파일 기록
    file3.close() # 객체 닫기
    file3=open('fwrite.txt',mode='r')
    li=file3.readline()
    li.strip()
    file3.close()
    
    '''
    # 파일 읽기 객체에서 지원하는 메서드
    파일객체.read(): 파일 내 전체 문서 문자열 읽기(하나의 string 객체)
    파일객체.readline(): 파일 내 한 줄 문자열 읽기(string)
    파일 객체.readlines(): 파일 내 전체 문서 줄 단위 읽기(list)
    '''
    file4=open('ftest.txt',mode='r') # file 객체 생성(읽기)
    # 5. readline: 한 줄 읽기 (파일 EOF = 빈 문자열 리턴)
    # 문장이 몇 줄 존재하는지 알 수 없기 때문에
    while True:
        line=file4.readline() # 한 줄 읽기
        if line != '':
            print(line.strip()) # programming is fun \n -> 불용어 없애기
            # .strip(): 문장 끝 \n 혹은 공백 처리
        else: # EOF
            print("EOF")
            break # 반복 종료
    file4.close()
    
    # 6. readlines: 여러 줄 읽기 (리스트 형태로 반환)
    file5=open('ftest.txt',mode='r')
    lines=file5.readlines()
    print('lines :',lines)
    '''
    lines : ['programming is fun\n', 'very fun!\n', 'have a good time\n', 'mouse is input device\n', 'keyboard is input device\n', 'computer is input output system']
    '''
    print('문장 길이 :',len(lines)) # 문장 길이: 6
    for line in lines:
        print(line.strip()) # 끝문장 불용어(\n, 공백, 특수문자)
    file5.close()
    
    # 7. with문 이용 파일 입출력
    with open('ftest.txt',mode='r') as file6: # 파일 객체를 파일변수에 입력
        print(file.read())
    # 별도 종료 필요 없음 = file.close() 생략 -> 블록 벗어나면 자동으로 객체 소멸
    
    
except Exception as e:
    print('Error 발생 : ', e)
    # Error 발생 :  [WinError 2] 지정된 파일을 찾을 수 없습니다: 'C:\\work\\Crystal\\DataAnalysis\\[ITWILL]BigDataAnalysis_ExpertTraining\\04. Python Basic\\workspace\\chap08_FileIO\\date'

## MyCode
file_m=open('ftest.txt',mode='r')
for i in file_m:
    print(i.strip())