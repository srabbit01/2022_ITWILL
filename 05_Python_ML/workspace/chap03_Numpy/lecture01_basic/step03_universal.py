'''
step03_universal.py

범용 함수(universal function) = 메서드
  - 다차원 배열의 원소를 대상으로 수학/통계 등의 연산을 수행하는 함수
'''
import numpy as np # 별칭 

dir(np) # 호출 가능한 함수 확인

# 1. numpy 제공 함수 -> np.function()
data = np.random.randn(5) # 1차원 난수 배열  # 정규분포 따름 

print(data) # 1차원 난수 
print(np.sum(data))
print(np.abs(data)) # 절대값
print(np.sqrt(data)) # 제곱근: 양수=계산결과, 음수=NaN
print(np.square(data)) # 제곱 -> 모든 값 양수화
print(np.sign(data)) # 부호: 음수(-1), 양수(1) 출력
print(np.var(data)) # 분산
print(np.std(data)) # 표준편차

                  
data2 = np.array([1, 2.5, 3.36, 4.6])

# 자연로그 함수 : 완만한 변화 -> data 정규화
np.log(data2) # 밑수 e
# [0.        , 0.91629073, 1.19392247, 1.5260563 ]

# 지수 함수 : 급격한 변화(지수적 변화)
np.exp(data2) # 밑 e
# [ 2.71828183, 12.18249396, 27.11263892, 99.48431564]

# 반올림 함수 
np.ceil(data2) # [1., 3., 4., 5.] - 큰 정수 올림 
np.rint(data2) # [1., 2., 3., 5.] - 가장 가까운 정수 올림
np.floor(data2) # 가장 가까운 정수 내림
np.round(data2, 1) # 자릿수 지정 

# 결측치 처리  
data2 = np.array([1,2.5, 3.3, 4.6, np.nan])
np.isnan(data2) # True 

# 결측치 제외 : 조건식 이용 
data2[np.logical_not(np.isnan(data2))] # [1. , 2.5, 3.3, 4.6]
data2[~(np.isnan(data2))] # 부정 기호: ~

# 2. numpy 객체 메서드 -> object.method()
data2 = np.random.randn(3, 4) # 2차원 난수 배열
print(data2)
print(data2.shape) # (3,4)
type(data2) # numpy.ndarray

dir(data2) # 호출 가능한 method() 확인

print('합계=', data2.sum()) # 합계
print('평균=', data2.mean()) # 평균
print('표준편차=', data2.std()) # 표준편차
print('최댓값=', data2.max()) # 최댓값
print('최솟값=', data2.min()) # 최솟값


# 3. axis 속성 
print(data2.sum(axis=0)) # 행 축 : 열 단위 합계 (차원축소: 2차원 -> 1차원)
print(data2.sum(axis=1)) # 열 축 : 행 단위 합계 (차원축소: 2차원 -> 1차원)
print('전체 원소 합계 :', data2.sum()) # 축 생략 : 전체 원소 합계 (차원축소: 2차원 -> 0차원)


