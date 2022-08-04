#################################
## <제7장-2 연습문제>
################################# 


# 01. 오바마 연설문(obama.txt)을 대상으로 빈도수가 2회 이상 단어를 대상으로 단어구름 시각화하시오.
# [단계1], [단계4] ~ [단계8]

# 필요한 패키지 로딩 
library(tm) # 전처리 용도 
library(wordcloud) # 단어 구름 시각화 
# 별도의 패키지 없이 tm만 있으면 영문자 텍스트 마이닝 가능

# [단계1] 파일 가져오기 
obama <-file(file.choose())  # obama.txt
obama_data<-readLines(obama)
str(obama_data) # chr [1:496] -> 496개 문장 


# [단계4] 자료 전처리   
# (1) 말뭉치(코퍼스:Corpus) 생성 : 문장을 처리할 수 있는 자료의 집합 
myCorpus=Corpus(VectorSource(obama_data))
inspect(myCorpus[2])

# (2) 자료 전처리 : 말뭉치 대상 전처리 : tm_map(Corpus, Func)
myCorpusPrepro=tm_map(myCorpus, removePunctuation) # 문장부호 제거
myCorpusPrepro=tm_map(myCorpusPrepro, removeNumbers) # 수치 제거
myCorpusPrepro=tm_map(myCorpusPrepro, tolower) # 영문자 대문자를 소문자로 변경
remove_word=c(stopwords('english'),'thats','will','can','just')
myCorpusPrepro=tm_map(myCorpusPrepro, removeWords,remove_word) # 불용어제거

# (3) 전처리 결과 확인 
inspect(head(myCorpusPrepro))

# [단계5] 단어-문서 행렬(단어 길이 2개 ~ 16개 이상)
myCorpusPrepro_term=TermDocumentMatrix(myCorpusPrepro,
                                          control=list(wordLengths=c(2,16)))
myCorpusPrepro_term
myTerm_df=as.data.frame(as.matrix(myCorpusPrepro_term)) 
dim(myTerm_df) 
head(myTerm_df)
myTerm_df[1:10,100:150]

# [단계6] 단어 빈도수 구하기
wordResult=sort(rowSums(myTerm_df),decreasing=TRUE) 
wordResult[1:10]

# [단계7] 단어구름에 디자인 적용(빈도수, 색상, 랜덤, 회전 등)

word.df=data.frame(word=names(wordResult),freq=wordResult)
head(word.df)

pal=brewer.pal(12,"Set2")
windowsFonts(malgun=windowsFont("맑은 고딕"))

wordcloud(word.df$word, word.df$freq,
          scale=c(3,1), min.freq=2, random.order=F,
          rot.per=.1, colors=pal, family="malgun")


# [단계8] 차트 시각화 : 상위 10개 토픽추출
topWord=head(sort(wordResult, decreasing=T), 10)

pct=round(topWord/sum(topWord)*100, 1)

label=paste(names(topWord), "\n", pct, "%")

pie(topWord, main="오바마 대통령 연설 관련 토픽분석", 
    col=rainbow(10), cex=0.8, labels=label,radius=1)

# 02. 공공데이터 사이트에서 관심분야 데이터 셋을 다운로드 받아서 빈도수가 5회 이상 단어를 이용하여 
#      단어 구름으로 시각화 하시오.
# 공공데이터 사이트 : www.data.go.kr 또는 기타 사이트 

# 패키지 로딩
library(hash)
Sys.setenv(JAVA_HOME='C:/Program Files/Java/jdk1.8.0_151')
library(rJava)
library(tau)
library(RSQLite)
library(devtools)
library(KoNLP)
library(tm) 
library(wordcloud) 

# 데이터 불러오기
data=read.csv('data/NaverMovie_Cats.csv',header=F,encoding='ANSI', stringsAsFactors = F)
head(data)
data=data$V1
length(data)
str(data) # chr [1:5279]

# sejong 사전 단어 수 확인
buildDictionary(ext_dic='sejong')

# 명사 추출 확인
paste(extractNoun(data[1]),collapse=" ")

# 명사 추출 함수 생성
exNouns <- function(x) {
  paste(extractNoun(as.character(x)), collapse=" ")
}

# 데이터를 명사 추출 함수에 입력
data_nouns=sapply(data,exNouns) 

data_nouns[1]

# 말뭉치(코퍼스) 생성
myCorpus <- Corpus(VectorSource(data_nouns)) 
myCorpus
inspect(myCorpus[1])  

# 전처리 실행
myCorpusPrepro=tm_map(myCorpus, stripWhitespace)
myCorpusPrepro=tm_map(myCorpus, removePunctuation)
myCorpusPrepro=tm_map(myCorpusPrepro, removeNumbers)
myCorpusPrepro=tm_map(myCorpusPrepro, tolower)
remove_word=c(stopwords('english'),'진짜','중간','처음','하나','해서','들이','하게',
              '마지막')
myCorpusPrepro=tm_map(myCorpusPrepro, removeWords,remove_word)

inspect(head(myCorpusPrepro))

# 최소/최대 음절 지정
myCorpusPrepro_term=TermDocumentMatrix(myCorpusPrepro,
                                       control=list(wordLengths=c(4,16)))
myCorpusPrepro_term

# 말뭉치 -> 데이터프레임 전환
myTerm_df=as.data.frame(as.matrix(myCorpusPrepro_term)) 

# 출현 빈도수 오름차순 정렬
wordResult=sort(rowSums(myTerm_df),decreasing=TRUE) 
# 상위 1위 ~ 10위 단어 출력
wordResult[1:10]

# 단어구름 생성을 위한 데이터프레임 생성
word.df=data.frame(word=names(wordResult),freq=wordResult)
head(word.df)

# 단어구름 색상 지정
pal=brewer.pal(12,"Set2")
windowsFonts(malgun=windowsFont("맑은 고딕"))

# 단어구름 만들기
wordcloud(word.df$word, word.df$freq,
          scale=c(3,1), min.freq=2, random.order=F,
          rot.per=.1, colors=pal, family="malgun")

# 1위 ~ 10위 단어 출력
topWord=head(sort(wordResult, decreasing=T), 10)

pct=round(topWord/sum(topWord)*100, 1)

label=paste(names(topWord), "\n", pct, "%")

# 파이 차트 생성
pie(topWord, main="영화 'cat's' 토픽 분석", 
    col=rainbow(10), cex=0.8, labels=label,radius=1)