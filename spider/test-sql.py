#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'hstking hstking@hotmail.com'
import urllib2
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import json
import traceback
import requests
import MySQLdb
#from selenium import webdriver
#from myLog import MyLog as mylog

class Item(object):
	kpi = None
	area = None
	time = None
        value=None
        column=None
class GetProxy(object):
	def __init__(self):
                self.startUrl = 'http://data.stats.gov.cn/search.htm?s='
#		self.log = mylog()
                self.urls = self.getUrls()
		self.proxyList = self.getProxyList(self.urls)
		self.fileName = 'error.txt'
		self.saveFile( self.proxyList)
	def getUrls(self):
		urls = []
                provinces=[u"安徽",u"上海",u"江苏",u"浙江",u"北京",u"河南",u"天津",u"重庆",u"河北",u"山西",u"辽宁",u"吉林",u"黑龙江",u"江苏",u"浙江",u"福建",u"江西",u"山东",u"河南",u"湖北",u"湖南",u"广东",u"海南",u"四川",u"贵州",u"云南",u"陕西",u"甘肃",u"青海",u"内蒙古",u"台湾",u"广西",u"西藏",u"宁夏",u"新疆",u"香港",u"澳门"]
                for province in provinces:
		    for i in xrange(1978,2018):
                        for j in xrange(0,3):
                            url = self.startUrl + province+str(i)+u"发电量"+"&m=searchdata&p="+str(j)
			    print url
                            urls.append(url)
                        
		return urls    

        def getProxyList(self, urls):
	    	proxyList=[]
              #  item=Item()
                for url in urls:
                    re=urllib2.urlopen(url)
                    jn=json.load(re)
                    try:
                        for da in jn["result"]:
                            if da["zb"]=="发电量_累计值(亿千瓦小时)":
                                if da["data"]!="":
                                    item=Item()
                                    item.value= da["data"]
                                    item.time= da["sj"]
                                    print da["data"]
                                    print da["reg"]
                                    item.area= da["reg"]
                                    item.kpi= da["zb"]
                                    proxyList.append(item)
                                else:
                                    '''with open(fileName,'w') as fp:
                                        for i in xrange(0,):
                                            fp.write(str(i)+item.time+item.area+"数据为空")'''
                                    for j in xrange(0,):
                                        print str(j)+item.time+item.area+"数据为空"
                    except:
                           traceback.print_exc(file=sys.stdout)
                return proxyList
        '''
        def saveFile(self, fileName, proxyList):
            with open(fileName, 'w') as fp:
                for item in proxyList:
                    fp.write(item.kpi + '\t')
                    
                    fp.write(item.area + '\t')
                    fp.write(item.time + '\t')
                    fp.write(item.value + '\n')
                        
	'''
        def saveFile(self,proxyList):
            conn=MySQLdb.connect(host='localhost',
                    port=3306,
                    user='root',
                    passwd='believe2017',
                    db='eletric',
                    charset='utf8')
            cur=conn.cursor()
            for item in proxyList:
                cur.execute("insert into ele_data(kpi,area,time,value) values(%s,%s,%s,%s)",(item.kpi,item.area,item.time,item.value))
            cur.close()
            conn.commit()
            conn.close()
if __name__ == '__main__':

    	GP = GetProxy()
