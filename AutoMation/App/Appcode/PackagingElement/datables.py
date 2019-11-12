import pymysql
def datables (URL,ORDER):

    # 打开数据库连接
    db = pymysql.connect("192.168.0.115", "root", "111111", "land")  #:3306    "192.168.0.115", "root", "111111", "land"

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 使用 execute()  方法执行 SQL 查询
    cursor.execute(ORDER)  #"select * from sys_user where id in (1,3,5,8,4)"

    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchall()
    #
    for i in data:
        print(i[2])

    # for ro in data:
    #     count = 0
    #     while count < 17:
    #         print(ro[count])
    #         count = count + 1
    #
    # print("Database version : %s " % data)

    # 关闭数据库连接
    db.close()
