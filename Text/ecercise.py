import pymysql


#
class User:
    def __init__(self, database):
        self.db = pymysql.connect(user='root',
                                  password='123456',
                                  database=database,
                                  charset='utf8')
        self.cur = self.db.cursor()

    def register(self, name, passworld):
        sql = 'select * from user where username = %s'
        self.cur.execute(sql, [name])
        r = self.cur.fetchone()  # 查找到说明用户存在
        if r:
            return False
        sql = 'insert into user (username,passworld)values(%s,%s)'
        try:
            self.cur.execute(sql, [name, passworld])
            self.db.commit()
            return True

        except:
            self.db.rollback()

    def login(self, name, passworld):
        sql = 'select * from user where username = %s and passworld = %s'
        self.cur.execute(sql, [name, passworld])
        r = self.cur.fetchone()  # 查找到说明用户存在
        # 查找到则登录成功
        if r:
            return True


if __name__ == '__main__':
    user = User('stu')
    # if user.register('Abby','123'):
    #     print("注册成功")

    if user.login('Abby', '123'):
        print("登陆成功")

# # 链接数据库
# db = pymysql.connect(host = 'localhost',
#                      port = 3306,
#                      user = 'root',
#                      password = '123456',
#                      database = 'user',
#                      charset = 'utf8')
#
# # 获取游标（操作数据库，执行sql语句，得到执行结果）
# cur = db.cursor()
#
# # 执行语句
# sql = "insert into user values(2,'Emma','draw','C',1480.00,'xxxx');"
#
# cur.execute(sql)
#
# # 提交到数据库
# db.commit()
#
# # 关闭数据库
# db.close()
#
# # 关闭游标
# cur.close()
