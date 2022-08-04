# chap07_2_InFormal

######################################
## 1. 패키지 설치와 준비 
######################################

# 1) KoNLP 설치 
install.packages("KoNLP") # 오류 발생 : 최신 버전에서 패키지 사용 불가 
#Warning in install.packages :
#  package ‘KoNLP’ is not available for this version of R

# [오류 해결방법]
# - 현재 R 버전에서 제공하지 않는 패키지(KoNLP) 설치 방법
# - 현재 버전에서 사용 KoNLP 사용이 불가능하기 때문에 R 버전 낮춰서 재설치

# [단계1] Rstudio 종료 


# [단계2] R 3.6.3 버전 다운로드 & 설치 : KoNLP 사용 버전  
# https://cran.r-project.org/bin/windows/base/old/
# 위 사이트 접속 후 'R 3.6.3 (February, 2020)' 클릭


# [단계3] Rstudio 실행 & R 버전 확인 
# 메뉴 [Tools] -> [Global Options] -> [General] 탭에서
#      R version : 64-bit R-3.6.3  변경 -> RStudion 재시작 


# [단계4] 이전 R 버전에서 kONLP 설치 
install.packages("https://cran.rstudio.com/bin/windows/contrib/3.4/KoNLP_0.80.1.zip",
                 repos = NULL) # 패키지 강제 설치
# 압축 파일 다운로드 및 풀어서 설치
# repos = NULL : 3.4버전을 현재 사용중인 3.6버전에 설치
# 버전이 다르기 때문에 같은 위치에 함께 패키지 저장하기 위해


# 2) Sejong 설치 : KoNLP와 의존성 있는 Sejong 설치 
# 세종 사전 설치: 3.6 버전에서 자체적으로 제공
# 형태소 분석에 사용됨: 전체적 관리는 (KoNLP가 관리)
install.packages("Sejong")  # 세종 사전 제공: 형태소 분석 이용
# 품사를 기준으로 문장에서 단어 추출 = 형태소 분석

# 3) wordcloud 설치    
# 단어 구름 시각화 패키지
install.packages("wordcloud")   

# 4) tm 설치 
# 텍스트 마이닝: 전처리 함수 제공
# 특수문자, 불용어 등 제거
install.packages("tm") 

# 5) 설치 위치 확인 
.libPaths()
# [1] "C:/Users/srabb/Documents/R/win-library/3.6": 사용자 패키지 설치 경로
# [2] "C:/Program Files/R/R-3.6.3/library": 30개의 기본 패키지 설치 경로

# 6) KoNLP 의존성 패키지 모두 설치 & 로드 
install.packages(c('hash','rJava','tau','RSQLite','devtools')) # 패키지 설치 
# devtools: 정상 설치되지 않음

library(hash)
Sys.setenv(JAVA_HOME='C:/Program Files/Java/jdk1.8.0_151') # jdk 경로 # 자바의 홈 디렉토리 지정 (RJava 때문)
library(rJava)
library(tau)
library(RSQLite) # 경로 없이 자동 설치

# ‘devtools’이라고 불리는 패키지가 없습니다
# devtools는 강제 설치 필요: 특정 사이트에서 다운 받아 설치
# Error 해결방법: devtools_2.4.1.zip 수동 설치
install.packages("https://cran.rstudio.com/bin/windows/contrib/3.6/devtools_2.4.1.zip",
                 repos = NULL) # 패키지 강제 수동 설치로 해결

# Error in library(sessioninfo) : 
# ‘sessioninfo’이라고 불리는 패키지가 없습니다
# 해결방법: sessioninfo_1.1.1.zip 수동설치
install.packages("https://cran.rstudio.com/bin/windows/contrib/3.6/sessioninfo_1.1.1.zip",
                 repos = NULL)

library(devtools) # 로딩 성공

# 7) KoNLP 패키지 로딩
library(KoNLP) # 로딩 성공

library(tm) # 전처리 용도

library(wordcloud) # 단어 구름 시각화 


##################################################
# 1. 토픽분석(텍스트 마이닝) 
# - 시각화 : 단어 빈도수에 따른 워드 클라우드
###################################################


# 단계1 :  facebook_bigdata.txt 가져오기
facebook <- file(file.choose(), encoding="UTF-8")
facebook_data <- readLines(facebook) # 줄 단위 읽기 
str(facebook_data) # chr [1:76]
facebook_data[1:6] # 앞부분 6문장 확인 


