'''

emp, dept 테이블에서
부서 번호를 입력 받아서
해당 부서 사원의 사번, 이름, 급여, 부서 번호, 부서 이름 출력

'''

import cx_Oracle
import lec08_database.oracle_config as cfg

with cx_Oracle.connect(cfg.user, cfg.pw, cfg.dsn) as connection:
    with connection.cursor() as cursor:

        deptno = int(input('부서 번호 입력 >> '))

        sql1 = '''
                select e.empno, e.ename, e.sal, e.deptno, d.dname
                from emp e, dept d
                where e.deptno = d.deptno and e.deptno = :dept_no
                '''
        cursor.execute(sql1,
                       dept_no = deptno)

        for row in cursor:
            print(row)