import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report

from scratch11.e03_knn함수제작 import train_test_split, my_scaler, MyKnnClassifier

if __name__ == '__main__':
    data = pd.read_csv('wisc_bc_data.csv')
    print(data.shape)
    print(data.head())


    X = data.iloc[:, 2:].to_numpy()
    y = data.iloc[:, 1].to_numpy()
    print(X)
    print(y)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .2)
    scaler = my_scaler()
    scaler.fit(X_train)
    X_train_scaled = scaler.transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    knn = MyKnnClassifier(n_neighbors = 5)
    knn.fit(X_train_scaled, y_train)
    y_pred = knn.predict(X_test_scaled)
    print(y_pred)

    print(np.mean(y_test == y_pred))

    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))
