#################################
## <제3장 연습문제>
#################################   
#01. 본문에서 작성한 titanic 변수를 다음과 같은 단계를 통해서 파일로 저장한 후 파일을 불러오시오.

#[단계 1] 'C:/ITWILL/3_Rwork/output' 폴더에 '행 이름' 없이 'titanic_df.csv'로 저장한다.
#힌트: write.csv() 함수 사용
write.csv(titanic_df,file="D:/03. R/output/titanic_df",row.names=F)

#[단계 2] 'titanic_df.csv' 파일을 titanicData 변수로 가져와서 결과를 확인하고, titanicData의 관측치와 칼럼수를 확인한다.
#힌트: read.csv(), str() 함수 사용
titanicData = read.csv("D:/03. R/output/titanic_df")
titanicData
str(titanicData)

#[단계 3] 1번, 3번 칼럼을 제외한 나머지 칼럼을 대상으로 상위 6개의 관측치를 확인한다. 
# 힌트 : 색인 이용 
titanicData[1:6,-c(1,3)]

# 02. R에서 제공하는 quakes 데이터셋을 대상으로 다음과 같이 처리하시오
data("quakes")
quakes # 지진 진앙지 데이터 셋 
str(quakes)
# 'data.frame':	1000 obs. of  5 variables:

# [단계1] 'C:/ITWILL/3_Rwork/output' 폴더에 row.names, quote 없이 "quakes_df.csv" 파일명으로 저장 
write.csv(quakes,"D:/03. R/output/quakes_df.csv",row.names=F,quote=F)

# [단계2] quakes_data로 파일 읽기 
quakes_df = read.csv("D:/03. R/output/quakes_df.csv")
str(quakes_df)

# [단계3] mag 변수를 대상으로 평균 계산하기 
head(quakes_df)
mean(quakes_df$mag,na.rm=T)
mag = quakes_df$mag
cat("mag 변수의 평균: ", mean(mag))

# 03. 다음의 Data2 객체를 대상으로 정규표현식을 적용하여 문자열을 처리하시오
Data2 <- c("2021-02-05 수입3000원","2021-02-06 수입4500원","2021-02-07 수입2500원")
library(stringr)

# 조건1) 일짜별 수입을 다음과 같이 출력하시오.
#  <출력 결과>  "3000원" "4500원" "2500원" 
str_extract_all(Data2,"\\d{4,}원")
price = str_extract_all(Data2,'[0-9]{4}[가-힣]$')
price = unlist(price)
price

# 조건2) 위 벡터에서 연속하여 2개 이상 나오는 모든 숫자를 제거하시오.  
#  <출력 결과> "-- 수입원" "-- 수입원" "-- 수입원"
str_replace_all(Data2,"[0-9]{1,}",'')

# 조건3) 위 벡터에서 -를 /로 치환하시오.
#   <출력 결과>  "2021/02/05 수입3000원" "2021/02/06 수입4500원" "2021/02/07 수입2500원"  
str_replace(Data2,'-','/')

# 조건4) 모든 원소를 쉼표(,)에 의해서 하나의 문자열로 합치시오. 
# 힌트) str_c(데이터셋, collapse="구분자")함수 이용
#   <출력 결과>  "2021-02-05 수입3000원,2021-02-06 수입4500원,2021-02-07 수입2500원"
str_c(Data2,collapse=',')