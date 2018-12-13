import pymysql

conn_info = pyodbc.connect(
            'DRIVER={SQL Server};server=localhost;PORT=1433;database=DounbanJUN;user=sa;password=Junrupan9393')
curs = conn_info.cursor()

s = '断背山'
img = '''SELECT imgURL FROM movies  WHERE movieNameCN ='%s' ''' % s
curs.execute(img)
resultimg = curs.fetchone()[0]
print(resultimg)

conn_info.close()
