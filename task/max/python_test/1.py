#!/usr/bin/python
list=[1,2,3,4]
total_number=0
for i in range(1,5):
	for j in range(1,5):
		for z in range(1,5):
			if(i!=j and i!=z and j!=z):
				print i*100+j*10+z
				total_number=total_number+1
print "total_number=",total_number
