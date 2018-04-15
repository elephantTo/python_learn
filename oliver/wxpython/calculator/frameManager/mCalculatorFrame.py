#! /usr/bin/python
# -*- coding: utf-8 -*-

import numpy
from misc import array_calculator
from wxpythonMakeFrame import calculatorFrame

class mCalculatorFrame(calculatorFrame.CalculatorFrame):
    # value
    m_ShowList = []
    m_OperationList = []
    m_bList2IsSetValue = 0
    m_text2RealValue = []
    def __init__(self, parent = None, updateFrame = None):
        calculatorFrame.CalculatorFrame.__init__(self, parent = None)
        self.updateFrame = updateFrame
    # UI：control setText2Value or appendText2Value
    def getIsSetText2Value(self):
        return self.m_bList2IsSetValue
    def setIsSetText2Value(self, isTure):
        m_bList2IsSetValue = int(isTure)
    # save UI and RealValue about text1
    def saveList1(self, showListValue, operationListValue):
        if showListValue.strip() == '':
            return
        self.m_ShowList.append(str(showListValue))
        self.m_OperationList.append(str(operationListValue))
        print self.m_OperationList
    def getOperationList(self):
        return self.m_OperationList
    def getShowList(self):
        return self.m_ShowList()
    def flushList1(self):
        self.m_ShowList = []
        self.m_OperationList = []
    def showText1(self):
        self.m_textCtrl2.SetValue("")
        for value in self.m_ShowList:
            self.m_textCtrl2.AppendText(value)
            self.m_textCtrl2.AppendText(" ")
    def flushText1(self):
        self.m_textCtrl2.SetValue("")
    def insertList2(self, value):
        self.m_text2RealValue.append(str(value))
    def setList2(self, value):
        self.m_text2RealValue = []
        self.m_text2RealValue.append(str(value))
    def flushList2(self):
        self.m_text2RealValue = []
    def deleteList2(self):
        self.m_text2RealValue= self.m_text2RealValue[:-1]
    def getList2(self):
        return ''.join(self.m_text2RealValue)
    def showText2(self):
        self.m_textCtrl3.SetValue(self.getList2())
    def flushText2(self):
        self.m_textCtrl3.SetValue("")
    def gotoMainFrame(self, event):
        self.updateFrame("main")
    def handleNum(self, event):
            if self.getIsSetText2Value():
                self.setIsSetText2Value(False)
                self.m_textCtrl2.Clear()
                self.insertList2(self.FindWindowById(event.GetId()).GetLabel())
                self.showText2()
            else:
                self.insertList2(self.FindWindowById(event.GetId()).GetLabel())
                self.showText2()
    def handleOperator(self, event):
        self.setIsSetText2Value(True)
        if (event.GetId() == self.button_SQR.GetId()):
            num = int(self.getList2())
            self.setList2(str(numpy.square(num)))
            self.showText2()
            self.saveList1("sqr(" + str(num) + ")", str(self.getList2()))
            self.showText1()
            self.flushList2()
        elif (event.GetId() == self.button_REC.GetId()):
            num = int(self.m_textCtrl3.GetValue())
            self.setList2(str(1/float(num)))
            self.showText2()
            self.saveList1("1/(" + str(num) + ")", str(self.getList2()))
            self.showText1()
            self.flushList2()
        elif (event.GetId() == self.button_SQU.GetId()):
            num = int(self.m_textCtrl3.GetValue())
            self.setList2(str(numpy.sqrt(num)))
            self.showText2()
            self.saveList1("√/(" + str(num) + ")", str(self.getList2()))
            self.showText1()
            self.flushList2()
        elif (event.GetId() == self.button_DEL.GetId()):
            self.deleteList2()
            self.showText2()
        elif (event.GetId() == self.button_CE.GetId()):
            self.flushList2()
            self.showText2()
        elif (event.GetId() == self.button_C.GetId()):
            self.flushList1()
            self.flushList2()
            self.showText1()
            self.showText2()
        elif (event.GetId() == self.button_ADD.GetId()):
            self.saveList1(self.getList2(),self.getList2())
            self.saveList1("+", "+")
            self.showText1()
            self.flushList2()
        elif (event.GetId() == self.button_SUB.GetId()):
            self.saveList1(self.getList2(), self.getList2())
            self.saveList1("-", "-")
            self.showText1()
            self.flushList2()
        elif (event.GetId() == self.button_MUL.GetId()):
            self.saveList1(self.getList2(), self.getList2())
            self.saveList1("*", "*")
            self.showText1()
            self.flushList2()
        elif (event.GetId() == self.button_DIV.GetId()):
            self.saveList1(self.getList2(), self.getList2())
            self.saveList1("/", "/")
            self.showText1()
            self.flushList2()
        elif (event.GetId() == self.button_NOT.GetId()):
            self.setList2(0 - int(self.getList2()))
            self.showText2()
        elif (event.GetId() == self.button_EQL.GetId()):
            self.saveList1(self.getList2(),self.getList2())
            self.showText1()
            print "operaList:" + str(self.getOperationList())
            if self.getOperationList()[-1] == "+" or\
                self.getOperationList()[-1] == "-" or\
                self.getOperationList()[-1] == "*" or \
                self.getOperationList()[-1] == "/":
                self.setList2(array_calculator.handleOperationList(self.getOperationList()[:-1]))
                self.setList2(array_calculator.handleOperationList([self.getList2(),self.getOperationList()[-1],self.getList2()]))
            else:
                self.setList2(array_calculator.handleOperationList(self.getOperationList()))
            print self.getList2()
            self.showText2()
        
