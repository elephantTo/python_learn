#!/usr/bin/python

import time
import datetime

day_num_rui = [31,29,31,30,31,30,30,31,30,31,30,31]
day_num_ping = [31,28,31,30,31,30,30,31,30,31,30,31]

a=0
c=0
d=0
data1=0

a ,c ,d = raw_input('yyyy-mm-dd\n').split()

year = int(a)
mon = int(c)
data = int(d)

print year , mon , data

if (year%4==0 and year%100!=0) or (year%100==0 and year%400 ==0) :
	for num in range(0,mon-1):
		data1 = data1 + day_num_rui[num];
	data1 = data1 + data;
else :
	for num in range(0,mon-1):
                data1 = data1 + day_num_ping[num];
        data1 = data1 + data;
print data1

