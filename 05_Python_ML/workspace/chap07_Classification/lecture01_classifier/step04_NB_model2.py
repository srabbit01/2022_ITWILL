'''
3. MultinomialNB : x변수가 단어 빈도수(텍스트 데이터)를 분류할 때 적합
'''

###############################
### news groups 분류 
###############################

from sklearn.naive_bayes import MultinomialNB # tfidf 문서분류 
from sklearn.datasets import fetch_20newsgroups # news 데이터셋 
from sklearn.feature_extraction.text import TfidfVectorizer# 희소행렬 
# feature_extraction.text: text로부터 X변수로 쓰이는 특이점 추출
# Tf: Term Frequancy, i: Inverse, df: Document Frequency
# 문서와 단어를 행렬로 만든 행렬 -> 독립변수(X)로 사용
from sklearn.metrics import accuracy_score, confusion_matrix
# 평가도구: accuracy_score(분류정확도), confusion_matrix(혼동행렬)


# 1. dataset 가져오기 
newsgroups = fetch_20newsgroups(subset='all') # train/test load 

print(newsgroups.DESCR)
'''
**Data Set Characteristics:**

    =================   ==========
    Classes                     20 -> y범주 20개 10진수
    Samples total            18846 -> 독립변수(X) 개수
    Dimensionality               1
    Features                  text -> 텍스트 형태의 독립변수(X)
    =================   ==========
'''
print(newsgroups.target_names) # 20개 뉴스 그룹 
print(len(newsgroups.target_names)) # 20개 뉴스 그룹 


# 2. train set 선택 : 4개 뉴스 그룹  
# 20개는 너무 많음
#cats = ['alt.atheism', 'talk.religion.misc','comp.graphics', 'sci.space']
cats = newsgroups.target_names[:4]

news_train = fetch_20newsgroups(subset='train',categories=cats)
news_data = news_train.data # texts
news_target = news_train.target # 0 ~ 3


# 3. sparse matrix: 고차원 행렬
obj = TfidfVectorizer()
sparse_train = obj.fit_transform(news_data)
sparse_train.shape # (2245, 62227) - (doc, term)
type(sparse_train)

# 4. NB 모델 생성 
nb = MultinomialNB() # alpha=.01 (default=1.0)
model = nb.fit(sparse_train, news_target) # 훈련셋 적용 


# 5. test dataset 4개 뉴스그룹 대상 : 희소행렬
news_test = fetch_20newsgroups(subset='test', categories=cats)
news_test_data = news_test.data # texts(자연어)
y_true = news_test.target

sparse_test = obj.transform(news_test_data) # 함수명 주의  
sparse_test.shape # (1494, 62227)


# 6. model 평가 
y_pred = model.predict(sparse_test) # 예측치 
acc = accuracy_score(y_true, y_pred)
print('accuracy =', acc) # accuracy = 0.8520749665327979

# 2) confusion matrix
con_mat = confusion_matrix(y_true, y_pred)
print(con_mat)
'''
[[312   2   1   4]
 [ 12 319  22  36]
 [ 16  26 277  75]
 [  1   8  18 365]]
- 왼쪽 대각선: 정분류
- 이외: 오분류
'''
