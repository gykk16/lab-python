import os

import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report

from scratch12.e04_NB함수제작 import summarize_by_class, calculate_class_probability


def find_Class(class_list):
    f_set = list(set(class_list))
    f_Class = []
    for i in class_list:
        for j in f_set:
            if i == j:
                f_Class.append(f_set.index(i))

    return f_Class


def train_test_split(df, test_size):
    '''
    df : DataFrame
    test_size : 테스트 세트의 비율

    학습 세트(X_train)와 검증 세트(X_test)를 return
    train/test set: list 또는 nd.array
    [[x1, x2, ..., label1], [x1, x2, ..., label2], ...], [[], [], ...]
    '''
    df = df.to_numpy()
    length = len(df)
    indices = np.array([i for i in range(length)])
    np.random.shuffle(indices)

    cut = int(length * (1 - test_size))

    X_train = df[indices[:cut]]
    X_test = df[indices[cut:]]
    X_class = X_test[:, -1]

    return X_train, X_test, X_class


def predict(summaries, X_test):
    ''' 테스트 세트의 예측값들의 배열(리스트)을 return
        [0, 1, 1, 2, 0, 0, 2, ...]
        '''

    predicts = []
    for i in X_test:
        # print(i)
        x = calculate_class_probability(summaries, i)
        # print(x)

        val_max = max(list(x.values()))
        # print(val_max)
        for key, val in x.items():
            if val == val_max:
                predicts.append(key)
    predicts = np.array(predicts)
    return predicts


if __name__ == '__main__':
    print('=== iris.csv ===\n')
    iris_file = os.path.join('..', 'scratch11', 'iris.csv')

    iris_dataset = pd.read_csv(iris_file,
                               header = None,
                               names = ['x1', 'x2', 'x3', 'x4', 'species'])

    y_Class = find_Class(iris_dataset['species'])
    # y_Class = []
    # for j in iris_dataset['name']:
    #     if j == 'Iris-setosa':
    #         y_Class.append(0)
    #     if j == 'Iris-versicolor':
    #         y_Class.append(1)
    #     if j == 'Iris-virginica':
    #         y_Class.append(2)

    iris_dataset['Class'] = y_Class
    del iris_dataset['species']
    # iris_dataset = iris_dataset.to_numpy()
    # print(iris_dataset[:5])

    X_train, X_test, X_class = train_test_split(iris_dataset, test_size = .2)

    summaries = summarize_by_class(X_train)

    x_pred = predict(summaries, X_test)

    print(X_class)
    print(type(X_class), X_class.shape)
    print(x_pred)
    print(type(x_pred), x_pred.shape)
    print(confusion_matrix(X_class, x_pred))
    print(classification_report(X_class, x_pred))

    print('\n\n')
    ##################################################
    print('=== wisc_bc_data.csv ===\n')

    cancer_file = os.path.join('..', 'scratch11', 'wisc_bc_data.csv')
    cancer_dataset = pd.read_csv(cancer_file)

    del cancer_dataset['id']

    # cols = cancer_dataset.columns.tolist()
    # cols.remove('diagnosis')
    # cols.append('diagnosis')
    # cancer_dataset = cancer_dataset[cols]

    y = cancer_dataset['diagnosis']
    # y_Class = []
    # for i in y:
    #     if i == 'B':
    #         y_Class.append(0)
    #     if i == 'M':
    #         y_Class.append(1)

    y_Class = find_Class(y)

    del cancer_dataset['diagnosis']  # .drop 활용
    cancer_dataset['Class'] = y_Class
    # cancer_dataset = cancer_dataset.to_numpy()
    # print(cancer_dataset[:-5], cancer_dataset.shape)

    X_train, X_test, X_class = train_test_split(cancer_dataset, test_size = .2)

    summaries = summarize_by_class(X_train)

    x_pred = predict(summaries, X_test)

    print(X_class)
    print(type(X_class), X_class.shape)
    print(x_pred)
    print(type(x_pred), x_pred.shape)
    print(confusion_matrix(X_class, x_pred))
    print(classification_report(X_class, x_pred))

