#!/usr/bin/python
# -*- coding: UTF-8 -*-
#7.将一个列表的数据复制到另一个列表中。

#list = []          ## 空列表
#list.append('Google')   ## 使用 append() 添加元素
#list.append('Runoob')
#print list

list1 =[1,2,3,4,5]
list2=[5,6,7]
for i in range(len(list1)):
	list2.append(list1[i])
print list2
