import numpy as np


def my_dot(A, B):
    """두 행렬 A와 B의 dot 연산 결과를 리턴
        dot_ik = sum(j)[a_ij * b_jk]
    """
    print('A shape:', A.shape)
    print('B shape:', B.shape)
    if A.shape[1] != B.shape[0]:
        raise ValueError('A의 column과 B의 row 개수는 같아야 함!')
    n_row = A.shape[0]  # dot 결과 행렬의 row 개수
    n_col = B.shape[1]  # dot 결과 행렬의 column 개수
    temp = A.shape[1]  # 각 원소들끼리 곱한 결과를 더하는 회수
    numbers = []  # 결과값들을 저장할 리스트
    # 결과를 저장할 (n_row, n_col) 모양의 행렬
    result = np.zeros((n_row, n_col))
    for i in range(n_row):  # A 행렬의 row 개수만큼 반복
        for k in range(n_col):  # B 행렬의 column 개수만큼 반복
            n = 0
            for j in range(temp):
                # dot 결과 행렬의 [i,k]번째 원소의 값을 계산
                n += A[i, j] * B[j, k]
            numbers.append(n)  # [i,j]번째 원소를 리스트에 추가
            result[i, k] = n
    # 결과를 (n_row, n_col) 모양의 행렬로 변환해서 리턴
    return np.array(numbers).reshape(n_row, n_col)


A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])


def dot_1d(X, Y):
    if len(X) != len(Y):
        raise ValueError('len(X) != len(Y)')
    result = 0
    for i in range(len(X)):
        result += X[i] * Y[i]
    return result


def dot_2d(X, Y):
    n_row = X.shape[0]
    n_col = Y.shape[1]
    if X.shape[1] != Y.shape[0]:
        raise ValueError('X.shape[1] != Y.shape[0]')
    result = np.zeros((n_row, n_col))
    for i, row in enumerate(X):
        for j, col in enumerate(zip(*Y)):
            print(f'i={i}, row={row}, j={j}, col={col}')
            result[i, j] = dot_1d(row, col)
    return result


print(dot_2d(A, B))
print(dot_2d(B, A))


