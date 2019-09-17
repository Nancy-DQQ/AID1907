import pymysql
import re


f = open('dict.txt')

# 链接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='dict',
                     charset='utf8')

# 获取游标（操作数据库，执行sql语句，得到执行结果）
cur = db.cursor()

# 执行语句
sql = 'insert into words (word,mean)values(%s,%s)'

for line in f:
    # tmp = line.split(' ',1)
    # world = tmp[0]
    # mean = tmp[1].strip()
    # cur.execute(sql,[world,mean])

    #　正则
    tup = re.findall(r'(\S+)\s+(.*)',line)[0]
    cur.execute(sql,tup)


try:
    # 提交到数据库
    db.commit()
except:
    db.rollback()

# 关闭数据库
db.close()

# 关闭游标
cur.close()