'''
R을 확용한 머신러닝 - 암 데이터 파일 csv

scikit-learn 패키지 활용, kNN 결과

'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

data = pd.read_csv('wisc_bc_data.csv', encoding = 'UTF-8')

print(data.shape)
print(data.info())
print(data.describe())
print(data.head())
print(data.columns)

X = data.iloc[:, 2:].to_numpy()
y = data.iloc[:, 1].to_numpy()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .2)
print(len(X_train), len(X_test), len(y_train), len(y_test))

scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

for i in range(1):
    print(f'train 평균 = {X_train[:, i].mean()} , 표준편차 = {X_train[:, i].std()}')
    print(f'test 평균 = {X_test[:, i].mean()} , 표준편차 = {X_test[:, i].std()}')

knn = KNeighborsClassifier(n_neighbors = 5)
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

conf_matrix = confusion_matrix(y_test, y_pred)
print(conf_matrix)
report = classification_report(y_test, y_pred)
print(report)

errors = []
for i in range(1, 41):
    knn = KNeighborsClassifier(n_neighbors = i)
    knn.fit(X_train, y_train)
    pred_i = knn.predict(X_test)
    errors.append(np.mean(pred_i != y_test))

plt.plot(range(1, 41), errors, marker = 'o')
plt.title('Mean Error with K-Values')
plt.xlabel('k-value')
plt.ylabel('mean error')
plt.show()


##########################
a = np.array([1, 2, 3])
b = np.array([1, 4, 6])
print(a != b)
print(np.mean(a != b))
###########################


