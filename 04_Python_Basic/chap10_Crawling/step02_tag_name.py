'''
1. tag 계층구조 찾기
2. find('tag')함수 찾기 
'''

from bs4 import BeautifulSoup

path = 'C:\\work\\Crystal\\DataAnalysis\\[ITWILL]BigDataAnalysis_ExpertTraining\\04. Python Basic\\workspace\\chap10_Crawling\\data'

# 1. 로컬 파일 읽기 
file = open(path + '/html01.html', mode='r', encoding='utf-8')
text_data = file.read() # 디코딩 생략
print(text_data)

# 2. html 파싱
html = BeautifulSoup(text_data, 'html.parser')
print(html)


# 3. 태그 내용 수집 
# 1) tag 계층 구조 찾기
h1=html.html.body.h1 # DOM 계층 구조
print(h1) # <h1> 시멘틱 태그 ?</h1>
print(h1.string) #  시멘틱 태그 ?

# 2) html.find('tag') 함수 찾기: 1개 태그 수정
h2=html.find('h2')
print(h2) # <h2> 주요 시멘틱 태그 </h2>
print(h2.string) # 주요 시멘틱 태그 

# 3) html.find_all('tag'): 여러 개 태그 수집
lis=html.find_all('li') # list 반환
print(lis)
len(lis) # 5

li_conts=[li.string for li in lis]
li_conts # 내용
