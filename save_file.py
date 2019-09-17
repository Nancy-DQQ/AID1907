import pymysql
import re


# f = open('dict.txt')

# 链接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='images',
                     charset='utf8')

# 获取游标（操作数据库，执行sql语句，得到执行结果）
cur = db.cursor()

# 执行语句
# with open('0.jpg','rb')as f:
#     data = f.read
#
# sql = 'insert into images values(1,%s,%s)'
# cur.execute(sql,[data,'summer'])
# db.commit()

# 提取图片
sql = "select photo from images where comment = '初恋'"
cur.execute(sql)
data = cur.fetchone()[0]
with open('1.jpg','wb')as f:
    f.write(data)




# try:
#     # 提交到数据库
#     db.commit()
# except:
#     db.rollback()

# 关闭数据库
db.close()

# 关闭游标
cur.close()