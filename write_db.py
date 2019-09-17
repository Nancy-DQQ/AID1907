"""
write_db.py
pymysql 写操作演示(insert update delete)
"""

import pymysql

# 链接数据库
db = pymysql.connect(user = 'root',
                      password = '123456',
                      database = 'class',
                      charset = 'utf8')

# 获取游标
cur = db.cursor()

# 执行sql语句
name = input("name:")
age = int(input("age:"))
score = float(input("score:"))

try:
    # 插入操作
    # 合成一个正确的sql语句才能正确commit
    # sql = "insert into class (name,age,score) values ('%s',%d,%f);"%(name,age,score)
    #
    # cur.execute(sql) # 执行语句
    # db.commit()  # 同步数据库

    # sql语句值参量可以通过execute传入
    # sql = 'insert into class_1(name,age,score)values(%s,%s,%s)'
    # sur.execute(sql,[name,age,score]) # 执行语句
    # db.commit() # 同步数据库

    # 修改操作
    sql = "update class set score = 91 where name = 'Abby';"
    cur.execute(sql)

    # 删除操作
    sql = "delect from class where name = 'Jame';"
    cur.execut(sql)
    db.commit() # 同步数据库


except Exception as e:
    print(e)
    db.rollback() # 回滚到没有commit之前的状态


db.close()
cur.close()