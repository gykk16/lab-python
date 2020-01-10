'''
lec08_database 패키지의 내용들을 참고해서,
오라클 데이터베이스에서 emp 테이블의 모든 레코드를 검색(select) -> 2차원 리스트
csv 모듈을 사용해서, csv 파일(emp.csv)로 저장

'''
import csv

import cx_Oracle


# 사용자 이름
user = 'scott'
# 비밀번호
pw = 'tiger'
# 데이터 베이스 서버 주소: DSN(Data Source Name)
dsn = 'localhost:1521/orcl'

emp =[]
with cx_Oracle.connect(user, pw, dsn) as conn:
    with conn.cursor() as cursor:
        cursor.execute('select * from emp')
        [emp.append(i) for i in cursor]

print(emp)

with open('emp.csv', mode = 'w', encoding = 'UTF-8') as f:
    writer = csv.writer(f, delimiter = ',')
    for i in emp:
        writer.writerow(i)



