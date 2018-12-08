import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "mikumikuliu1234", "DOUBAN_JUN")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
sql = "select castName from casts where castId = 001"
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchone()
    print(results)
except:
    print ("Error: unable to fetch data")

# 关闭数据库连接
db.close()
