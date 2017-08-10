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
		self.fileName = '2017/8/4.txt'
		self.saveFile(self.fileName, self.proxyList)
	def getUrls(self):
		urls = []
                provinces=[u"安徽",u"上海",u"江苏",u"浙江",u"北京",u"河南"]
                for province in provinces:
		    for i in xrange(1999,2001):
                        url = self.startUrl + province+str(i)+u"发电量"+"&m=searchdata&p="+str(0)
			print url
                        urls.append(url)
                        
		return urls    

        def getProxyList(self, urls):
		for url in urls:
                    re=urllib2.urlopen(url,timeout=3)
                    jn=json.load(re)
                    try:
                        for da in jn["result"]:
                            data=da["data"]
                            print data
                            print da["sj"]
                            print da["reg"]
                            print da["zb"]

                        print(u'共几类:'+str(len(data)))
                    except:
                        traceback.print_exc(file=sys.stdout)
	                		
                       
                        
				
if __name__ == '__main__':

    	GP = GetProxy()
