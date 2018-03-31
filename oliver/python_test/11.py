#! /usr/bin/python
list = [2,2]

def rabbit():
	global list
	list.append(list[len(list) - 1] + list[len(list) - 2])
	if list[len(list)-1] > 999999:
		print list
		return
	rabbit()




if __name__ == "__main__":
	rabbit()

