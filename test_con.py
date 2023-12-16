import cx_Oracle 
'''
conn = 'C##PL_SQL/rayen@localhost:1521/orcl'
conn = f''
conn = cx_Oracle.connect(conn) 
cur = conn.cursor()
print('succcessfully connected') 
'''
user="C##PL_SQL"
password="rayen"
dsn="localhost:1521"
sid = 'orcl'
connection_string = f'{user}/{password}@{dsn}/{sid}'
conn = cx_Oracle.connect(
            connection_string) 
