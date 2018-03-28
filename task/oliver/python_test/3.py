#!/usr/bin/python
num = 0
while(1):
	num += 1	
	num_1 = (num + 100) ** 0.5
	num_2 = (num + 268) ** 0.5
	if num_1 - int(num_1) <= 0 and num_2 - int(num_2) <= 0:
                print str(num) + '\n'
                if num > 100000:
                	break
