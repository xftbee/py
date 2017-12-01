__author__ = 'xuft'

import MySQLdb as mysql
import urllib2
import sys
import io
import email
import time
import hashlib
import types

def md532(str):
    if type(str) is types.StringType:
        hash=hashlib.md5()
        hash.update(str)
        return hash.hexdigest().upper()
    else:
        return ''

def sha140(str):
    if type(str) is types.StringType:
        aa=hashlib.sha1(str).hexdigest().upper()
        return  aa
    else:
        return ''

conn = mysql.connect(host="192.168.18.133",user="dba",passwd="123456",db="test",charset="utf8")
cursor= conn.cursor()

#r= cursor.execute("create table qiubai(id int,name varchar(20),created int)")

sql = "insert into upasscode1(srcstr,md5str,shastr) values(%s,%s,%s)"
for i in range(1,100000000):
    #param = (i,"jack"+str(i),int(time.time()))
    param = (str(i),md532(str(i)),sha140(str(i)))
    n = cursor.execute(sql,param)
    print n


c = cursor.execute("select * from qiubai")
for row in cursor.fetchall():
    for r in row:
        print r


conn.commit()
cursor.close()
conn.close()




