#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'hstking hstking@hotmail.com'


from selenium import webdriver
from myLog import MyLog as mylog


class Item(object):
	kpi = None
	area = None
	time = None
        value=None
        column=None
class GetProxy(object):
	def __init__(self):
                self.startUrl = 'http://data.stats.gov.cn/search.htm?s='
		self.log = mylog()
		self.urls = self.startUrl
		self.proxyList = self.getProxyList(self.urls)
		self.fileName = 'data.txt'
		self.saveFile(self.fileName, self.proxyList)
	def getUrls(self):
		urls = []
                provinces=['安徽','上海','江苏','浙江','北京','河南']
                for province in provinces:
		    for i in xrange(1999,2001):
			url = self.startUrl + province+str(i)+'发电量'
			print url
                        urls.append(url)
                        
#                        self.log.info('get url %s to urls' %url)
		return urls    

        def getProxyList(self, urls):
		browser = webdriver.PhantomJS()
		proxyList = []
		item = Item()
		for url in urls:
			browser.get(url)
			browser.implicitly_wait(5)
			elements = browser.find_elements_by_xpath('//tbody/tr')
			for element in elements:
				item.kpi = element.find_element_by_xpath('./td[1]').text.encode('utf8')
                                print item.kpi
				item.area = element.find_element_by_xpath('./td[2]').text.encode('utf8')
                                print item.area
				item.time = element.find_element_by_xpath('./td[3]').text.encode('utf8')
                                print item.time
				item.value = element.find_element_by_xpath('./td[4]').text.encode('utf8')
                                print item.value
				item.column = element.find_element_by_xpath('./td[5]').text.encode('utf8')
				proxyList.append(item)
				self.log.info('add proxy %s:%s to list' %(item.area, item.value))
		browser.quit()
		return proxyList

	def saveFile(self, fileName, proxyList):
		self.log.info('add all proxy to %s' %fileName)
		with open(fileName, 'w') as fp:
			for item in proxyList:
				fp.write(item.kpi + '\t')
                                print 'hello'
				fp.write(item.area + '\t')
				fp.write(item.time + '\t')
				fp.write(item.value + '\t')
				fp.write(item.column + '\t')
				

if __name__ == '__main__':
	GP = GetProxy()
