# chap03_DataO_String

# 1. 입력: 데이터 불러오기

# 1) 키보드 일력: 소량의 자료
num = scan() # 숫자 입력
num

sum(num) # [1] 10 20 30

# what = double(): 실수형, character(): 문자형 (기본: double 숫자형)
names = scan(what=character()) # 문자 입력
names # 벡터 형태로 저장 # "홍길동" "이순신" "유관순"
names[3]

# 단어를 문장으로 만들기
names_sent = paste(names,collapse=",") # collapse = "구분자"
names_sent

# 2) 파일 불러오기: 대량의 자료
# - 컬럼 단위 구분: csv, excel
# - 형식: read.XXXX(파일)

getwd()
setwd("E:/")
setwd("E:/03. R/data")

# (1) read.table(): 컬럼 구분자가 콤마가 아닌 공복 혹은 특수문자일 때

# 칼럼명이 없는 경우
st1 = read.table(file = 'student.txt',header=FALSE,sep="")
st1

# 칼럼명이 있는 경우
st2 = read.table('student1.txt',header=T,sep="") # 칼럼명을 지정하지 않으면 칼럼명 행도 자료값으로 인식
st2

# 구분자: 특수문자
st3 = read.table('student2.txt',header=TRUE,sep=";")
# 제목행이 깨짐 -> 인코딩 방식이 다르기 때문
st3

# (2) read.csv(): 컬럼 구분자가 콤마일 때
st4 = read.csv('student4.txt') # header = TRUE와 sep="," 생략 가능능
st4
str(st4)
class(st4) # 대부분의 파일은 data.frame
# 만일 특수문자(-) 등이 있으면 숫자형이 있더라도 문자형으로 인식 -> 통계 계산 불가능
# 따라서, 특수문자(-)를 NA로 처리하면 숫자형은 숫자형으로 인식
st4 = read.csv('student4.txt',na.strings="-") # 특수문자가 여러개인 경우 벡테 c()로 묶기
st4
str(st4)
mean(st4$키) # NA # 그러나, NA 결측치가 있으면 통계 함수 계산 불가능
mean(st4$'키',na.rm=TRUE) # 177,6667 # 결측치 제외하고 계산
# 컬럼명이 한글인 경우 홑따옴표 붙이기: '한글컬럼명'
mean(st4$'몸무게',na.rm=TRUE) # 73.33333

# 탐색기 제공: 사용자가 직접 파일 선택
test = read.csv(file=file.choose())
test
head(test) # 앞의 6행 조회
tail(test) # 뒤의 6행 조회

# (3) read.xlsx()
# 엑셀은 별도의 패키지 설치 필요: 기본 패키지로는 읽어올 수 없음
# install.packages("readxl") # 파일 설치 후, 주석 처리하기 (중복 설치 없애기 위해)
library(readxl)

st_excel = read_excel('student_ex.xlsx') # excel 파일 # sheet가 여러개면 첫번째 sheet만 읽어옴
st_excel # header = TRUE (기본)
getwd()
read_excel('E:/03. R/output/stu_2sheet_ex.xlsx') # sheet1만 출력
read_excel('E:/03. R/output/stu_2sheet_ex.xlsx',sheet=2)
# sheet="시트명": 특정 시트 선택

## 추가
install.packages('xlsx') # rJava 자동 설치
Sys.setenv(JAVA_HOME='C:\\Program Files\\Java\\jre1.8.0_31')
library(xlsx)
read.xlsx('E:/03. R/output/stu_2sheet_ex.xlsx',sheetName='Sheet1')

# 3) 인터넷 파일 불러오기
# 데이터 셋 제공 사이트 
# http://www.public.iastate.edu/~hofmann/data_in_r_sortable.html - Datasets in R packages
# https://vincentarelbundock.github.io/Rdatasets/datasets.html
# https://vincentarelbundock.github.io/Rdatasets/csv/COUNT/titanic.csv
# https://r-dir.com/reference/datasets.html - Dataset site
# http://www.rdatamining.com/resources/data

