'''
08_update.py

부서 번호를 업력 받아서, 해당 부서의 위치를 update 실행
'''


import cx_Oracle
import lec08_database.oracle_config as cfg

with cx_Oracle.connect(cfg.user, cfg.pw, cfg.dsn, encoding = 'utf-8') as connection:
    with connection.cursor() as cursor:
        deptno = int(input('수정 할 위치 부서 번호 >> '))
        loc = input('수정할 위치 >> ')

        sql1 = 'update dept2 set loc = :loc where deptno = :dept_no'
        cursor.execute(sql1,
                       loc = loc,
                       dept_no = deptno)

        connection.commit()

        sql_select = 'select * from dept2'
        cursor.execute(sql_select)
        for row in cursor:
            print(row)
