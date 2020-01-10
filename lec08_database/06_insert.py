'''
06_insert.py

시용자 입력을 받아서 데이터베이스에 insert
'''

import cx_Oracle
import lec08_database.oracle_config as cfg

with cx_Oracle.connect(cfg.user, cfg.pw, cfg.dsn, encoding = 'utf-8') as connection:
    with connection.cursor() as cursor:
        deptno = int(input('부서 번호 입력>> '))
        dname = (input('부서 이름 입력>> '))
        loc = input('부서 위치>> ')

        sql_insert = f"insert into dept2 values({deptno}, '{dname}', '{loc}')"
        # 사용자가 입력한 문자열에 따음표(')가 포함되어 있는 경우 SQL 에러가 발생 할 수 있음. 권하지 않는 방법.
        # -> data binding 방법 권장.
        cursor.execute(sql_insert)

        connection.commit()



