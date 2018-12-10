import pymysql


conn_info = pymysql.connect(
    "localhost", "test", "testnimabi", "DOUBAN_JUN")
curs = conn_info.cursor()

s = '盖尔 加朵'
castname = '''SELECT  castName FROM casts   WHERE castNameCN ='%s' ''' % s
curs.execute(castname)
resultname = str(curs.fetchall()[0][0])
print(resultname)

conn_info.close()
