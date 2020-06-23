import pymysql




class OperationMysql():
     def __init__(self,host,user,passwd,db,port,charset):
         self.conn_db = pymysql.connect(host=host, user=user, passwd=passwd, db=db, port=port,
                                   charset=charset)
         self.cursor=self.conn_db.cursor()

     '''插入语句'''

     def insert_sql(self,name1,birth1,name2,birth2):
         sql_info="insert into tb_user(userName, birth) value(%s,%s)"
         person_info = [[name1, birth1], [name2, birth2]]
         for i in range(len(person_info)):
             params=tuple(person_info[i])
             self.cursor.execute(sql_info,params)
         self.conn_db.commit()
         self.conn_db.close()

     '''更新语句'''

     def update_sql(self,name,id):
         sql_info="update tb_user set userName='%s' where id='%s'"%(name,id)
         self.cursor.execute(sql_info)
         self.conn_db.commit()
         self.conn_db.close()

     '''查询语句'''

     def select_sql(self):
         datalist=[]
         sql_info="select * from tb_user"
         self.cursor.execute(sql_info)
         data=self.cursor.fetchall()
         for i in range(len(data)):
             datalist.append(data[i])
         self.conn_db.commit()
         self.conn_db.close()
         return datalist

     '''删除语句'''

     def delete_sql(self,id):
         sql_info="delete from tb_user where id='%s'"%(id)
         self.cursor.execute(sql_info)
         self.conn_db.commit()
         self.conn_db.close()



if __name__=="__main__":
    data=OperationMysql(host='172.16.20.145',user='xudt',passwd='Xudt@253',db='test',port=3306,charset='utf8')
    data.insert_sql('丽雪','1997-07-01','张怜','1990-07-01')
    print("sdas")