titanic = read.csv('https://vincentarelbundock.github.io/Rdatasets/csv/COUNT/titanic.csv')
titanic
str(titanic)
# 'data.frame':	1316 obs. of  5 variables:
# $ X       : int  1 2 3 4 5 6 7 8 9 10 ... # 순번: 일련번호 (전체 행 길이로 확인 가능)
# $ class   : chr  "1st class" "1st class" "1st class" "1st class" ... # 몇 등석 (범주형 변수)
# $ age     : chr  "adults" "adults" "adults" "adults" ... # 어른과 아이 구분 (범주형)
# $ sex     : chr  "man" "man" "man" "man" ... # 여자 와 남자 (범주형)
# $ survived: chr  "yes" "yes" "yes" "yes" ... # 생존과 사망 (범주형)

# 범주형 변수의 빈도수 확인
table(titanic$sex) 
# man women 
# 869   447 
tab_sur = table(titanic$survived) # 생존 유무무
# no yes 
# 817 499 

# 범주형 빈도수 비율 확인
prop.table(table(titanic$sex))
# man     women 
# 0.6603343 0.3396657 
prop.table(tab_sur) # 사망/생존 비율
# no       yes 
# 0.6208207 0.3791793 

# 교차분할표: 두 테이블 간 관련성 확인 가능
table(titanic$sex,titanic$survived) # table(행,열)
#        no yes
# man   694 175 = 869
# women 123 324 = 447
175 / (694 + 175) # 남성 생존 비율: 0.20
324 / (123 + 324) # 여성 생존 비율: 0.72


# 2. 출력: 데이터 저장하기
# 불러온 데이터는 메모리 상에 존재: 휘발성이기 때문에 R Studio 종료 시 삭제됨
# 따라서, 지속적으로 데이터를 사용하기 위해 저장 필요

# 1) 화면 출력
print(titanic)
titanic # 흔히 print 생략 가능
print(175 / (694 + 175)) # 0.20

print('남성의 생존 비율 =',175 / (694 + 175)) # 변수만, 혹은 수식만 가능하나 콤마(,)를 이용하여 여러개 출력 불가능

# 문자열 + 상수 + 수식 결합하여 결과 출력할 경우,
cat('남성의 생존 비율 =', 175 / (694 + 175))

# 2) 파일에 데이터 저장하기
# read.table() -> write.table(): 구분자(공백, 특수문자)
# read.csv() -> write.csv(): 구분자(콤마)
# read_excel() -> write_excel(): 패키지 설치 필요

# (1) write.csv()
getwd() # "D:/03. R/data"
titanic_df = subset(titanic,select=c(class,age,survived))
write.csv(titanic_df,file="D:/03. R/output/titanic_df.csv",
          row.names=T,quote=F)

# (2) write_excel(): 패키지 설치
# install.packages('writexl')
library(writexl)

write_xlsx(st_excel,path="D:/03. R/output/student.xlsx")

## 추가
write.xlsx(st_excel,"E:/03. R/output/student.xlsx")

# 3.문자열 처리 & 정규표현식
# 정규표현식: 메타 문자 등을 이용하여 패턴을 지정하는 표현식
# 메타 문자: 패턴을 지정하는 약속된 특수기호(., [], {} 등)

# 1) stringr 패키지: 함수
install.packages("stringr")
library(stringr)
library(help='stringr')

# str_extract(string,pattern)
str_extract_all('#$%#342$*@gf4d%ds*##235s@##$','[0-9]{3}')
# [[1]] -> key
# [1] "342" "235" -> value

# (1) 문자열 길이
length(string) # 단어 개수: 1
str_length(sring) # 문자열 길이: 28

# (2) 문자열 교체: str_replace(문자열,패턴,교차할내용)
str_replace_all(string,'[0-9]{2}','') # 숫자 제거
str_rep = str_replace_all(string,'[0-9]{2}',',') # ,로 교체

