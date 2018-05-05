# -*- coding: utf-8 -*-
import sqlite3
def search(keyworlds):
	key_worlds=keyworlds.split(u',')
	sql_key_worlds=u'%'.join(key_worlds)
	conn=sqlite3.connect('health.sqlite3')
	sql="select keywords,description,title,url,source from news where keywords like ?"
	cur=conn.cursor()
	cur.execute(sql,(sql_key_worlds,))
	for  r in cur.fetchall():
		print r[0],r[1],r[2],r[3]
	#print len(res)



if __name__ == "__main__":
	search(u"人工智能,AI")