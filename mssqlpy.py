#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'xuft'

import pymssql
import time

def intval():
    conn = pymssql.connect( host="192.168.18.8" , user="sa", password="Sa!@#321" , database="dbsys")
    cur = conn.cursor()
    cur.execute("create table testvv8(id int identity(1,1) primary key,name varchar(2000),val varchar(1020) ,dt datetime2  not null default getdate())")
    for i in range(100):
        sql = "insert into testvv8(name,val) values( \'"+('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz' + str(i))+"\',\'"+('valabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'+str(i))+"\')"
        print sql
        cur.execute(sql)
        print i
        print time.time()

    print 3
    cur.close()
    conn.commit()


def ainta():
    conn = pymssql.connect( host="192.168.100.202" , user="lyx", password="M123456" , database="dbamonitor" ,charset="utf8")
    cur = conn.cursor()
    sql1 = "select top 100 carvin,repairdate,kilometre,repairtype,rcontent from car2"
    sql2 = "select top 30 carvin,carbrand,carmodel,transmission,col2 from carinfo "
    cur.execute(sql2.encode('utf8'))
    rs = cur.fetchall()
    for c,r,k,rr,rrr in rs:
        print("{} {} {} {} {}".format(c,r,k,rr,rrr))



if __name__ == "__main__":
    start = time.time()
    #intval()
    ainta()
    total=time.time()-start
    print "%d second" % total