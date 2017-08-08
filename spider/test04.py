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
		self.fileName = 'result.txt'
		self.saveFile(self.fileName, self.proxyList)
	def getUrls(self):
		urls = []
                provinces=[u"安徽",u"上海",u"江苏",u"浙江",u"北京",u"河南"]
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
                    re=urllib2.urlopen(url,timeout=3)
                    jn=json.load(re)
                    try:
                        for da in jn["result"]:
                            if da["zb"]=="发电量_累计值(亿千瓦小时)":
                                item=Item()
                                item.value= da["data"]
                                item.time= da["sj"]
                                print da["data"]
                                print da["reg"]
                                item.area= da["reg"]
                                item.kpi= da["zb"]
                                proxyList.append(item)
                    except:
                           traceback.print_exc(file=sys.stdout)
                return proxyList
         
        def saveFile(self, fileName, proxyList):
            with open(fileName, 'w') as fp:
                for item in proxyList:
                    fp.write(item.kpi + '\t')
                    
                    fp.write(item.area + '\t')
                    fp.write(item.time + '\t')
                    fp.write(item.value + '\n')
                        
				
if __name__ == '__main__':

    	GP = GetProxy()
