#coding:utf-8
import MySQLdb


class  ViewData(object):
    time=input("请输入查询时间：")
    area=raw_input("请输入查询地区：")
    def __init__(self):
        self.tim="2001年1月"
        self.are="安徽省"
        self.select_data(self.tim,self.are)

    def select_data(self,tim,are):
        conn=MySQLdb.connect(host='localhost',
                port=3306,
                user='root',
                passwd='believe2017',
                db='eletric',
                charset='utf8'
                )
        cur=conn.cursor()
        #for i in xrange(1,13):
        times="2011年3月"
        areas="安徽省"
        sql1="select * from ele_data where area=\"安徽省\" AND time=\"2001年3月\""
        print sql1
        sql2="select * from ele_data where area="+"'"+areas+"'"+ "AND time="+"'"+times+"'"
        print sql2
        sql="select * from ele_data "
        cur.execute(sql2)
        month_datas=cur.fetchall()
        for month_data in month_datas:
            print month_data

        cur.close()
        conn.commit()
        conn.close()




if __name__=='__main__':
    viewdata=ViewData()


