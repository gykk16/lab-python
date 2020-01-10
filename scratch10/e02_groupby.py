import csv
from functools import reduce

import pandas as pd

import cx_Oracle

import lec08_database.oracle_config as cfg
from scratch09.e10_sql_pandas import select_all_from

if __name__ == '__main__':
    # with - as 구문을 사용해서 오라클 DB 서버에 접속
    with cx_Oracle.connect(cfg.user, cfg.pw, cfg.dsn) as conn:
        # with - as 구문을 사용해서 Cursor 객체를 생성
        with conn.cursor() as cursor:
            # scratch09 패키지에서 작성한 테이블 전체 검색 함수를 사용해서,
            # emp_df 데이터 프레임을 생성
            emp_df = select_all_from('emp', cursor)

            # emp_df 를 csv 파일로 저장
            emp_df.to_csv('emp_df.csv', sep = ',', encoding = 'UTF-8', index = False)

            # emp_df 에서 부서별 평균 급여를 출력
            print('\n=== emp_df 에서 부서별 평균 급여를 출력 ===')
            grouped_by_deptno = emp_df.groupby('DEPTNO')
            grouped_by_deptno_sal_mean = grouped_by_deptno['SAL'].mean()
            print(grouped_by_deptno_sal_mean)
            print('')

            # emp_df 에서 부서별 인원수를 출력
            print('\n=== emp_df 에서 부서별 인원수를 출력 ===')
            grouped_by_deptno_count = grouped_by_deptno['SAL'].count()
            print(grouped_by_deptno_count)

            # emp_df 에서 부서별 급여 최소값
            print('\n=== emp_df 에서 부서별 최소값 ===')
            grouped_by_deptno_minsal = grouped_by_deptno['SAL'].min()
            print(grouped_by_deptno_minsal)

            # emp_df 에서 부서별 급여 최대값
            print('\n=== emp_df 에서 부서별 최대값 ===')
            grouped_by_deptno_maxsal = grouped_by_deptno['SAL'].max()
            print(grouped_by_deptno_maxsal)

            # 위의 결과를 한개의 데이터프레임으로 출력
            print('\n=== 위의 결과를 한개의 데이터프레임으로 출력 ===')
            emp_dfs = [grouped_by_deptno_sal_mean, grouped_by_deptno_count, grouped_by_deptno_minsal, grouped_by_deptno_maxsal]
            emp_df_merged = reduce(lambda left, right: pd.merge(left, right, on = 'DEPTNO'), emp_dfs)
            emp_df_merged.columns = ['SAL_MEAN', 'DEPT_POP', 'SAL_MIN', 'SAL_MAX']
            print(emp_df_merged)
            print()
            #######################

            df = pd.DataFrame({
                'mean': grouped_by_deptno_sal_mean,
                'count': grouped_by_deptno_count,
                'min': grouped_by_deptno_minsal,
                'max': grouped_by_deptno_maxsal
            })
            print(df)
            print()
            #######################

            df = grouped_by_deptno['SAL'].agg(['mean', 'count', 'min', 'max'])
            print(df)


            # emp_df 에서 직책별 직원 수, 급여 평균, 최소, 최대값을 출력
            print('\n=== emp_df 에서 직책별 직원 수, 급여 평균, 최소, 최대값을 출력 ===')
            emp_by_job = emp_df.groupby('JOB')

            emp_by_job_count = emp_by_job['SAL'].count()
            emp_by_job_mean = emp_by_job['SAL'].mean()
            emp_by_job_min = emp_by_job['SAL'].min()
            emp_by_job_max = emp_by_job['SAL'].max()

            emp_dfs2 = [emp_by_job_mean, emp_by_job_count, emp_by_job_min, emp_by_job_max]

            emp_df_merged2 = reduce(lambda left, right: pd.merge(left, right, on = 'JOB'), emp_dfs2)
            emp_df_merged2.columns = ['SAL_MEAN', 'DEPT_POP', 'SAL_MIN', 'SAL_MAX']
            print(emp_df_merged2)

            ###############
            sal_by_job = emp_df.groupby('JOB')['SAL']
            print(sal_by_job.agg(['count', 'mean', 'min', 'max',
                                  lambda x: x.max() - x.min()]))

            # emp_df 에서 부서별, 직책(job)별 직원 수, 급여 평균, 최소, 최대값을 출력
            print('\n=== emp_df 에서 부서별, 직책(job)별 직원 수, 급여 평균, 최소, 최대값을 출력 ===')
            grouped_by_deptnojob = emp_df.groupby(['DEPTNO', 'JOB'])
            grouped_by_deptnojob_count = grouped_by_deptnojob['ENAME'].count()
            grouped_by_deptnojob_mean = grouped_by_deptnojob['SAL'].mean()
            grouped_by_deptnojob_min = grouped_by_deptnojob['SAL'].min()
            grouped_by_deptnojob_max = grouped_by_deptnojob['SAL'].max()

            emp_dfs3 = [grouped_by_deptnojob_mean, grouped_by_deptnojob_count, grouped_by_deptnojob_min, grouped_by_deptnojob_max]

            emp_df_merged3 = reduce(lambda left, right: pd.merge(left, right, on = ['DEPTNO', 'JOB']), emp_dfs3)
            emp_df_merged3.columns = ['SAL_MEAN', 'DEPT_POP', 'SAL_MIN', 'SAL_MAX']
            print(emp_df_merged3)

            sal_by_dept_job = emp_df.groupby(['DEPTNO', 'JOB'])['SAL']
            df = sal_by_dept_job.agg(dept_pop = 'count',
                                     sal_mean = 'mean',
                                     sal_min = 'min',
                                     sal_max = 'max')
            print(df)





