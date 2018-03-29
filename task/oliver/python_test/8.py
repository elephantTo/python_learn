#! /usr/bin/python
def printClcDisp(num):
        list = []
	if num > 9:
		return
	for i in range(1,num + 1):
		list.append(str(i) + "*" + str(num) + "=" + str(i*num))
	print list
	printClcDisp(num + 1)
if __name__ == "__main__":
	printClcDisp(1)

