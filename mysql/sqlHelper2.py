# -*- coding:utf-8 -*-

#查询数据
import pymysql

#创建连接
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db='test')

#创建游标 以字典的类型
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

#执行sql,返回受到影响的行数
effectRow = cursor.execute("select* from users")

#获取所有数据
# result = cursor.fetchall()
# print(result)

#获取第一条数据
# result = cursor.fetchone()  #获取第一条数据
# print(result)
# result = cursor.fetchone()  # 除掉之前那条的第一条数据（第二条）
# print(result)
# result = cursor.fetchone()  # 除掉之之前那条的第一条数据（第三条）（迭代；依次类推）
# print(result)

# result = cursor.fetchmany(3)  # 依次拿多个
# print(result)

# result = cursor.fetchone()
# cursor.scroll(-1, mode="relative")  # relative相对移动:相对当前位置移动

cursor.scroll(1, mode="absolute")  # absolute绝对移动:相对绝对位置移动
result = cursor.fetchone()
print(result)

# 关闭游标
cursor.close()

# 关闭连接
conn.close()