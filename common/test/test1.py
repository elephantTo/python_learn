#! /usr/bin/python
# -*- coding: UTF-8 -*-
#1.python 函数的参数传递  字典与列表
a = [1,2]

def test(x):
	x.append(2)
	return


if __name__ == "__main__":
	print a
	test(a)
	print a
	
