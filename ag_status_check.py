#!/usr/bin/env python
#-*- coding=utf-8 -*-

import urllib2
import json
import sys,os,time
import datetime
import pyodbc

def send(cid,msg):
    url='http://work.weixin.com/RestServices/SendMsgService.svc/SendMsg'
    data={"AppKey":"J3520G","TempId":3,"ClientId":cid,"Content":msg,"IpAddress":"10.10.103.215","Terminal":4}
    headers = {'Content-Type':'Application/json'}
    request = urllib2.Request(url=url,headers=headers,data=json.dumps(data))
    response = urllib2.urlopen(request)
    return response

def mrole():
    cn = pyodbc.connect("dsn=DSN40;UID=checkuser;PWD=passforcheck")
    cur=cn.cursor()
    cur.execute("SELECT role FROM sys.dm_hadr_availability_replica_states  a inner join sys.availability_replicas b  on a.replica_id=b.replica_id where b.replica_server_name=@@servername")
    ck = cur.fetchone()
    c2  = ck[0]
    #print c2
    return c2
    cur.close()
    cn.close()

if __name__ == "__main__":
    cids = '111903'
    mr = mrole()
    atime = datetime.datetime.now()
    msgs = 'the time is  '+atime.strftime('%Y-%m-%d %H:%M:%S')+' ,alwayson ag1 had changed ,please check it! '
    if mr > 1:
        #print 'the server or programs stopped at %s !' % dt
        send(cids,msgs)
    else:
        #print di
        pass
    #rea = send(cids,msgs)
    #print rea
    
