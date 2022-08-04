'''
 문2) 당료병(diabetes.csv) 데이터 셋을 이용하여 다음과 같은 단계로 
     RandomForest 모델을 생성하시오.

  <단계1> 데이터셋 로드 & 칼럼명 적용 
  <단계2> x, y 변수 선택 : x변수 : 1 ~ 8번째 칼럼, y변수 : 9번째 칼럼
  <단계3> 500개의 트리를 이용하여 모델 생성   
  <단계4> 중요변수 시각화 : feature names 적용                    
'''

from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import matplotlib.pyplot as plt # 중요변수 시각화 

# 단계1. 테이터셋 로드 
path=r"C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML"
dia = pd.read_csv(path+'/data/diabetes.csv', 
                  header=None) # 제목 없음 

print(dia.info())
# 칼럼명 추가 
dia.columns = ['Pregnancies','Glucose','BloodPressure','SkinThickness',
               'Insulin','BMI','DiabetesPedigree','Age','Outcome']
print(dia.info()) 
'''
 0   Pregnancies       759 non-null    float64
 1   Glucose           759 non-null    float64
 2   BloodPressure     759 non-null    float64
 3   SkinThickness     759 non-null    float64
 4   Insulin           759 non-null    float64
 5   BMI               759 non-null    float64
 6   DiabetesPedigree  759 non-null    float64
 7   Age               759 non-null    float64
 8   Outcome           759 non-null    int64  
 (한글명 : 임신, 혈당, 혈압, 피부두께,인슐린,비만도지수,당료병유전,나이,결과)  
'''


# 단계2. x,y 변수 생성 
# x, y 변수 선택 : x변수 : 1 ~ 8번째 칼럼, y변수 : 9번째 칼럼
X=dia.iloc[:,[1:9]]
y=dia.iloc[:,9]

# 단계3. model 생성
# 500개의 트리를 이용하여 모델 생성   
model = RandomForestClassifier() .fit(X = X, y = y)

# 단계4. 중요변수 시각화 
# 중요변수 시각화 : feature names 적용      
plt.bar(range(X.shape[1]),model.feature_importances_)
plt.xticks(range(X.shape[1]),X.colums)
plt.ylabel('feature_importances')

# Gluscose(혈당) > BMI(비만도지수)