#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'xuft'

import time
from datetime import datetime
from datetime import timedelta

def prend_mxtime(predate):
	expdate = predate
	today = datetime.now()
	preds = timedelta(days = expdate)
	pred = today + preds
	pd = pred.strftime('%Y-%m-%d')
	uxtime = int(time.mktime(time.strptime(pd,'%Y-%m-%d')))
	#print 'uxtime is ' , uxtime
	return uxtime


if __name__ == "__main__":
	expd = -3
	mt = prend_mxtime(expd)
	print mt
	




