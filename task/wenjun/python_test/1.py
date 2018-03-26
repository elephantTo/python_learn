#!/usr/bin/python

data_list=[1,2,3,4]

for num in range(0,4):
	for num1 in range(0,4):
		for num2 in range(0,4):
			if data_list[num] != data_list[num1] and data_list[num] != data_list[num2] and data_list[num1] != data_list[num2]:
				data_num=data_num+1;
				aa=data_num
				print str(data_list[num])+ str(data_list[num1]) +  str(data_list[num2])
print aa
