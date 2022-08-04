# chap06_1_DataHandling

################################################
# 1. dplyr 패키지 활용
################################################

# dplyr 패키지와 
install.packages("dplyr") # plyr 패키지 업그레이드 
library(dplyr)

# 1) %>% : 파이프 연산자 : df 조작에 필요한 함수 나열 기능
# 형식) df %>% func1() %>% func2()
iris %>% head() %>% filter(Sepal.Length >= 5.0) 


# 2) tibble() 함수 : 콘솔 크기에 맞는 데이터 구성
iris_df <- tibble(iris) # 콘솔 크기에 맞는 데이터 구성 
iris_df

# 3) filter() 함수 : 행 추출
# 형식) df %>% filter(필터조건)
names(iris) # 칼럼명 확인
iris %>% filter(Sepal.Width > 3) %>% head() # 조건에 만족하는 상위 6개의 자료만 추출
head(10) # 상위 10개 출력

# 4) arrange()함수 : 칼럼 기준 정렬 
# 형식) df %>% arrange(칼럼명)
sort(iris$Sepal.Width) # 오름차순(컬럼 하나만 정렬렬)
iris %>% arrange(Sepal.Width) %>% head() # 오름차순 
iris %>% arrange(Sepal.Width) %>% tail()

iris %>% arrange(desc(Sepal.Width)) %>% head() # 내림차순

# 5) select()함수 : 열 선택
# 형식) df %>% select(칼럼명1,칼럼명2)
iris %>% select(Sepal.Length:Petal.Length, Species) %>% head() 
iris[c('Sepal.Length','Sepal.Width','Petal.Length')] # 콜론(:) 사용 시 오류 발생
iris[c(1:3)]

# 6) mutate() 함수 : 파생변수(변형) 생성
# 형식) df %>% mutate(변수 = 식)
iris %>% mutate(diff = Sepal.Length - Sepal.Width) %>% head()


# 7) summarise()함수 : 통계 
# 형식) df %>% summarise(변수 = 내장함수)
iris %>% summarise(col1_avg = mean(Sepal.Length),
                   col2_sd = sd(Sepal.Width))
iris %>% summarise(mean(Sepal.Length),
                   sd(Sepal.Width))


# 8) group_by()함수 : 집단변수 이용 그룹화 
# 형식) df %>% group_by(집단변수)
iris_grp <- iris %>% group_by(Species)
# iris 변수 호출 -> 그룹화 -> iris_grp 객체에 저장
iris_grp # Groups:   Species [3]


# 그룹별 통계 
summarise(iris_grp, mean(Sepal.Length),count=n())
# n(): 해당 그룹 길이

# 9) left_join() 함수 : 왼쪽 dataframe의 x칼럼 기준 열 합치기  
df1 <- data.frame(x=1:5, y=rnorm(5))
df2 <- data.frame(x=1:5, z=rnorm(5))
df3 <- data.frame(x=6:9, z=rnorm(4))
df3

df_join <- left_join(df1, df2, by='x') # x칼럼 기준 : right_join()
df_join

# 10) right_join() 함수 : 오른쪽 dataframe의  x칼럼 기준 열 합치기 
df_join <- right_join(df1, df2, by='x') # 결과 동일 


# 11) bind_rows() : 행 합치기 
df1 <- data.frame(x=1:5, y=rnorm(5))
df2 <- data.frame(x=6:10, y=rnorm(5))

df_rows <- bind_rows(df1, df2,df3)
df_rows

# 12) bind_cols() : 열 합치기 
df_cols <- bind_cols(df1,df2,df3)

# 칼럼명 추출 + 수정
names(df_cols)=c('x1','y1','x2','y2')
df_cols


######################################################
# 2. reshape2 패키지 활용
######################################################
install.packages('reshape2')
library(reshape2)

# 1) dcast()함수 이용 : 긴 형식 -> 넓은 형식 변경
# - '긴 형식'(Long format)을 '넓은 형식'(wide format)으로 모양 변경

data <- read.csv(file=file.choose()) # data.csv
data

# data.csv 데이터 셋 구성 - 22개 관측치, 3개 변수
# Date : 구매날짜
# Customer : 고객ID
# Buy : 구매수량

# (1) '넓은 형식'(wide format)으로 변형
# 형식) dcast(데이터셋, row ~ col, FUNC)
# 앞변수 : 행 구성, 뒷변수 : 칼럼 구성

dcast(data, Customer_ID ~ Date)

wide <- dcast(data, Customer_ID ~ Date, sum) # 구매합계 
wide # Buy 칼럼을 이용해서 교차셀에 합 표시 

wide2 <- dcast(data, Customer_ID ~ Date, length) # 구매회수 
wide2

# 2) melt() 함수 이용 : 넓은 형식 -> 긴 형식 변경
#   형식) melt(data, id='열이름')

# - 긴 형식 변경
long <- melt(wide, id='Customer_ID') 
long

# id변수를 기준으로 넓은 형식이 긴 형식으로 변경

# 칼럼명 수정
name <- c("Customer_ID", "Date", "Buy")
colnames(long) <- name   
head(long)

# example
data("smiths") # reshape2에서 제공하는 dataset

smiths
melt(smiths,id=1:2,measure='weight')