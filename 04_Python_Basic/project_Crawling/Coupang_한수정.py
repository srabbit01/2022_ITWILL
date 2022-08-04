"""
COUPANG_한수정.py

목적: 입력 받은 카테고리 내 1위 ~ 59위 물품 정보 크롤링
"""

## 1. 패키지/모듈 로딩

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import pandas as pd # DataFrame
import datetime # Today Date
import pymysql
import re

## 2. 기본 세팅

# 1) url 추출 함수 생성
def get_url(url):
    url_req=urlopen(Request(url,headers={'User-Agent': 'Mozilla/5.0'})) # 열기
    url_read=url_req.read() # 읽기
    url_decode=url_read.decode("utf-8") # 디코딩
    soup=BeautifulSoup(url_decode,'html.parser') # 파싱
    return soup

# 2) csv 파일 경로 지정
path = 'C:\\work\\Crystal\\DataAnalysis\\[ITWILL]BigDataAnalysis_ExpertTraining\\04. Python Basic\\workspace\\project_Crawling'

# 3) 오늘 날짜
today=str(datetime.date.today()).replace('-','')

# 4) DB 연동 환경변수 생성 
config = {
    'host' : '127.0.0.1',
    'user' : 'scott',
    'password' : 'tiger',
    'database' : 'work',
    'port' : 3306,
    'charset':'utf8',
    'use_unicode' : True}

## 3. 카테고리 번호 입력 받기
cate=int(input('''
1. 여성패션     2. 남성 패션       3. 뷰티           4. 출산/유아동
5. 식품         6. 주방용품       7. 생활용품        8. 홈인테리어 
9. 가전디지털   10. 스포츠/레저   11. 자동차용품     12. 도서/음반/DVD
13. 완구/취미   14. 문구/오피스   15. 반려동물용품   16. 헬스/건강식품
원하는 카테고리 번호를 입력하시오. '''))

## 4. 지정한 카테고리 href 추출
url = 'https://www.coupang.com/'

# 1) url 추출
soup=get_url(url)

# 2) href 추출
get_cate=soup.find("div",id="gnbAnalytics")
get_cate2=get_cate.select("ul[class='menu shopping-menu-list'] > li")
if cate==1: # 1. 여성패션
    href=get_cate2[0].select("ul > li[class='second-depth-list'] > a")
    href=href[0].get('href')
elif cate==2: # 2. 남성패션
    href=get_cate2[0].select("ul > li[class='second-depth-list'] > a")
    href=href[1].get('href')
else: # 패션 외 카테고리
    href=get_cate2[cate-2].select_one("a").get('href')
tot_href='https://www.coupang.com'+href

## 5. 지정한 카테고리 내 top 60 상품 정보 추출
# 추출할 정보: 이름, 원가, 판매가, 도착 예정일, 평점

# 1) url 추출
soup=get_url(tot_href)

# 2) top 59 상품 정보 추출
get_product=soup.find("ul",id="productList")
get_product2=get_product.find_all("li","baby-product renew-badge")
# 각 정보별 리스트 생성
rank=list(range(1,60))
name=[]
first_price=[]
sale_price=[]
arr_date=[]
rating=[]
# top 59 상품별 정보 리스트에 입력
for g in get_product2:
    info=g.find('dd','descriptions')
    name.append(info.find('div','name').string.strip()) # 상표명
    sp=info.find('strong','price-value').string.strip() # 판매가
    sale_price.append(sp)
    try:
        first_price.append(info.find('del','base-price').string.strip()) # 원가
    except:
        first_price.append(sp) # 원가 = 판매가
    arr_date.append(info.find('span','arrival-info emphasis').find_all('em')[0].string.strip()) # 도착 예정일
    rating.append(info.find('em','rating').string.strip()) # 평점

# 데이터 정제
first_price2=[int(i.replace(',','')) for i in first_price]
sale_price2=[int(i.replace(',','')) for i in sale_price]
arr_date2=[re.findall('\d{1,3}/\d+$',i)[0] for i in arr_date] # 날짜만 추출

# 3) 추출한 정보별 리스트 -> 전체 딕셔너리
pro_info={'순위':rank,'상품명':name,'원가':first_price2,'판매가':sale_price2,'도착 예정일':arr_date2,'평점':rating2}

## 6. 추출한 정보 csv 파일 저장

# 1) 이름 생성
SaveName='Coupang_Product'+str(cate)+'_'+today

# 2) 데이터프레임 생성
DF=pd.DataFrame(pro_info)

# 3) csv 파일 저장: CouPang_product_오늘날짜.csv
DF.to_csv(path+'/'+SaveName+'.csv',index=False,encoding='utf-8')

## 7. 추출한 정보 DB 테이블 저장

try :
    
    # 1) db 연동 객체 생성 
    conn = pymysql.connect(**config)
    
    # 2) sql문 실행 객체 
    cursor = conn.cursor()
    
    # 3) 테이블 생성
    cursor.execute(f"""
    create or replace table {SaveName}(
        Rank int auto_increment primary key,
        ProductName varchar(100) not null,
        FirsePrice int default 0,
        SalePrice int not null,
        ArrivalDate varchar(20) not null,
        Rating float(10));""") 
    
    # 4) 레코드 추가
    file=pd.read_csv(path+'/'+SaveName+'.csv',encoding='utf-8')
    for i in range(59): # 1위 ~ 59위
        Iquery=f"""INSERT INTO {SaveName}
            VALUES ({file.iloc[i,0]},'{file.iloc[i,1]}',{file.iloc[i,2]},{file.iloc[i,3]},'{file.iloc[i,4]}',{file.iloc[i,5]})"""
        cursor.execute(Iquery) # 레코드 추가
        conn.commit() # db 반영   
    
    # 5) 테이블 검색
    cursor.execute(f'select * from {SaveName}')    
    datas=cursor.fetchall()
    print(datas)

except Exception as e :
    print('db error :', e)
    conn.rollback()
    
finally :
    cursor.close(); conn.close()