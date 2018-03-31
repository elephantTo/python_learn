#!/usr/bin/python
year=int(raw_input("year="))
print "year=",year
month=int(raw_input("month="))
print "month=",month
data=int(raw_input("data="))
print "data=",data
#list=[0,31,59,90,121,151,182,212,243,274,304,335,365]
#if (year%400==0) or( year%4==0 and year%100!=0):
#	leap=1
#else:
#	leap=0
#if leap==1:
#	print "day_number",list[month-1]+data+1
#else:
#	print "day_number",list[month-1]+data
list1=[0,31,28,31,30,31,30,31,30,31,30,31,30,31]
list2=[0,31,29,31,30,31,30,31,30,31,30,31,30,31]

day_number=0
if (year%400==0) or (year%4==0 and year%100!=0):
	leap=1
else:
	leap=0
if leap==1:
	for month_num in range(month):
		day_number=day_number+list2[month_num]
else:
       for month_num in range(month):
                day_number=day_number+list1[month_num]
print "day_number",day_number+data



