# 포루투갈의 2차교육과정에서 학생들의 음주에 영향을 미치는 요인은 무엇인가? 
# 만약 영향을 미친다면 그 정도는 어떠한가?
# 독립변수 = 음주에 영향을 미치는 요인들
# 종속변수 = 음주
# What are the factors influencing drinking in Portuguese secondary education? 
# If it does, what is its degree?

# data source (kaggle.com)
# https://www.kaggle.com/uciml/student-alcohol-consumption

# 파일 자료 불러오기 
setwd('E:/03. R/data/data')
student = read.csv('student-mat.csv')
str(student) # 'data.frame':	395 obs. of  33 variables:

# 학생들의 음주에 미치는 영향을 조사하기 위해 6가지의 변수 후보 선정
# 독립변수 : sex, age, Pstatus, failures, famrel, grade(G1+G2+G3)
# 종속변수 : Alcohol = (Dalc+Walc)/2*100 : 1주간 알코올 섭취정도  
# 파생변수: grade=G1+G2+G3, Alcohol=(Dalc+Walc)/2*100

# subset 만들기 
df = student[c('sex','age','Pstatus','failures','famrel','Dalc','Walc','G1','G2','G3')]
str(df)
# data.frame :	395 obs. of  10 variables:
# $ sex       : chr : 성별(F, M)
# $ age       : int : 나이(15 ~ 22)
# $ Pstatus   : chr : 부모거주여부(T, A)
# $ failures  : int : 수업낙제횟수(0,1,2,3)
# $ famrel    : int : 가족관계(1,2,3,4,5)
# $ Dalc      : int : 1일 알콜 소비량(1,2,3,4,5) -> 1: 적음 ~ 5: 많음
# $ Walc      : int : 1주일 알콜 소비량(1,2,3,4,5)  
# $ G1        : int : 첫번째 학년 성적(0~20)
# $ G2        : int : 두번째 학년 성적(0~20) 
# $ G3        : int : 마지막 학년 성적(0~20) 


# 1. 각 변수의 통계량과 빈도수 확인
summary(df) # 오직 숫자형 변수의 통계 결과만 확인 가능

table(df$sex) # 여학생이 다소 많음
#   F   M 
#  208 187

table(df$Pstatus) # A: Alone(혼자거주), T: Together(부모님함께거주)
#   A   T 
#  41 354

prop.table(table(df$Pstatus)) # 비율 확산
#  A         T 
# 0.1037975 0.8962025 

# 2. 파생변수 만들기

df$grade=df$G1+df$G2+df$G3 # 1~3학년 점수
range(df$grade)
# $ grade   : int : 전체 학년 점수의 합 (4~58)

df$Alcohol=(df$Dalc+df$Walc)/2*100 # 알콜 소비량(평균치)
# $ Alchohol: num : 알콜 소비량 평균 (100~500) # 100: 알콜 소비량 낮은 ~ 500: 알콜 소비량 높음

# 3. 기존 변수 제거: G1~G3, Dalc, Walc
# 찾고자 할 위치 찾기: Which() 함수 사용
names(df)
which(names(df)=='Dalc') #6
which(names(df)=='G3') # 10
# 특정 칼럼을 제외하고 새로운 데이터프레임 생성
new_df = df[-c(6:10)] # 칼럼 제거 -> new df
str(new_df)
# 'data.frame':	395 obs. of  7 variables:
# $ sex     : chr  "F" "F" "F" "F" ...                         독립변수(x1)
# $ age     : int  18 17 15 15 16 16 16 17 15 15 ...           독립변수(x2)
# $ Pstatus : chr  "A" "T" "T" "T" ...
# $ failures: int  0 0 3 0 0 0 0 0 0 0 ...
# $ famrel  : int  4 5 4 3 4 5 4 4 4 5 ...
# $ grade   : int  17 16 25 44 26 45 35 17 53 44 ...
# $ Alcohol : num  100 100 250 100 150 150 100 100 100 100 ...

# 4. EDA: 종속변수 기준으로 독립변수 탐색
library(lattice) # 격자 기준 고급 시각화

# 1) Alcohol vs sex
barplot(table(new_df$sex)) # 문자형의 경우, table()로 만들어 사용

# 음주량과 성별: 연속형변수 vs 범주형변수
densityplot(~Alcohol,data=new_df,group=sex,
            plot.points=T,auto.key=T) # 남성에 비해 여성의 알코올 섭취량이 적음
# 남학생이 여학생에 비해 음주 소비량이 많음

# 2) Alcohol vs Pstatus
densityplot(~Alcohol,data=new_df,group=Pstatus,
            plot.points=T,auto.key=T)
# 부모의 거주 상태는 음주 소비량과 관련성이 낮음 (큰 차이가 없음)

# 3) Alcohol vs failures
densityplot(~Alcohol,data=new_df,group=failures,
            plot.points=T,auto.key=T)
# 낙제 개수가 많을 수록 음주 소비량이 많음 (강한 상관성)

# 4) Alcohol vs grade: 연속변수 vs 연속변수 -> 산점도 그리기
plot(Alcohol~grade,data=new_df) # 산점도 제공하는 lattice 패키지: 기존 plot과 매우 유사한 형식
# 하위 점수: 음주 소비량 높음(증가)
# 중위 점수: 음수 소비량 변화 없음(가장높음)
# 상위 점수: 음주 소비량 낮음(감소)

# 5) 각 점수별 음주량의 평균으로 시각화
library(dplyr)

# 성적별 그룹 생성
group = new_df %>% group_by(grade)
grade_al = summarise(group,mean(Alcohol))
grade_al

plot(grade_al) # 점수대 별 알코올 소비량 시각화
# 하위 점수(0~20점대): 음주 소비량 높음(증가)
# 중위 점수(20~40점대): 음수 소비량 변화 없음(가장높음)
# 상위 점수(40~60점대): 음주 소비량 낮음(감소)

# 6) 각 연령별 음주량 평균으로 시각화
group = new_df %>% group_by(age)
age_al = summarise(group,mean(Alcohol))
age_al

plot(age_al)
# 연령대가 증가할 수록 음주 소비량 증가 (단, 18~19세 제외) (강한 상관성)

# 7) Alcohol vs famrel
group = new_df %>% group_by(famrel)
famrel_al = summarise(group,mean(Alcohol))
plot(famrel_al)
# 가족 간의 화목정도가 좋을 수록 음주 소비량 감소 (매우 강한 상관성)

## [정리]
# 강한 상관성: famrel(가족관계), 연령(age), failures(낙제점 개수)
# 상관성 없음: Pstatus(부모와동거여부)
# 특정 구간에서 상관성 유무: grade(점수) -> 0~20점, 20~40점, 40~60점