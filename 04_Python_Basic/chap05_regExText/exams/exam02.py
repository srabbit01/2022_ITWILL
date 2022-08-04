'''
문2) 다음과 같은 여러 줄의 문자열을 대상으로 정규표현식을
       적용하여 email 양식이 올바른 것만 출력되도록 하시오. 

   email 형식 : 아이디@호스트이름.최상위도메인 
     
  <email 패턴 조건>         
        아이디 : 첫자는 영문소문자(^[a-z]), 단어길이 3자 이상(\w{3,})
        호스트이름 : 영문소문자 시작([a-z]), 단어길이 2자 이상(\w{2,})
        최상위 도메인 : 영문소문자 3자리 이하([a-z]{3})
        
  << 출력 결과 >>
  you2@naver.com
  kimjs@gmail.com
'''

from re import match # match 함수 이용 

email = """hong@12.com
you2@naver.com
12kang@hanmail.net
kimjs@gmail.com"""

email=email.split('\n')

for i in email:
    mat=match('^[a-z]\w{3,}@[a-z]\w{2,}\.[a-z]{3}$',i)
    if mat:
        print(i)