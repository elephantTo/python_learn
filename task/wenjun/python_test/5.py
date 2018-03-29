#!/usr/bin/python

x,y,z = raw_input("please input three num ,for example 1 2 3\n").split()

list_xyz = [int(x), int (y) ,int(z)]

if x==y or x==z or y==z :
	print "your input is wrong , please again input:"
else :
	if list_xyz[0] < list_xyz[1] :
		if list_xyz[0] < list_xyz[2] :
			a1 = list_xyz[0]
			if list_xyz[1] < list_xyz[2] :
				a2 = list_xyz[1]
				a3 = list_xyz[2]
			else :
				a3 = list_xyz[1]
				a2 = list_xyz[2]
		else :
			a1 = list_xyz[2]
			a2 = list_xyz[0]
			a3 = list_xyz[1]
	else :
		if list_xyz[0] < list_xyz[2] :
		 	a1 = list_xyz[1]
			a2 = list_xyz[2]
			a3 = list_xyz[0]	
		else :
			if list_xyz[1] < list_xyz[2] :
				a1 = list_xyz[1]
				a2 = list_xyz[2]
				a3 = list_xyz[0]
			else :
				a1 = list_xyz[2]
				a2 = list_xyz[1]
				a3 = list_xyz[0]
	print a1,a2,a3
				
					

		







