'''

'''

import cx_Oracle
import lec08_database.oracle_config as cfg

with cx_Oracle.connect(cfg.user, cfg.pw, cfg.dsn, encoding = 'utf-8') as connection:
    with connection.cursor() as cursor:
        