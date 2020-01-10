import pandas as pd

if __name__ == '__main__':
    # csv 파일에서 데이터 프레임을 생성
    emp_df = pd.read_csv('emp_df.csv')
    # print(emp_df.head())
    print(emp_df.iloc[0:5])

    # 부서별, 직책별 직원수를 출력
    emp_by_dept = emp_df.groupby(['DEPTNO', 'JOB'])['EMPNO']
    df = emp_by_dept.agg(직원_수 = 'count')
    print(df)

    unstacked = df.unstack()
    print(unstacked)
    print(unstacked.shape)

    grouped = emp_df.groupby('DEPTNO', as_index = False)
    print(grouped['EMPNO'].count())

    grouped = emp_df.groupby(['DEPTNO', 'JOB'], as_index = False)
    print(grouped['EMPNO'].count())