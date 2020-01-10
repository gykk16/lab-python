'''
Naive Bayes 알고리즘
Naive Bayes 분류기(Classifier)를 iris 품종 분류

'''

from sklearn import datasets
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler

iris = datasets.load_iris()
print(type(iris))

# Bunch 클래스: {'data': [], 'target': []} 으로 이루어진 dict 와 비슷한 클래스
#   data: 특성(변수)들. n차원 공간의 점(point)
#   target: 레이블(분류 클래스)
# print(iris)
print('data shape :', iris.data.shape)
print('data target :', iris.target_names)
print('iris features: ', iris.feature_names)

X = iris.data
print('type X :', type(X))
print(X[:5])

y = iris.target
print('type y :', type(y))
print(y[:5])

X, y = datasets.load_iris(return_X_y = True)
# return_X_y = True: numpy.ndarray 들의 튜플(data, target)을 리턴
# return_X_y = False(기본값): Bunch 클래스 타입을 리턴

# 데이터 세트를 학습(Train) / 검증(Test) 세트로 나눔
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .2)

# 데이터들 변환 (스케일링)
scaler = StandardScaler()  # 생성자 호출
scaler.fit(X_train)
X_train_transformed = scaler.transform(X_train)
X_test_transformed = scaler.transform(X_test)

# 머신러닝 모델 선택 - Naive Bayes
gnb = GaussianNB()  # Gaussian Naive Bayes 모델 선택
gnb.fit(X_train_transformed, y_train)  # 모델 학습
y_pred = gnb.predict(X_test_transformed)  # 예측

# 성능 측정
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
