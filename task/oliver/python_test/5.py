#! /usr/bin/python

import re
str_threeNum = raw_input("please input three number, such as: 20 300 50\n")
pattern = re.compile('[0-9]+ ?')
mylist = pattern.findall(str_threeNum)
def maxNum(list):
        global average
        average = 0
        global saveList
        saveList = []
        print "len :" + str(len(list))
	if len(list) == 1:
                print  "the max is :" + str(list)
		return list
	for num in list:
		average += int(num)/len(list)
	print "aver :" + str(average)
	for num in list:
		if num > average:
			saveList.append(int(num))
        print saveList
	maxNum(saveList)
if __name__ == "__main__":
        maxNum(mylist)
	
		