# 단계2 : 세종 사전에 신규 단어 추가
# term='추가단어', tag=ncn(명사지시코드)
# tag='품사' (품사마다 지시코드 다름)
user_dic <- data.frame(term=c("R 프로그래밍","페이스북","김진성","소셜네트워크"), tag='ncn')

# Sejong 사전에 신규 단어 추가 : KoNLP 제공 
buildDictionary(ext_dic='sejong', user_dic = user_dic)
# 중간에 발생하는 오류 메세지 무시 가능
# 성공: 370961 words dictionary was built.

# 신규 단어는 휘발성:실행할 때마다 매번 추가해야 함 (끝내면 사라짐) -> 저장되지 않음

# 명사 추출: KoNLP 패키지 함수
# 간단한 형태소 분석
extractNoun('김진성은 많은 사람과 소통을 위해서 소셜네트워크에 가입하였습니다.') # 세종 사전의 명사로 등록된 것만 추출
# [1] "김진성"       "사람"         "소통"         "소셜네트워크" "가입"   -> 5개 추출
# 명사가 아닌 동사, 부사 등 추출되지 않음


# 단계3 : 단어추출 사용자 함수 정의
# (1) Sejong 사전에 등록된 신규 단어 테스트    
paste(extractNoun('김진성은 많은 사람과 소통을 위해서 소셜네트워크에 가입하였습니다.'), collapse=" ")
# 각각의 단어들이 공백을 기준으로 하나의 문장으로 결합

# (2) 사용자 정의 함수 실행 순서 : 문자변환 -> 명사 단어추출 -> 공백으로 합침
exNouns <- function(x) { # x: 1개 문장
  paste(extractNoun(as.character(x)), collapse=" ") # 
}

# (3) exNouns 함수 이용 단어 추출 
# 형식) sapply(vector, 함수) -> 76개 vector 문장(원소)에서 단어 추출 
# 76개의 문장이 한문장씩 exNouns 함수에 입력되어 함수 실행
facebook_nouns <- sapply(facebook_data, exNouns) 

# (4) 단어 추출 결과
str(facebook_nouns) # [1:76] attr(*, 'names')=ch [1:76] 
facebook_nouns[1] # vector names:원본문장(윗문장), vector:단어 추출(아랫문장)
# 위: 벡터의 이름 # 아래: 함수의 반환된 내용(벡터)
# 영문은 그대로 추출 (사전에 등록되지 않아도 영어는 단어로 추출)
# 한글만 대상으로 형태소 분석이 이루어짐
facebook_nouns[2]
length(facebook_nouns) # 76: 76의 원본과 함수에 의해 반환된 단어의 묶음 존재 (단어 묶음(모음): 문장은 아니며, 공백으로 하나 묶음으로 됨)
# 음절 '만'도 단어(명사)로 인식


# 단계4 : 자료 전처리: tm 패키지 사용
# tm 용도: 전처리 용도 -> 명사를 대상으로 어떤 단어가 얼마나 나왔는지 확인
# 숫자, 문자부호 등을 제거

# (1) 말뭉치(코퍼스:Corpus) 생성 : 자연어 처리를 위한 문자(텍스트) 집합 
# tm에서 전처리를 위해 반드시 말뭉치 생성해야 함
# VectorSource(): 벡터를 말뭉치(Corpus) 생성을 위한 소스로 전환
myCorpus <- Corpus(VectorSource(facebook_nouns)) 
myCorpus # 객체의 내용이 아닌 정보 제공
# <<SimpleCorpus>>
# Metadata:  corpus specific: 1, document level (indexed): 0
# Content:  documents: 76 -> 76개의 말뭉치 생성 의미

# corpus 내용 보기
# insepct: tm 패키지 소속 함수
inspect(myCorpus[1])  
inspect(myCorpus[2])
inspect(myCorpus[76])


# (2) 자료 전처리 : 말뭉치 대상 전처리 
# tm_map()함수: 1:1로 묶음(사상시킴)
# 두번째 인수: tm 소속 함수를 이용하여 코퍼스 객체에 반영
myCorpusPrepro <- tm_map(myCorpus, removePunctuation) # 문장부호 제거
myCorpusPrepro <- tm_map(myCorpusPrepro, removeNumbers) # 수치 제거
myCorpusPrepro <- tm_map(myCorpusPrepro, tolower) # 영문자 대문자를 소문자로 변경
inspect(myCorpusPrepro[1])