# (3) 형태소(단어)화 = 문자열 분리: split
names = str_split(str_rep,',') # 토큰(단어) 생성
names = unlist(names)
names = names[1:5]
names

# (4) 문장화 = 토큰(단어) 결합 -> 문장: join
sents = str_c(names,collapse=' ')
sents # [1] "Hong lee kang 유관순 이사부"
sents_join = str_join(names,collapse=' ')

# (5) 부분 문자열: str_sub(string,start,end) 
str_sub(string,7,9) # lee

# (6) 문자열 위치 출력
str_locate_all(string,'[0-9]{2}')

# 2) 정규표현식을 이용한 패턴 지정 (원하는 문자열만 추출)

string = "Hong35lee45kang25유관순25이사부35"

# (1) 반복 관련 메타 문자
# [x]: x 중 1개 일치 (x는 범위가 될 수 있음)
# {n}: n개 연속인 경우 의미 (생략 시 기본: {1})

## (1) 숫자 추출
str_extract_all(string,'[0-9].')
ages = str_extract_all(string,'[0-9]{2}')
ages = str_extract_all(string,'\\d{2}')
ages
# [[1]] -> key
# [1] "35" "45" "23" "23" "35" -> value
ages = ages[[1]] # 리스트 결과를 벡터로 넘기기
ages # 값만 반환
# [1] "35" "45" "23" "23" "35"

# 문자형 -> 숫자형 변환
ages_num = as.numeric(ages)
mean(ages_num) # 33

## (2) 영문자 추출
enames = str_extract_all(string,'[A-z]{3}') # 문자열이 잘려서 추출 # "hon" "lee"  "kan"
enames = str_extract_all(string,'[A-z]{3,}') # 문자열이 3개 이상인 것 추출 # "hong" "lee"  "kang"
enames = str_extract_all(string,'[A-z]{3,4}') # 문자열이 3개 이상 4개 이하인 것 추출 # "hong" "lee"  "kang"
enames

## (3) 국문자 추출
knames = str_extract_all(string,'[가-힣]{3,}') # 문자열이 3개 이상인 것 추출
knames # [1] "유관순" "이사부"

# 추출된 자료형 list
class(knames)
# 만일 리스트를 벡터로 변화
nknames = unlist(knames)
nknames

# (2) 접두어/접미어 메타문자: ^, $
# ^: 접두어
# $: 접미어
# 특정 규칙이 있어야 하는 경우, 형식 지정
email = "kpjiku@naver.com" # email 형식: 아이디@호스트명(포털사이트명).최상위도메인명
email2 = "2hihello3d@google.com" # 잘못된 email
email3 = "hihello3d@google.co.kr"

str_extract(email,"^[A-z]\\w{3,}@[A-z]\\w{3,}.com$") # 반드시 영문자로 시작 com으로 마무리 되어야 함 의미
# 첫문자 영문자이며 단어가 3개 이상의 조합으로 이루어져야 함을 의미
# \\w: 단어(숫자,영문자,숫자 의미) 메타문자
# \\w{n}: n개의 단어
# \\d{n}: n개의 숫자 (숫자 메타문자) = [0-9]

str_extract(email2,"^[A-z]\\w{3,}@[A-z]\\w{3,}.com$") # NA
str_extract(email3,"^[A-z]\\w{3,}@[A-z]\\w{3,}.com$") # NA

# 둘 중 하나로 끝나는 경우 허용
str_extract(email3,"^[A-z]\\w{3,}@[A-z]\\w{3,}.(co.kr$|com$)")
# 만일, str_extract_all로 끝나는 경우, 없으면 NA가 아닌 character(0) 일치되는 것 없음으로 나옴


# (3) 부정 메타문자: [^x]
str_extract_all(string,"[^0-9]{3,}") # 숫자 제외