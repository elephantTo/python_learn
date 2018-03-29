#!/usr/bin/python

import copy

string = raw_input("please input string \n ")

string_copy =copy.deepcopy(string)

print "this the string _is your _input\n" + string
print "this the string is copy string \n "+ string_copy