# 영문 대상 불용어 제외 : stopwords()
stopwords('english') # 174개의 불용어 존재 (부사,전치사,접속사,대명사 등으로 구성)
# 특정 주어진 단어 제거: 영문에 불용어로 등록된 단어 제거
myCorpusPrepro <-tm_map(myCorpusPrepro, removeWords, stopwords('english')) # 불용어제거


# (3) 전처리 결과 확인 
myCorpusPrepro # Content:  documents: 76
inspect(myCorpusPrepro[1:3]) # 데이터 전처리 결과 문장 3개만 확인(숫자, 문장부호, 영문 상태 확인)


# 단계5 : 단어 선별(단어 길이 2개 이상)
# 2음절 이상 8음절 이하만 문자로 지정
# (1) 한글 단어길이 2음절 ~ 8음절(한글 1개 2byte) 
# TermDocumentMatrix(): 단어 문자 행렬 생성 함수 -> 값으로는 해당 문장에서 단어 출현 빈도수
# 예시: n번째 문장에서 특정 단어 몇번 출현?
# Term: 단어, Document: 문서, Matrix: 행렬 -> 단어를 행, 문장을 열로 만든 행렬
myCorpusPrepro_term <- TermDocumentMatrix(myCorpusPrepro, 
                                          control=list(wordLengths=c(4,16))) 
# control=c(최소byte,최대byte): 단어의 길이 설정 
# 한글의 음절은 2byte를 차지하기 때문에 2배로 곱해서 지정

myCorpusPrepro_term # 단어 vs 문서 행렬 -> 내용이 아닌 객체 정보 확인 가능
# <<TermDocumentMatrix (terms: 696, documents: 76)>> # 696개 단어(행) 76개 문장(열) -> cell의 개수: 696*16개
# Non-/sparse entries: 1256/51640: 실제 단어 출현 빈도셀수(단어출현빈도셀)/비어 있는 셀 수(희소빈도셀) -> 대부분 cell은 0
# Sparsity           : 98% : 희소 비율 -> 2%는 단어 출현, 나머지 98% 비어있는 cell
# Maximal term length: 12 : 한글 6음절이 최대 길이를 가진 단어 (가장 음절이 긴 단어는 6음절)
# Weighting          : term frequency (tf) -> 가중치: 셀에 표시된 값
# 희소 행렬: Sparse Matrix

1256/51640 # 0.02432223

# (2) Corpus -> 평서문 변환 : matrix -> data.frame 변경
# 행렬
myTerm_df <- as.data.frame(as.matrix(myCorpusPrepro_term)) 
dim(myTerm_df) 
head(myTerm_df[1])


# 단계6 : 단어 빈도수 구하기
# (1) 단어 빈도수 내림차순 정렬
wordResult <- sort(rowSums(myTerm_df), decreasing=TRUE) 
# rowSums() 함수: 행단위 합계 -> 전체 문서에서 단어가 몇번 출현했는지 확인 가능: 전체 출현비도수 확인 가능
wordResult[1:10] # top10 단어  

# (2) 불용어 제거 
# 특정 문자 제거
myStopwords = c(stopwords('english'), "사용","얘기"); # 제거할 문자 추가
# 불용어 처리는 코퍼스 객체로 했었음 -> 
# tm_map(변수,removeWords,제거변수) -> removeWords: 제거함수
myCorpusPrepro <-tm_map(myCorpusPrepro, removeWords, myStopwords) # 불용어제거

# (3) 단어 선별과 평서문 변환
myCorpusPrepro_term <- TermDocumentMatrix(myCorpusPrepro, 
                                          control=list(wordLengths=c(4,16))) # 2음절 ~ 8음절

# (4) 말뭉치 객체를 평서문으로 변환
myTerm_df <- as.data.frame(as.matrix(myCorpusPrepro_term)) 

#(5) 단어 출현 빈도수 구하기
wordResult <- sort(rowSums(myTerm_df), decreasing=TRUE) 
wordResult[1:10]


# 단계7 : 단어구름에 디자인 적용(빈도수, 색상, 랜덤, 회전 등)
# (1) 단어 이름 생성 -> 빈도수의 이름
myName <- names(wordResult)  

# (2) 단어이름과 빈도수로 data.frame 생성
word.df <- data.frame(word=myName, freq=wordResult) 
str(word.df) # word, freq 변수
head(word.df)

# (3) 단어 색상과 글꼴 지정
pal <- brewer.pal(12,"Paired") # 12가지 색상 pal <- brewer.pal(9,"Set1") # Set1~ Set3
# 폰트 설정세팅 : "맑은 고딕", "서울남산체 B"
windowsFonts(malgun=windowsFont("맑은 고딕"))  #windows

