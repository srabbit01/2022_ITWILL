#################################
## <제6장 연습문제>
################################# 

# 01. dplyr 패키지에서 제공하는 함수를 이용하여 다음과 같이 단계별로 처리하시오. 
library(dplyr)

# 변수명 확인 
names(iris)
# [1] "Sepal.Length" "Sepal.Width"  "Petal.Length" "Petal.Width"  "Species" 

# [단계1] iris의 꽃잎의 길이(Petal.Length) 칼럼을 대상으로 5.0 이상의 값만 필터링하여 q1에 저장하시오.
q1 <- iris %>% filter(Petal.Length>=5.0)
class(q1) # "data.frame" -> dataframe을 입력하면 dataframe으로 출력력
dim(q1) # [1] 46  5 -> 조건에 만족하는 128개 행 선택

# [단계2] 01번에서 만든 q1을 대상으로 1,3,5번 칼럼만 선택하여 q2에 저장하시오.
q2 <- q1 %>% select(c(1,3,5))
q2 <- q1 %>% select(Sepal.Length,Petal.Length,Species)
dim(q2) # [1] 6 3 -> 3개의 칼럼(열) 선택

# [단계3] 02번에서 만든 q2를 대상으로 1번 - 3번 칼럼의 차를 구해서 diff 파생변수를 만들고, q3에 저장하시오.
q3 <- q2 %>% mutate(diff=iris[1]-iris[3])
q3 <- q2 %>% mutate(diff=Sepal.Length - Petal.Length)
head(q3)
dim(q3) # [1] 150   4
names(q3) # [4] diff

# [단계4] 03번에서 만든 q3를 대상으로 꽃의 종(Species)별로 그룹화하여 Sepal.Length와 Petal.Length 변수의 평균을 계산하시오.
q4 <- q3 %>% group_by(Species) %>% summarise(sep_len_mean=mean(Sepal.Length),
                                               pet_len_mean=mean(Petal.Length))
dim(q4) # [1] 2 3
q4

# 02. mtcars 데이터셋의 qsec(1/4마일 소요시간) 변수를 대상으로 극단치(상위 0.3%)를 
# 발견하고, 정제하여 mtcars_df 이름으로 서브셋을 생성하시오.

library(ggplot2)
str(mtcars) # 'data.frame':	32 obs. of  11 variables:

# [단계1] 이상치 통계
boxplot(mtcars$qsec) # 객체에서 호출 가능한 멤버 확인
boxplot(mtcars$qsec)$stats # 정상범주: 14.5 ~ 20.22
summary(mtcars$qsec)

# [단계2] 서브셋 생성
mtcars_df = subset(mtcars,14.50<=qsec & qsec<=20.22)

# [단계3] 정제 결과 확인 
str(mtcars_df)
summary(mtcars_df$qsec)
boxplot(mtcars_df$qsec)

# 03. 본문에서 생성된 dataset2의 resident 칼럼을 대상으로 NA 값을 제거한 후 dataset3 변수에 저장하시오.
dataset3 = subset(dataset2,!is.na(resident)) # subset(dataset,조건식)
dim(dataset3)

dataset4 = na.omit(dataset2$resident)
table(is.na(dataset4))

# 04. 본문에서 생성된 dataset2의 직급(position) 칼럼을 대상으로 1급 -> 5급, 5급 -> 1급 형식으로
# 역코딩하여 position2 칼럼에 추가하시오.
dataset2$position2=6-dataset2$position
head(dataset2[c('position','position2')])

# 05. dataset3의 gender 칼럼을 대상으로 1->"남자", 2->"여자" 형태로 코딩 변경하여 
# gender2 칼럼에 추가하고, 파이 차트로 결과를 확인하시오.
# 형식) df$칼럼명[조건식]='값'
dataset3$gender2[dataset3$gender==1]="남자"
dataset3$gender2[dataset3$gender==2]="여자"
head(dataset3[c('gender','gender2')])

# 06. 나이를 30세 이하 -> 1, 31~55 -> 2, 56이상 -> 3 으로 리코딩하여 age3 칼럼에 추가한 후 
# age, age2, age3 칼럼만 확인하시오.
dataset3$age3[dataset3$age<=30]=1
dataset3$age3[dataset3$age>30 & dataset3$age<=55]=2
dataset3$age3[dataset3$age>55]=3
head(dataset3[c('age','age2','age3')])


# 07. 정제된 dataset3를 대상으로 작업 디렉터리(c:/itwill/3_Rwork/output)에 cleanData.csv 파일명으로 
# 따옴표(quote)와 행 이름(row.names)을 제거하여 저장하고, new_data변수로 읽어오시오.

# (1) 정제된 데이터 저장
write.csv(dataset3,"cleanData.csv", quote=F, row.names=F)

# (2) 저장된 파일 불러오기/확인
new_data <- read.csv("cleanData.csv")
head(new_data)


# 08. user_data.csv와 return_data.csv 파일을 이용하여 각 고객별 
# 반품사유코드(return_code)를 대상으로 다음과 같이 파생변수를 추가하시오.
user_data=read.csv('user_data.csv')
return_data=read.csv('return_data.csv')

# <조건1> 반품사유코드에 대한 파생변수 칼럼명 설명 
# 제품이상(1) : return_code1, 변심(2) : return_code2, 
# 원인불명(3) :> return_code3, 기타(4) : return_code4 
head(return_data)
return_table=dcast(return_data,user_id~return_code)
names(return_table)=c('user_id','제품이상(1)','변심(2)','원인불명(3)','기타(4)')
head(return_table)

# <조건2> 고객별 반품사유코드를 고객정보(user_data) 테이블에 추가(join)
library(dplyr)
new_table=left_join(user_data,return_table,by='user_id')
new_table