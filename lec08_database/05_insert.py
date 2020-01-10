'''
05_insert.py

'''


import cx_Oracle
import lec08_database.oracle_config as cfg

# 데이터 베이스 서버와 연결
with cx_Oracle.connect(cfg.user, cfg.pw, cfg.dsn, encoding = 'utf-8') as connection:
    # SQL 문장으로 실행, 결과 분석할 수 잇는 cursor 객체 생성
    with connection.cursor() as cursor:
        sql_insert = "insert into dept2(deptno, dname, loc) values(91, '강의장10', 'Seoul')"
        cursor.execute(sql_insert)
        # DML(Data Manipulation Language): insert, update, delete 결과를 영구적으로 반영하기 위해서는 commit을 해야 함
        connection.commit()

        sql_select = 'select * from dept2'
        cursor.execute(sql_select)
        for row in cursor:
            print(row)