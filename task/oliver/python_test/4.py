#!/usr/bin/python

#init variable
YMD = raw_input("please input year-month-day\nfor example 20180325\n")
year = YMD[0:4]
year_ = YMD[2:4]
month = YMD[4:6]
day = YMD[6:8]
leapYear = {1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31} 
commonYear = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
num = 0
#define function
def func_isLeapYear(year):
	if int(year_) == 0 and int(year)%400 == 0:
		return True
	elif int(year_) != 0 and int(year)%4 == 0:
		return True
	else:
		return False

if __name__ == "__main__":
	if func_isLeapYear(year):
		if int(day) > leapYear[int(month)] or int(month) > 13:
			print "your input is err"
		for i in range(1,int(month)):
			num += leapYear[i]
                num += int(day)
                print "the count is " + str(num)
	else:
		if int(day) > commonYear[int(month)] or int(month) > 13:
			print "your input is err"
		for k in range(1,int(month)):
                        num += commonYear[k]
                num += int(day)
                print "the count is " + str(num)