# (4) 단어 구름 시각화: 크기,최소빈도수,순서,회전,색상,글꼴 지정  
wordcloud(word.df$word, word.df$freq, # 단어이름,빈도수
          scale=c(3,1), min.freq=2, random.order=F, #화면크기,출현빈도 2회이상,순서랜덤아님
          rot.per=.1, colors=pal, family="malgun") # 색상,글꼴맑은고딕
# 빈도수가 높을 수록 중앙에 글씨크기 크게 출력

# 단계8 : 차트 시각화  
#(1) 상위 10개 토픽추출
topWord <- head(sort(wordResult, decreasing=T), 10) # 상위 10개 토픽추출 
# (2) 파일 차트 생성 
pie(topWord, col=rainbow(10), radius=1) 
# radius=1 : 반지름 지정 - 확대 기능  

# (3) 빈도수 백분율 적용 
pct <- round(topWord/sum(topWord)*100, 1) # 백분율

# (4) 단어와 백분율 하나로 합친다.
label <- paste(names(topWord), "\n", pct, "%")

# (5) 파이차트에 단어와 백분율을 레이블로 적용 
pie(topWord, main="SNS 빅데이터 관련 토픽분석", 
    col=rainbow(10), cex=0.8, labels=label)


###########################################
# 단계2 - 연관어 분석(단어와 단어 사이 연관성 분석) 
#   - 시각화 : 연관어 네트워크 시각화,
###########################################

# 한글 처리를 위한 패키지 설치
Sys.setenv(JAVA_HOME='C:\\Program Files\\Java\\jre1.8.0_151')
library(rJava) # 아래와 같은 Error 발생 시 Sys.setenv()함수로 java 경로 지정
library(KoNLP) # rJava 라이브러리가 필요함

#----------------------------------------------------
# 1.텍스트 파일 가져오기
#----------------------------------------------------

marketing <- file(choose.files(), encoding="UTF-8") # marketing.txt 불러오기
marketing2 <- readLines(marketing) # 줄 단위 데이터 생성
close(marketing) # 객체 닫기
head(marketing2) # 앞부분 6줄 보기 - 줄 단위 문장 확인 
str(marketing2) # chr [1:472] -> 472개의 데이터 존재
marketing2[1:5]

#----------------------------------------------------
# 2. 줄 단위 단어 추출
#----------------------------------------------------
# Map()함수 이용 줄 단위 단어 추출 
lword <- Map(extractNoun, marketing2) # list로 반환
# sapply와 같이 뒤 변수를 각 원소 별로 함수에 입력
# key: 문장, value: 단어
length(lword) # [1] 472
class(lword) # list: 자료구조 리스트로 추출
lword[1] # 33개 단어
lword[472] # 180개 단어

# 중복 문장 제거
lword <- unique(lword)
length(lword) # [1] 353(119개 제거)

# 중복 단어 제거
# 전체 문장 기준 중복되는 단어 있으면 제거
lword <- sapply(lword, unique) # 중복 문장 제거
length(lword) 
class(lword)
lword[1]
lword[330]

################################
# list 처리 함수: unqiue, sapply
################################
lst=list(a=c(1,2,1),b=c(2,3,2),a=c(2,3,2))
lst
unique(lst) # 중복 key(문장) 제거 -> 리스트 반환
# [[1]]
# [1] 1 2 1
# [[2]]
# [1] 2 3 2

sapply(lst,unique) # 각 벡터 별로 중복된 단어 제거 -> 행렬 반환
#      a b a
# [1,] 1 2 2
# [2,] 2 3 3

#----------------------------------------------------
# 3. 전처리
#----------------------------------------------------
# 1) 단어 길이 2음절~4음절 단어 필터링 함수 정의
filter1 <- function(x){
  nchar(x) <= 4 && nchar(x) >= 2 && is.hangul(x)
}
# &: 문장이 공백인 경우 Error 발생
# &&: 문장이 공백인 경우 character(0)
# &와 &&는 같으나, 공백 처리를 위해 필요

# &와 &&
c(TRUE,TRUE) & c(FALSE,FALSE) # 벡터 간의 연산
c(1,2) & c(1,3)

c(TRUE,TRUE) && c(TRUE,FALSE) # 한 개의 
c(1,2) && c(1,3)

