#!/usr/bin/python
# -*- coding: UTF-8 -*-
#11.古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？


months=int(raw_input("please input number of month="))
#print months
def func_rabbits(months):
	if(months==1 or months ==2):
		num_rabbits = 1
		return num_rabbits
	else:
		num_rabbits=func_rabbits(months-1)+func_rabbits(months-2)
                return num_rabbits
print "rabbits total number is = ",func_rabbits(months)




