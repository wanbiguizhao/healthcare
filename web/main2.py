# -*- coding: UTF-8 -*- 
import web
import sys
import sqlite3
reload(sys)
sys.path.append("..")
sys.setdefaultencoding('utf-8')
sys.path.append("..")
#from ml.Search import Search

render = web.template.render('web/templates/')

def dbconn():
	conn=sqlite3.connect('health.sqlite3')
	return conn

def search(keyworlds):
	key_worlds=keyworlds.split(u',')
	sql_key_worlds=u'%'.join(key_worlds)
	conn=sqlite3.connect('health.sqlite3')
	sql="select keywords,description,title,url,source,author from news where keywords like ?"
	cur=conn.cursor()
	cur.execute(sql,(sql_key_worlds+u'%',))
	newslist=[]
	for  r in cur.fetchall():
		news={'keywords':r[0],'description':r[1],'title':r[2],'url':r[3],'source':r[4],'author':r[5]}
		newslist.append(news)
	return newslist




urls=(
	"/","index",
	"/news","news"
)

app = web.application(urls,globals())

class index:
	def __init__(self):
		#self.se = Search()
		pass
	def GET(self):
		data = web.input()
		if data:
			print data
			searchword = data.searchword
		else:
		 	searchword = ''
		newslist=list()
		if searchword:
			newslist = search(searchword.replace('，',',').replace('|',',').replace('|',','))#self.se.QueryByTime(searchword)
			print newslist[0]
		return render.index(searchword,newslist)
	
# -*- coding: utf-8 -*-
class news:
	def __init__(self):
		self.se = Search()
	def GET(self):
		data = web.input()
		if data:
			ID = data.id
		else:
		 	ID=''
		news = self.se.QueryById(ID)
		return render.news(news)

if __name__ == "__main__":
	app = web.application(urls,globals())
	app.run()
