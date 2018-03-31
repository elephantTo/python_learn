#! /usr/bin/python
# -*- coding: UTF-8 -*-
#使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。
a = "asdasdsadsadsa"
b = 2

def test(str,int):
	print str
	print int
	return


if __name__ == "__main__":
	test(int = b,str = a)	
