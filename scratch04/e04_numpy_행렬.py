'''
numpy의 행렬 관련 함수

'''
import numpy as np

# numply.ndarray 타입의 객체를 생성
A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

B = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

print(A)
print('shape of A =', A.shape)
print()
print(B)
print('shape of B =', B.shape)
print()
nrows, ncols = B.shape
print(nrows, '*', ncols)

# slicing: 원하는 행, 열의 원소들을 추출
# list[row][col], ndarray[row, col]
print(A[1, 2])
print(A[0, 0:2])
print(A[0:2, 0:2])
print(A[:, :])

print()
# 항등 행렬(Identity Matrix)
identity_matrix = np.identity(3, dtype = int)
print(identity_matrix)

print()
# 전치 행렬(Transpose Matrix)
print(A.transpose())
print(B.transpose())

print()
# 행렬 곱셈
#   [n * m] & [m * k] => [n * k] 행렬 리턴
#   두 행렬의 m 은 길이가 같아함
print(A.dot(B))
print(B.dot(A))

