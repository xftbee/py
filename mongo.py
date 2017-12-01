#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'xuft'
import time
from pymongo import *
client = MongoClient("192.168.103.215",6000)
db = client.checklist
start = time.time()
collection=db.users
for i in collection.find():
	print i
total = time.time()-start
print "%d second" % total

