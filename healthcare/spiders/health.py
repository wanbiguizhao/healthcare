# -*- coding: utf-8 -*-
import scrapy

import json
import time 
import re
import json
import sys
import json
from healthcare.items import HealthcareItem
import sqlite3
def dbconn():
	conn=sqlite3.connect('health.sqlite3')
	return conn

class HealthSpider(scrapy.Spider):
	name = 'health'
	allowed_domains = ['www.healthcare.com']
	start_urls = ['http://www.healthcare.com/']
	nextpage=1
	size=20
	count=0
	
	def start_requests(self):
		print "hehes"
		#print self.start_urls[0]
		scrapy.Request(url=self.start_urls[0],callback=self.startParse)
		print self.count
		while self.nextpage*self.size<40000:

			url="https://www.cn-healthcare.com/api/article/articlelist?data={%22start%22:%22"+str(self.nextpage)+"%22,%22size%22:%22"+str(self.size)+"%22,%22arctype%22:%220%22}"
			self.nextpage=self.nextpage+1
			#print url
			yield scrapy.Request(url=url,callback=self.parse)

	def startParse(self,url):
		jsonresponse = json.loads(response.body_as_unicode(),encoding="utf-8")
		self.count=int(jsonresponse['count'])

	def parse(self,response):
		jsonresponse = json.loads(response.body_as_unicode(),encoding="utf-8")
		#print(len(jsonresponse['data']))
		items=[]
		for ele_data in  jsonresponse['data']:
			item= HealthcareItem()
			item['id']= ele_data['id']
			item['keywords']= ele_data['keywords']
			item['description']= ele_data['description']
			item['url']= ele_data['url']
			item['title']= ele_data['title']
			item['source']= ele_data.get('source','---')
			item['content']= ele_data.get('content','---')
			item['author']= ele_data.get('author','---')
			db=dbconn()
			cur=db.cursor()
			cur.execute(" insert into news(id,keywords,description,url,title,source,content,author)values(?,?,?,?,?,?,?,? ) ",(
					item['id'],item['keywords'],item['description'],item['url'],item['title'],
					item['source'],item['content'],item['author']
				))
			db.commit()
			cur.close()
			items.append(item)
		#print(self.nextpage)
		#print jsonresponse['count']
		return items

