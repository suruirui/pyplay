# -*- coding:utf-8 -*-

#python3版本使用pymysql库操作数据库
#插入数据
import pymysql

#创建连接
conn = pymysql.connect(  # 参数依次：数据库IP、数据库用户名、数据库密码、数据库名
    host='127.0.0.1',
    user='root',
    passwd='root',
    db='test')

# 创建游标以字典的类型
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# 执行sql，并返回受到的影响行数

effect_row = cursor.execute("insert into users(username,password,age) values('rose', '8888',20) ")   # 引号内写SQL语句，python就执行
print("effect_row:%d"%effect_row)

# 提交，不然无法保存新建或者修改的数据
conn.commit()

# 关闭游标
cursor.close()

# 关闭连接
conn.close()
