import os
from collections import defaultdict, Counter

import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report

from scratch12.e04_NB함수제작 import summarize_by_class, calculate_class_probability


def train_test_split(df, test_size):
    '''
    df : DataFrame
    test_size : 테스트 세트의 비율

    학습 세트(X_train)와 검증 세트(X_test)를 return
    train/test set: list 또는 nd.array
    [[x1, x2, ..., label1], [x1, x2, ..., label2], ...], [[], [], ...]
    '''

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

    r = []
    for i in X_test:
        vector = i[:len(X_test[0]) - 1]
        x = calculate_class_probability(summaries, vector)
        # print(x)

        val_max = max(list(x.values()))
        # print(val_max)
        for key, val in x.items():
            if val == val_max:
                r.append(key)
    r = np.array(r)
    return r


def find_Class(class_list):

    f_Class = []
    for i in y:
        for j in y_set:
            if i == j:
                f_Class.append(y_set.index(i))

    return f_Class


if __name__ == '__main__':
    print('=== wisc_bc_data.csv ===\n')

    cancer_file = os.path.join('..', 'scratch11', 'wisc_bc_data.csv')
    cancer_dataset = pd.read_csv(cancer_file)

    del cancer_dataset['id']

    y = cancer_dataset['diagnosis']

    c = Counter(y)
    print(c)
    print(y.value_counts())