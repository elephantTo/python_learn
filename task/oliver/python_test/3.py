#!/usr/bin/python

num_str = raw_input("pelase a num\n")
num = int(num_str)

output = num ** 0.5

if output - int(output) <= 0:
	print output
else:
	print "This number can't be squared."

