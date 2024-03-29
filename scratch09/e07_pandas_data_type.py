'''
pandas 데이터 타입
    Series: 1차원 리스트, 인덱스가 1개
    DataFrame: 2차원 리스트, 인덱스가 2개

'''

import pandas as pd
import numpy as np

a = pd.Series([1, 3, 5, np.nan, 6, 8])
print(type(a))  # Series
print(a)

# Series 에서 특정 인덱스의 아이템 선택: Series[index]
print(a[0:3])

# 인덱스 연산자([]) 안에서 법위 연산자(:)를 사용할 수도 있음
print(a[0:3])
print(a[[0, 2, 4]])

# dict 타입의 데이터에서 DataFrame 생성
df = pd.DataFrame({
    'no': [3, 13, 23],
    'name': ['김영광', '이은지', '조유경'],
    'gender': ['M', 'F', 'F']
})
print(df)

# 2차원 리스트([[...], [...], [...]] 타입의 데이터에서 DataFrame을 생성
students = pd.DataFrame([
    [4, '김재성', 'M'],
    [14, '이재경', 'M'],
    [24, '조지원', 'F']
], columns = ['번호', '이름', '성별'])
# students.columns = ['번호', '이름', '성별']
print(students)

print('=============')
# DataFrame.iloc[row_index, column_index]
print(students.iloc[0, 0])  # 0번 row, 0번 col
print(students.iloc[0, 0:3])    # 0번 row, 0, 1, 2 col에 있는 아이템
print(type(students.iloc[0, 0:3]))  # Series
print(students.iloc[0:2, 0:2])
print(type(students.iloc[0:2, 0:2]))    # DataFrame
print(students.iloc[:, 1:3])    # 모든 row, 1, 2 col
print(students.iloc[1:3, :])
print(students.iloc[1:3])   # 모든 col 선택할 때는 컬럼 인덱스를 생략 가능


# boolean indexing
print(students[[False, True, False]])
condition = (students['성별'] == 'M')
print(condition)    # [True, True, False]
print(students[condition])


# 데이터 프레임 이어 붙이기: concat
students.columns = ['no', 'name', 'gender']
stu_df = pd.concat([df, students])
print(stu_df)
print(stu_df.iloc[0])
print(stu_df.loc[0])

stu_df2 = pd.concat([df, students], ignore_index=True)
print(stu_df2)


# DataFrame.sort_values(정렬 기준 걸럼 이름
print(stu_df2.sort_values('no'))
print(stu_df2.sort_values('gender'))

# 두개 이상의 조건으로 boolean indexing
cond1 = stu_df2['no'] % 2 == 1  # no 컬럼의 값이 홀수 이면
cond2 = stu_df2['gender'] == 'F'    # gender 컬럼의 값이 'F'이면
subset = stu_df2[cond1 & cond2]
# boolean indexing 에서는 and, or 연산자 사용 할 수 없음
# 각 성분별로 연산하는 (bitwise 연산자) &, | 를 사용해야 함
print(subset)



