import pymysql


conn_info = pymysql.connect(
    "localhost", "test", "testnimabi", "DOUBAN_JUN")
curs = conn_info.cursor()

s = '断背山'
img = '''SELECT imgURL FROM movies  WHERE movieNameCN ='%s' ''' % s
curs.execute(img)
resultimg = curs.fetchone()[0]
print(resultimg)

conn_info.close()
