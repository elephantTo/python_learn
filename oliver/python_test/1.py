#!/usr/bin/python
count = 0
for i in range(1,5):
	for j in range(1,5):
        	if j!=i:
			for k in range(1,5):
				if k!=j and k!=i:
					count += 1
					print str(i) + str(j) + str(k)
print count

