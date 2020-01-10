'''
csv 모듈을 이용한 mpg.csv 파일 읽기

'''

import csv
import os

file_path = os.path.join('..', 'scratch08', 'mpg.csv')
# Windows OS: ..\scratch08\mpg.csv
# Linux, macOS: ../scratch08//mpg.csv
with open(file_path, mode = 'r', encoding = 'UTF-8') as f:
    # f.readline()
    reader = csv.reader(f)
    reader.__next__()   # 한줄 읽고 건너뜀 (.readline() 역할)
    df = [i for i in reader]

print(df[0:5])
print(df[0][0], df[0][1], df[0][2])


# 리스트에서 각 행마다 반복해서,
# 각 행의 인덱스 2번 아이템을 숫자로 변환해서 새로운 리스트에 저장
displ = [float(i[2]) for i in df]
print(displ)

with open(file_path, mode = 'r', encoding = 'UTF-8') as f:
    # 사전(dict) 타입으로 데이터들을 읽어주는 reader 객체
    # 보통 csv 파일에 컬럼 이름이 포함된 경우 사용
    reader = csv.DictReader(f)
    # DictReader 객체의 read 기능을 사용하려면,
    # 각 행은 '컬럼이름: 값' 의 쌍으로 이루어진 dict가 됨
    df = [i for i in reader]

print(df[0:5])
print(df[0])
print(df[0]['manufacturer'])
print(df[0]['model'])
print(df[0]['displ'])

displ = [float(i['displ']) for i in df]
print(displ)