# 2) Filter(f,x) -> filter1() 함수를 적용하여 x 벡터 단위 필터링 
filter2 <- function(x){
  Filter(filter1, x)
}
# is.hangul() : KoNLP 패키지 제공
# Filter(f, x) : base
# nchar() : base -> 문자 수 반환

# 3) 줄 단어 대상 필터링
lword_final <- sapply(lword, filter2)
lword_final # 전처리 단어확인(2~4음절) 


#----------------------------------------------
# 4. 트랜잭션 생성 : 연관분석을 위해서 단어를 트랜잭션으로 변환
#----------------------------------------------------
# 연관분석을 하기 위해 사용되는 객체
# arules 패키지 설치
install.packages("https://cran.rstudio.com/bin/windows/contrib/3.6/arules_1.6-7.zip",repos=NULL)
library(arules) 
#--------------------
# arules 패키지 제공 기능
# - Adult,Groceries 데이터 셋
# - as(),apriori(),inspect(),labels(),crossTable()=table()
#-------------------
# as(dataset, 'class') # 형변환 
wordtran <- as(lword_final, "transactions") # lword에 중복데이터가 있으면 error발생
wordtran 
# transaction in spase format with
# 353 transaction (rows) and = 문장수(거래수)
# 2424 items (columns) = 단어수(상품수)

# 트랜잭션 내용 보기 -> 각 트랜잭션의 단어 보기
inspect(wordtran)  

#----------------------------------------------------
# 5.단어 간 연관규칙 산출
#----------------------------------------------------
# 트랜잭션 데이터를 대상으로 지지도와 신뢰도를 적용하여 연관규칙 생성
# 형식) apriori(data, parameter = NULL, appearance = NULL, control = NULL)
tranrules <- apriori(wordtran, parameter=list(supp=0.25, conf=0.05)) 
tranrules # set of 59 rules
inspect(tranrules) # [59 rule(s)]
# lhs: 선행 조건 # rhs: 후행 조건
# { }: 조건이 없는 것
# 선행과 후행의 순서는 상관 없음

#----------------------------------------------------
# 6.연관어 시각화 
#----------------------------------------------------
# (1) 데이터 구조 변경 : 연관규칙 -> label 추출  
rules <- labels(tranrules, ruleSep=" ")  
rules 

# 문자열로 묶인 연관단어 -> 공백 기준 list 변경 
rules <- sapply(rules, strsplit, " ",  USE.NAMES=F) # list 변환  
rules

# list -> matrix 반환
rulemat <- do.call("rbind", rules)
rulemat
class(rulemat)

# (2) 연관어 시각화를 위한 igraph 패키지 설치
install.packages("igraph") # graph.edgelist(), plot.igraph(), closeness() 함수 제공
library(igraph)   

# (3) edgelist보기 - 연관단어를 정점 형태의 목록 제공 
ruleg <- graph.edgelist(rulemat[c(12:59),], directed=F) # [1,]~[11,] "{}" 제외
# 선행 후행 모두 있는 벡터만 시각화
ruleg

# (4) edgelist 시각화
X11() # 별도 창 제공 
plot.igraph(ruleg, vertex.label=V(ruleg)$name,
            vertex.label.cex=1.2, vertex.label.color='black', 
            vertex.size=20, vertex.color='green', vertex.frame.color='blue')

##################
# 후행사건: '경영'
##################
sub_rules=subset(tranrules,rhs %in% '경영') # 후행 사건이 경영인 것만 포함
inspect(sub_rules)

# 선행사건 기준
sub_rules=subset(tranrules,lhs %in% '경영') # 선행 사건에 '경영'이 있으면 전부 추출

# (1) 데이터 구조 변경 : 연관규칙 -> label 추출  
rules <- labels(sub_rules, ruleSep=" ")  
rules 

# 문자열로 묶인 연관단어 -> 공백 기준 list 변경 
rules <- sapply(rules, strsplit, " ",  USE.NAMES=F) # list 변환  
rules

# list -> matrix 반환
rulemat <- do.call("rbind", rules)
rulemat
class(rulemat)

# (2) edgelist보기 - 연관단어를 정점 형태의 목록 제공 
ruleg <- graph.edgelist(rulemat[c(2:14),], directed=F) # [1,]~[11,] "{}" 제외
# 선행 후행 모두 있는 벡터만 시각화
ruleg

# (3) edgelist 시각화
X11() # 별도 창 제공 
plot.igraph(ruleg, vertex.label=V(ruleg)$name,
            vertex.label.cex=1.2, vertex.label.color='black', 
            vertex.size=20, vertex.color='green', vertex.frame.color='blue')


