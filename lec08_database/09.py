'''

1) emp 테이블에서 부서 번호를 입력 받아서, 해당 부서의 직원들의 사번, 이름, 부서번호를 출력

2) emp 테이블에서 사원 이름을 입력 받아서, 해당 글자가 이름에 표함된 직원들의 사번, 이름, 급여를 출력

'''

import cx_Oracle
import lec08_database.oracle_config as cfg

with cx_Oracle.connect(cfg.user, cfg.pw, cfg. dsn, encoding = 'utf-8') as connection:
    with connection.cursor() as cursor:
        deptno = int(input('부서 번호 입력 >> '))

        sql1 = 'select empno, ename, deptno from emp where deptno = :dept_no'
        cursor.execute(sql1,
                       dept_no = deptno)
        # for row in cursor:
        #     print(row)
        for empno, ename, deptno in cursor: # 성분 분해, unpacking
            print(empno, ename, deptno)

        print()
        ############################

        ename = input('사원 이름 입력 >> ').upper()

        sql2 = 'select empno, ename, sal from emp where upper(ename) like :e_name'
        cursor.execute(sql2,
                       e_name = '%' + ename + '%')

        for empno, ename, sal in cursor:
            print(empno, ename, sal)

        connection.commit()


