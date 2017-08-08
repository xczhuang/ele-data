#coding:utf-8
import MySQLdb


class  ViewData(object):
    time=input("请输入查询时间：")
    area=input("请输入查询地区：")
    

    def select_data(self,time,area):
        conn=MySQLdb.connect(host='localhost',
                port=3306,
                user='root',
                passwd='believe2017',
                db='eletric',
                charset='utf8'
                )
        cur=conn.cursor()
        for i in xrange(1,13):
            month_data=cur.execute("select time,area,value from ele_data where area=%s AND time=%s",(self.area,self.time+"年"+str(i)+"月"))
        cur.close()
        conn.commit()
        conn.close()
