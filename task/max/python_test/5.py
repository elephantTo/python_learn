#!/usr/bin/python
# -*- coding: UTF-8 -*-
#5.输入三个整数x,y,z，请把这三个数由小到大输出。
print "please input x,y,z..."
x=int(raw_input("x="))
y=int(raw_input("y="))
z=int(raw_input("z="))
if x>y and x>z:
	num_max=x
	if y>z:
		num_mid=y
		num_min=z
	else:
		num_mind=z
		num_min=y
elif y>x and y>z:
	num_max=y
	if x>z:
		num_mid=x
		num_min=z
	else:
		num_mid=z
                num_min=x
else:
	num_max=z
	if x>y:
                num_mid=x
                num_min=y
        else:
                num_mid=y
                num_min=x
print num_min, num_mid,num_max