#############################################
# 단계3 - 감성 분석(단어의 긍정/부정 분석) 
#  - 시각화 : 파랑/빨강 -> 불만고객 시각화
#############################################

# 1. 데이터 가져오기() 
# 1번째 컬럼: 회사 이름, 2번째 컬럼: 회사에 대한 평가
getwd()
setwd("E:/03. R/data")

data<-read.csv("reviews.csv") 
head(data,2)


# 2. 단어 사전에 단어추가

# 긍정어/부정어 영어 사전 가져오기
posDic <- readLines("posDic.txt") # 긍정어 사전
negDic <- readLines("negDic.txt") # 부정어 사전
# 새로운 단어 추가도 가능
length(posDic) # 2006
length(negDic) # 4783


# 긍정어/부정어 단어 추가 
posDic.final <-c(posDic, 'victor')
negDic.final <-c(negDic, 'vanquished')


# 3. 감성 분석 함수 정의-sentimental

# (1) 문자열 처리를 위한 패키지 로딩 
install.packages('plyr')
library(plyr) # laply()함수 제공
install.packages('stringr')
library(stringr) # str_split()함수 제공

# (2) 감성분석을 위한 함수 정의
sentimental = function(sentences, posDic, negDic){ # (문장,긍정사전,부정사전)
  
  scores = laply(sentences, function(sentence, posDic, negDic) {
    
    # 1. 문장 전처리
    sentence = gsub('[[:punct:]]', '', sentence) #문장부호 제거
    sentence = gsub('[[:cntrl:]]', '', sentence) #특수문자 제거
    sentence = gsub('\\d+', '', sentence) # 숫자 제거
    sentence = tolower(sentence) # 모두 소문자로 변경(단어가 모두 소문자 임)
    
    # 2. 문장 -> 단어(token): 영문자의 경우 공백을 기준으로 하나의 단어로 간주
    # 단어 구분자: 한 칸 이상의 공백
    word.list = str_split(sentence, '\\s+') # 공백 기준으로 단어 생성 -> \\s+ : 공백 정규식, +(1개 이상) 
    # 중복 단어 제거
    words = unlist(word.list) # unlist() : list를 vector 객체로 구조변경
    
    # 3. 단어(token) vs 사전 비교하여 긍정 단어에 해당하는지 부정 단어에 해당하는지 확인
    pos.matches = match(words, posDic) # words의 단어를 posDic에서 matching
    neg.matches = match(words, negDic) # 부정 단어 매칭
    # 등록되지 않은 단어는 둘 중 하나도 매칭되지 않기 때문에 결측치(NA)로 간주
    # 각각 긍정/부정에 매칭된 단어들의 벡터 생성
    
    pos.matches = !is.na(pos.matches) # NA 제거, 위치(숫자)만 추출
    neg.matches = !is.na(neg.matches)
    
    # 4. 점수=긍정어수-부정어수 (양수: 긍정 단어가 많음, 음수: 부정 단어가 많음으로 해석)
    score = sum(pos.matches) - sum(neg.matches) # 긍정 - 부정    
    return(score)
  }, posDic, negDic)
  
  scores.df = data.frame(score=scores, text=sentences) # 점수 반환 후 문장 반환
  return(scores.df)
}

# 4. 감성 분석 : 두번째 변수(review) 전체 레코드 대상 감성분석
result<-sentimental(data[,2], posDic.final, negDic.final)
result
head(result)
names(result) # "score" "text" 
dim(result) # 100   2
result$text
result$score # 100 줄 단위로 긍정어/부정어 사전을 적용한 점수 합계

# score값을 대상으로 color 칼럼 추가
result$color
result$color[result$score >=1] <- "blue"
result$color[result$score ==0] <- "green"
result$color[result$score < 0] <- "red"

# 감성분석 결과 차트보기
plot(result$score, col=result$color) # 산포도 색상적용
barplot(result$score, col=result$color, main ="감성분석 결과화면") # 막대차트


# 5. 단어의 긍정/부정 분석 

# (1) 감성분석 빈도수 
table(result$color)

# (2) score 칼럼 리코딩 
result$remark[result$score >=1] <- "긍정"
result$remark[result$score ==0] <- "중립"
result$remark[result$score < 0] <- "부정"

sentiment_result<- table(result$remark)
sentiment_result

# (3) 제목, 색상, 원크기
pie(sentiment_result, main="감성분석 결과", 
    col=c("blue","red","green"), radius=0.8) # ->  1.2
