'''
다음과 같은 결과가 나올 수 있도록
numpy를 사용하지 않고 add(x, y), subtract(), multiply(), divide(), dot() 함수를 구현
|1 2| + |5 6| = |6  8 |
|3 4|   |7 8|   |10 12|

|1 2| - |5 6| = |-4 -4|
|3 4|   |7 8|   |-4 -4|

|1 2| * |5 6| = |5  12|
|3 4|   |7 8|   |21 32|

|1 2| / |5 6| = |0.2   0.333|
|3 4|   |7 8|   |0.428 0.5  |

|1 2| @ |5 6| = |19 22|
|3 4|   |7 8|   |43 50|
위의 결과와 같은 결과를 주는 numpy 코드를 작성

항등 행렬(Indentity matrix): 대각선의 원소는 1이고, 나머지 원소는 0인 정사각행렬
    A @ I = I @ A = A를 만족
역행렬(Inverse matrix): A @ A- = A- @ A = I를 만족하는 행렬
전치 행렬(Transpose matrix): 행렬의 row와 column을 서로 바꾼 행렬

'''
import numpy as np


def add(x, y):
    z = z = np.zeros(shape = (len(x), len(x[0])))
    for i in range(len(x)):
        for j in range(len(x[0])):
            z[i, j] = x[i, j] + y[i, j]
    return z


def substract(x, y):
    z = z = np.zeros(shape = (len(x), len(x[0])))
    for i in range(len(x)):
        for j in range(len(x[0])):
            z[i, j] = x[i, j] - y[i, j]
    return z


def multiply(x, y):
    z = z = np.zeros(shape = (len(x), len(x[0])))
    for i in range(len(x)):
        for j in range(len(x[0])):
            z[i, j] = x[i, j] * y[i, j]
    return z


def divide(x, y):
    z = z = np.zeros(shape = (len(x), len(x[0])))
    for i in range(len(x)):
        for j in range(len(x[0])):
            z[i, j] = x[i, j] / y[i, j]
    return z


def dot(x, y):
    ''' 두 행렬 A와 B의 dot 연산 결과를 리턴
        dot_ik = sum(j)[a_ij * b_jk]
        '''
    z = np.zeros(shape = (len(y), len(x[0])))
    for i in range(len(x)):
        for j in range(len(x[0])):
            z[i, j] = x[i, 0] * y[0, j] + x[i, 1] * y[1, j]

    return z


def my_dot(x, y):
    ''' 두 행렬 A와 B의 dot 연산 결과를 리턴
        dot_ik = sum(j)[a_ij * b_jk]
        '''
    if x.shape[1] != y.shape[0]:
        raise ValueError('x의 column과 y의 row 개수는 같아야 함')

    row = x.shape[0]  # dot 결과 행렬의 row 개수
    col = y.shape[1]  # dot 결과 행렬의 col 개수
    temp = x.shape[1]  # 각 원소들끼리 곱한 결과를 더하는 횟수

    z = np.zeros(shape = (x.shape[0], y.shape[1]))
    for i in range(row):  # x 행렬의 row 개수만큼 반복
        for j in range(col):  # y 행렬의 column 개수만큼 반복
            n = 0.
            for k in range(temp):
                # dot 결과 행렬의 [i, j]번째 원소의 값을 계산
                n += x[i, k] * y[k, j]
            z[i, j] = n

    return z


if __name__ == '__main__':
    x = np.array([[1, 2],
                  [3, 4]])

    y = np.array([[5, 6],
                  [7, 8]])

    A = np.array([[1, 1, 1],
                  [2, 2, 2]])

    B = np.array([[1, 2],
                  [3, 4],
                  [5, 6]])
    r = my_dot(A, B)

    print(r)
    print()
    print(A.dot(B))
