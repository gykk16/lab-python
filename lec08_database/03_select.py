'''
ex03_select.py

for-in 구문을 사용한 결과 처리

for 변수 in 커서:
    실행문
for-in 구문에서 cursor.fetchone()ㅇ의 결과를 변수에 전달

'''

import cx_Oracle
import lec08_database.oracle_config as cfg


# connection 설정
connection = cx_Oracle.connect(cfg.user,
                               cfg.pw,
                               cfg.dsn)

# cursor 설정
cursor = connection.cursor()

# SQL 문장 실행
cursor.execute('select * from dept')

# select 결과 처리
for row in cursor:
    print(row)

# cursor 종료
cursor.close()

# connection 종료
connection.close()