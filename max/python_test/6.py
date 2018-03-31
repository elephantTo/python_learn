#!/usr/bin/python
# -*- coding: UTF-8 -*-
#斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……
print "please input two number..."
num_1=int(raw_input("num_1="))
num_2=int(raw_input("num_2="))
print num_1
print num_2
for i in range(1,100):
        num_3=num_1+num_2
	num_1=num_2
        num_2=num_3
	print num_3

