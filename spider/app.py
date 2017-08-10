#coding:utf-8
import MySQLdb
import json


class  ViewData(object):
   # time=raw_input("请输入查询时间：")
   # area=raw_input("请输入查询地区：")
    def __init__(self):
        time=raw_input("请输入查询时间：")
        area=raw_input("请输入查询地区：")

        self.times=time
        self.areas=area
        self.select_data(self.times,self.areas)

    def select_data(self,times,areas):
        print  times ,areas
        conn=MySQLdb.connect(host='localhost',
                port=3306,
                user='root',
                passwd='believe2017',
                db='eletric',
                charset='utf8'
                )
        cur=conn.cursor()
        dict={}
        for i in xrange(2,13):
            timet="'"+times+"年"+str(i)+"月"+"'"
            print timet
            sql2="select value from ele_data where area="+"'"+areas+"'"+ "AND time="+"'"+times+"年"+str(i)+"月"+"'"
            print sql2
            cur.execute(sql2)
            month_data=cur.fetchall()
            dict[timet]=month_data
            print dict[timet]
            json.dump(dict,open('json.txt','w'))
        cur.close()
        conn.commit()
        conn.close()




if __name__=='__main__':
    viewdata=ViewData()


