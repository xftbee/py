#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'xufengtao'
import time
import cPickle as pickle
t =time.localtime(time.time())
print t[2],t


print type(t[2])

if t[2] == 30:
    billdate = time.localtime(time.time())
    billfilename='bill'+str(billdate[0])+str(billdate[1])+'.txt'
    with open('card.txt','r') as cardinfo,open(billfilename,'w') as billfile:
        for line in cardinfo.readlines():
            s = line.strip()
            c = s.split('|')
            print c[0],c[3],c[4],type(c[0]),type(c[3])
            user = c[0]
            totalmoney=int(c[3])
            balance=int(c[4])
            bill = totalmoney-balance
            billtxt = user+'你本期账单应还款金额为：'+ str(bill)+'\n'
            billfile.write(billtxt)
            print user,totalmoney,balance,bill
    cardinfo.close()
    billfile.close()


t1 = ('this is a string',32,[322,3,23],None)
t1
p1 = pickle.dumps(t1)
p1
print p1

t2 = pickle.loads(p1)
print t2


a1 = 'apple'
b1 = {1:'one',2:'two',3:'three'}
c1 = [1,3,4,5]
f1 = open('pick.txt','wb')
pickle.dump(a1,f1,True)
pickle.dump(b1,f1,True)
pickle.dump(c1,f1,True)
f1.close()
print '*'*8

f2 = open('pick.txt','rb')
a2 = pickle.load(f2)
b2 = pickle.load(f2)
c2 = pickle.load(f2)

print 'loadload',a2,b2,c2

print "你真的弱爆了"
