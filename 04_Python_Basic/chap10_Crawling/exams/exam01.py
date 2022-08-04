'''
 문) login.html 웹 문서를 대상으로 다음 조건에 맞게 내용을 추출하시오. 
    조건> <tr> 태그 하위 태그인 <th> 태그의 모든 내용 출력
    
   <출력 결과>
   th 태그 내용 
    아이디 
    비밀번호 
'''

from bs4 import BeautifulSoup

path = 'C:\\work\\Crystal\\DataAnalysis\\[ITWILL]BigDataAnalysis_ExpertTraining\\04. Python Basic\\workspace\\chap10_Crawling\\data'

# 1. 파일 읽기 
file = open(path + "/login.html", mode='r', encoding='utf-8')
source = file.read()

# 2. html 파싱
soup=BeautifulSoup(source,'html.parser')

# 3. 태그 찾기 
trFind=soup.find_all('tr')
thFind=[]
for tr in trFind:
    th=tr.find_all('th')
    thFind.extend(th)

# 4. 태그 내용 출력 
print('th 태그 내용')
for th in thFind:
    print(th.string)