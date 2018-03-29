#!/usr/bin/python


#define function
def function_digui( month_num ):
	if month_num==0 or month_num ==1  :
		x= 1
		return x
	else :
		y=function_digui( month_num -1)+function_digui( month_num -2)
		return y

if __name__ == "__main__":
	for monthes in range(20):
		print "monthes" ,monthes+1 , function_digui( monthes )



