# -*- coding:utf-8 -*-

#修改和删除数据

import pymysql

#创建连接
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db='test')

#创建游标
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

#执行sql，返回受到影响到行数  cursor.executemany表示多条 占位符 不管什么类型都是%s
# effectRow = cursor.execute("update users set password = %s where id = %s",
#                            ("123456", "2"))
effectRow = cursor.execute("delete from users where id = %s","2")  #删除数据
print("effectRow:%d" % effectRow)
# 提交，不然无法保存新建或者修改的数据
conn.commit()

# 关闭游标
cursor.close()

# 关闭连接
conn.close()
