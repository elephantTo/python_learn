#! /usr/bin/python
# -*- coding: utf-8 -*-
def handleOperationList(list):
    if len(list) == 1:
        if float(list[0]) - int(float(list[0])) != 0:
            return float(list[0])
        else:
            return int(float(list[0]))
    for num in range(0, len(list)):
        if (list[num] == "*") or (list[num] == "/"):
            if list[num] == "*":
                count = float(list[num - 1]) * float(list[num + 1])
                list.insert(num-1,str(count))
                del list[num:num+3]
                print list
                handleOperationList(list)
                return handleOperationList(list)
            elif list[num] == "/":
                count = float(list[num - 1]) / float(list[num + 1])
                list.insert(num-1,str(count))
                del list[num:num+3]
                print list
                handleOperationList(list)
                return handleOperationList(list)
    for num in range(0, len(list)):
        if (list[num] == "+") or (list[num] == "-"):
            if list[num] == "+":
                count = float(list[num - 1]) + float(list[num + 1])
                list.insert(num-1,str(count))
                del list[num:num+3]
                print list
                handleOperationList(list)
                return handleOperationList(list)
            elif list[num] == "-":
                count = float(list[num - 1]) - float(list[num + 1])
                list.insert(num-1,str(count))
                del list[num:num+3]
                print list
                handleOperationList(list)
                return handleOperationList(list)

                
            
            
    