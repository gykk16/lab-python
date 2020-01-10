'''



'''
import cx_Oracle
import lec08_database.oracle_config as cfg
import pandas as pd

def get_columns_names_of(table, cursor):
    # sql_select = f"""
    #                 select column_name
    #                 from user_tab_columns
    #                 where table_name = '{table.upper()}'
    #                 order by column_id
    #                 """
    # cursor.execute(sql_select)

    select = '''select column_name 
                from user_tab_columns 
                where table_name = :tbl_name
                order by column_id
                '''
    cursor.execute(select, tbl_name = table.upper())    # data binding
    r = [i[0] for i in cursor]
    # Cursor은 Tuple을 출력하기 때문에 괄호 제거 위해 index로 뽑기
    return r


def select_all_from(table, cursor):
    select = f'select * from {table.upper()}'
    cursor.execute(select)
    # r = pd.DataFrame([i for i in cursor],
    #                  columns = get_columns_names_of(table, cursor))
    ##
    # data = cursor.fetchall()    # [i for i in cursor]
    ##
    r = pd.DataFrame(cursor)
    r.columns = get_columns_names_of(table, cursor)

    return r


if __name__ == '__main__':
    # 오라클 DB 서버에 접속
    with cx_Oracle.connect(cfg.user, cfg.pw, cfg.dsn) as conn:
        # Cursor 객체 생성
        with conn.cursor() as cursor:
            emp_columns = get_columns_names_of('emp', cursor)
            print(emp_columns)  # ['empno', 'ename', 'job', ... ]

            emp_df = select_all_from('emp', cursor) # pandas.DataFrame
            # 컬럼 이름(인덱스)가 포함 되어 있어야 함
            print(emp_df)

            dept_df = select_all_from('dept', cursor)
            print(dept_df)

            salgrade_df = select_all_from('salgrade', cursor)
            print(salgrade_df)
            print('\n \n')

            # DataFrame에 새로운 컬럼을 추가
            # DataFrame['컬럼 이름'] = list, pandas.Series
            # emp_df에 salgrade 컬럼 추가
            # emp_df['sal']에 대해서 반복:
            # 선택한 행의 sal 값이 salgrade_df 어느 grade에 속하는지 찾음
            # -> salgrade_df 의 행 개수 만큼 반복하면서 LO, HI와 비교
            # -> DataFrame.interrows() 함수 이용

            grade = []
            for i in emp_df['SAL']:
                # print(i)
                for index, row in salgrade_df.iterrows():
                    if row['LOSAL'] <= i <= row['HISAL']:
                        grade.append(row['GRADE'])
                        break

            # print(grade)
            emp_df['SAL_GRADE'] = grade
            print(emp_df)


            # SQL join - pandas.merge
            emp_dept = pd.merge(emp_df, dept_df, on = 'DEPTNO')
            print(emp_dept)

            # pandas.merge(left, right, how, on, left_on, right_on, ...)
            # left, right: 조인할 데이터 프레임
            # how: 조인 방식(inner, left, right)
            # on: 조인할 때 기준이 되는 컬럼 이름
            # 조인의 기준이 되는 컬럼 이름이 데이터 프레임마다 다르면,
            # left_on='left 데이터 프레임 컬럼', right_on='right DF column'

            # emp_df, dept_df 데이터 프레임의 left, right join 결과 비교
            # emp 테이블에서 mgr과 empno가 일치하는 join
            # 1) inner, 2) left, 3) right join
            print('\n inner')
            emp_inner = pd.merge(emp_df, emp_df[['EMPNO', 'ENAME']],
                                 how = 'inner', left_on = 'MGR', right_on = 'EMPNO')
            print(emp_inner)
            print()
            print('\n left')
            emp_left = pd.merge(emp_df, emp_df[['EMPNO', 'ENAME']],
                                how = 'left', left_on = 'MGR', right_on = 'EMPNO')
            print(emp_left)
            print()
            print('\n right')
            emp_right = pd.merge(emp_df, emp_df[['EMPNO', 'ENAME']],
                                 how = 'right', left_on = 'MGR', right_on = 'EMPNO')
            print(emp_right)
            print()
