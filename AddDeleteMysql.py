import pymysql



# 打开数据库连接
conn_db=pymysql.connect(host='172.16.20.145',user='xudt',passwd='Xudt@253',db='test',port=3306,charset='utf8')

# 获取游标
cursor=conn_db.cursor()

#使用execute执行SQL语句
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取一条数据
data=cursor.fetchone()


#输出语句
print(type(data))
print("Database version :{}".format(data))


# -----插入语句-----

# insert_sql="insert into tb_user(userName, birth) value(%s,%s)"
#
# person_info=[['罗伊','1994-12-12'],['李小海','1991-09-22']]
#
# for i in range(len(person_info)):
#     param=tuple(person_info[i])
#     data=cursor.execute(insert_sql,param)
#     if data>0:
#         print("添加数据成功！\n")
# #提交事务
# conn_db.commit()
# conn_db.close()



# -----改写语句-----
# person_info=('杨密','2')
# params=tuple(person_info)
# print(params)
# update_sql="update tb_user set userName='%s' where id='%s'"%('范冰冰','3')
#
# cursor.execute(update_sql)
# conn_db.commit()
# conn_db.close()


# -----查询语句-----
#
# select_sql="select * from tb_user"
#
# cursor.execute(select_sql)
# #获取所有数据
# data=cursor.fetchall()
# for i in range(len(data)):
#     print(data[i])
#
#
# select_sql1="select id,userName from tb_user where id=%s"%('2')
#
# cursor.execute(select_sql1)
# #获取所有数据
# data1=cursor.fetchone()
# print(data1)
#
#






# -----删除语句-----

delete_sql="delete from tb_user where id='%s' "%(5)
cursor.execute(delete_sql)

select_sql="select * from tb_user"

cursor.execute(select_sql)
#获取所有数据
data=cursor.fetchall()
for i in range(len(data)):
    print(data[i])
conn_db.commit()
conn_db.close()

person_info=[['罗伊','1994-12-12'],['李小海','1991-09-22']]
print(type(person_info))