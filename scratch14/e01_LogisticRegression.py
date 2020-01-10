'''
Linear Regression (선형 회귀) : 값을 예측

Logistic Regression (로지스틱 회귀) : 분류를 하기 위한 알고리즘

'''
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()
X = iris['data']
y = iris['target']
features = iris['feature_names']

print(features)

cols = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
iris_df = pd.DataFrame(X, columns = cols)

print(iris_df.head())  # iris.iloc[:5, :]

iris_df['species'] = y
print(iris_df.iloc[:5])
print(iris_df.describe())

sns.pairplot(iris_df, hue = 'species', vars = cols)
plt.show()

# 데이터(X)와 타겟(y)을 학습/검증 세트로 분리
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size = .2,
                                                    random_state = 1217)

# 분류 알고리즘 중에서 Logistic Regression 을 선택
log_reg = LogisticRegression()

# 모델 적합(fitting) / 학습(training)
log_reg.fit(X_train, y_train)

# 예측 / 테스트
predictions = log_reg.predict(X_test)

print('y true :', y_test)
print('y pred :', predictions)

# 성능 측정
print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))

