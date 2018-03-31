#!/usr/bin/python
# -*- coding: UTF-8 -*-
#10.题目：暂停一秒输出，并格式化当前时间。

import time
print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
time.sleep(10)
print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) 
localtime = time.asctime(time.localtime(time.time()))
print "local time :",localtime
