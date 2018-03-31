#!/usr/bin/python
# -*- coding: UTF-8 -*-
#9.题目：暂停一秒输出。
#使用 time 模块的 sleep() 函数。   time模块

#!/usr/bin/python
# -*- coding: UTF-8 -*-
#import time
# 格式化成2016-03-20 11:45:39形式
#print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
#time.sleep(1)
#print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())


#print "Start %s" % time.ctime()
#time.sleep(5)
#print "Start %s" % time.ctime()

import time
for i in range(1,5):
	print i
	time.sleep(1)

