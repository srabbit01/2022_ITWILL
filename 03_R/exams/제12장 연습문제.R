#################################
## <제12장 연습문제>
################################# 

# 01. 다음 mtcars 데이터셋을 대상으로 연비효율(mpg), 실린더수(cyl), 엔진크기(disp),
#  마력(hp), 무게(wt) 변수를 대상으로 서브셋을 작성하시오.
library(datasets) # 기본 패키지
data(mtcars)
str(mtcars)

mtcars_sub=mtcars[,c(1:4,6)]
str(mtcars_sub)

# 02. 작성된 서브셋을 대상으로 상관분석을 수행하여 연비효율(mpg)과 가장 상관계수가 
# 높은 변수를 확인하시오. 
# cor() 함수 이용
cor(mtcars_sub)
cor(mtcars_sub[,'mpg'],mtcars_sub) # wt와 가장 상관성이 높음

# 03. 연비효율과 가장 상관계수가 높은 변수와 산점도로 시각화하시오. 힌트) plot()함수 이용 
plot(mtcars_sub$mpg,mtcars_sub$wt) # 음(반비례)의 선형 관계

# 04. iris 데이터셋에서 5번째 칼럼을 제외한 4개의 칼럼으로 상관계수를 확인하시오.
# <단계1> 4개 칼럼 간의 상관계수 행렬 확인 
cor(iris[,-5])
#             Sepal.Length Sepal.Width Petal.Length Petal.Width
# Sepal.Length    1.0000000  -0.1175698    0.8717538   0.8179411
# Sepal.Width    -0.1175698   1.0000000   -0.4284401  -0.3661259
# Petal.Length    0.8717538  -0.4284401    1.0000000   0.9628654
# Petal.Width     0.8179411  -0.3661259    0.9628654   1.0000000
# 양의 상관계수가 가장 큰 관계: Petal.Length & Petal.Width

# <단계2> 첫번째 칼럼(Sepal.Length) 기준으로 나머지 변수와 상관계수 출력  
cor(iris$Sepal.Length,iris[,1:4]) # 상관계수 행렬
#     Sepal.Length Sepal.Width Petal.Length Petal.Width
#[1,]            1  -0.1175698    0.8717538   0.8179411

# <단계3> 양의 상관계수가 가장 큰 두 변수를 대상으로 산점도 시각화
library(ggplot2) 
# qplot(x,y,color=색상)

# <조건1> qplot()함수 이용
qplot(x=Petal.Length,y=Petal.Width,data=iris)

# <조건2> Species 변수로 색상 적용     
qplot(x=Petal.Length,y=Petal.Width,color=Species,data=iris)
# 산점도에서 양의 상관관계를 나타내는 선형성이 나타남
# 회귀선(선)을 그리면 x와 y의 상관관계를 차악할 수 있음 # 0.9628의 선형성