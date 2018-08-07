#! /usr/bin/python
# -*- coding: utf-8 -*-

import wx
import re

class mGobangFrame( wx.Frame ):
    def __init__(self, parent = None, updateFrame = None):
            wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"五子棋", pos=wx.DefaultPosition, size=wx.Size(500, 421),
                              style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
            self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
            self.width = 20
            self.hight = 20
            self.updateFrame = updateFrame
            self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
            self.gSizer3 = wx.GridSizer(self.width,self.hight, 0, 0)
            self.updateCheckBoard()
            self.SetSizer(self.gSizer3)
            self.Layout()
            self.Centre(wx.BOTH)
            self.AorB = True
            self.flag8 = 0b10000000
            self.flag7 = 0b01000000
            self.flag6 = 0b00100000
            self.flag5 = 0b00010000
            self.flag4 = 0b00001000
            self.flag3 = 0b00000100
            self.flag2 = 0b00000010
            self.flag1 = 0b00000001
            self.result = False
            self.Bind(wx.EVT_CLOSE, self.gotoMainFrame)
            
    def updateCheckBoard(self):
        for x in xrange(0, self.hight):
            for y in xrange(0,self.width):
                self.__dict__['button%d_%d' % (x,y)] = wx.RadioButton(self, wx.ID_ANY, wx.EmptyString,
                                                                          wx.DefaultPosition, wx.DefaultSize,
                                                                          wx.RB_SINGLE)
                self.gSizer3.Add( self.__dict__['button%d_%d' % (x,y)], 0, wx.ALL, 5 )
                self.__dict__['button%d_%d' % (x,y)].SetValue(False)
                self.__dict__['button%d_%d' % (x,y)].SetName("%d_%d"% (x,y))
                self.__dict__['button%d_%d' % (x,y)].Bind( wx.EVT_LEFT_DOWN, self.select)
    def gotoMainFrame(self, event):
        self.updateFrame("main")
    def select(self, event):
        if(self.FindWindowById(event.GetId()).GetValue()):
            pass
            #wheather can canel is or not[oliver.he]
            #self.FindWindowById(event.GetId()).SetValue(False)
            #self.FindWindowById(event.GetId()).SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
        else:
            if self.AorB == True:
                self.FindWindowById(event.GetId()).SetValue(True)
                #set color by system enum[oliver.he]
                #self.FindWindowById(event.GetId()).SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_3DSHADOW))
                self.FindWindowById(event.GetId()).SetBackgroundColour("#aa0007")
                if self.checkIfFiveAreConnected(event, "#aa0007"):
                    print "A are win"
                self.AorB = False
            else:
                self.FindWindowById(event.GetId()).SetValue(True)
                self.FindWindowById(event.GetId()).SetBackgroundColour("#Fa74f7")
                if self.checkIfFiveAreConnected(event, "#Fa74f7"):
                    print "B are win"
                self.AorB = True
                

    def checkIfFiveAreConnected(self, event, color):
        self.result = False
        
        curPosition = self._getCurrentPosition(event)
        x = int(curPosition[0])
        y = int(curPosition[1])
        flag = self.checkAroundEight(x, y, color)
        #1 8
        if self._checkFlag(flag, 1) and  self._checkFlag(flag, 8):
            self.result |= self.check1and8Line(x, y, color)
        elif self._checkFlag(flag, 1):
            self.result |= self.checklLine(x, y, color)
        elif self._checkFlag(flag, 8):
            self.result |= self.check8Line(x, y, color)
        print "1"
        print self.result
        #2 7
        if self._checkFlag(flag, 2) and  self._checkFlag(flag, 7):
            self.result |= self.check2and7Line(x, y, color)
        elif self._checkFlag(flag, 2):
            self.result |= self.check2Line(x, y, color)
        elif self._checkFlag(flag, 7):
            self.result |= self.check7Line(x, y, color)
        print "2"
        print self.result
        #3 6
        if self._checkFlag(flag, 3) and  self._checkFlag(flag, 6):
            self.result |= self.check3and6Line(x, y, color)
        elif self._checkFlag(flag, 3):
            self.result |= self.check3Line(x, y, color)
        elif self._checkFlag(flag, 6):
            self.result |= self.check6Line(x, y, color)

        print "3"
        print self.result
        #4 5
        if self._checkFlag(flag, 4) and  self._checkFlag(flag, 5):
            self.result |= self.check4and5Line(x, y, color)
            print "4"
            print self.result
        elif self._checkFlag(flag, 4):
            self.result |= self.check4Line(x, y, color)
            print "5"
            print self.result
        elif self._checkFlag(flag, 5):
            self.result |= self.check5Line(x, y, color)
            print "6"
            print self.result
        return self.result
    #第一步：检查周围六子得出可能连成五子的线路
    """
    678
    4*5
    123
    flag = 0b11111111
             87654321
    """
    def checkAroundEight(self, x, y,color):
        flag = 0b00000000
        if self.checkPointIsValueAndSelected(x - 1,y - 1,color):
            print "1 line"
            flag |= self.flag1
        if self.checkPointIsValueAndSelected(x,y - 1,color):
            print "2 line"
            flag |= self.flag2
        if self.checkPointIsValueAndSelected(x + 1, y - 1, color):
            print "3 line"
            flag |= self.flag3
        if self.checkPointIsValueAndSelected(x - 1, y, color):
            print "4 line"
            flag |= self.flag4
        if self.checkPointIsValueAndSelected(x + 1, y, color):
            print "5 line"
            flag |= self.flag5
        if self.checkPointIsValueAndSelected(x - 1, y + 1, color):
            print "6 line"
            flag |= self.flag6
        if self.checkPointIsValueAndSelected(x, y + 1, color):
            print "7 line"
            flag |= self.flag7
        if self.checkPointIsValueAndSelected(x + 1, y + 1, color):
            print "8 line"
            flag |= self.flag8
        return  flag
    #第二步：检查八条线路得出是否连成五子的结果
    def checklLine(self, x, y, color):
        result = False
        if self.checkPointIsValueAndSelected(x - 2, y - 2, color):
            if self.checkPointIsValueAndSelected(x - 3, y - 3, color):
                if self.checkPointIsValueAndSelected(x - 4, y - 4, color):
                    result = True
        return result
    def check2Line(self, x, y, color):
        result = False
        if self.checkPointIsValueAndSelected(x, y - 2, color):
            if self.checkPointIsValueAndSelected(x, y - 3, color):
                if self.checkPointIsValueAndSelected(x, y - 4, color):
                    result = True
        return result
    def check3Line(self, x, y, color):
        result = False
        if self.checkPointIsValueAndSelected(x + 2, y - 2, color):
            if self.checkPointIsValueAndSelected(x + 3, y - 3, color):
                if self.checkPointIsValueAndSelected(x + 4, y - 4, color):
                    result = True
        return result
    def check4Line(self, x, y, color):
        result = False
        if self.checkPointIsValueAndSelected(x - 2, y, color):
            if self.checkPointIsValueAndSelected(x - 3, y, color):
                if self.checkPointIsValueAndSelected(x - 4, y, color):
                    result = True
        return result
    def check5Line(self, x, y, color):
        result = False
        if self.checkPointIsValueAndSelected(x + 2, y, color):
            if self.checkPointIsValueAndSelected(x + 3, y, color):
                if self.checkPointIsValueAndSelected(x + 4, y, color):
                    result = True
        return result
    def check6Line(self, x, y, color):
        result = False
        if self.checkPointIsValueAndSelected(x - 2, y + 2, color):
            if self.checkPointIsValueAndSelected(x - 3, y + 3, color):
                if self.checkPointIsValueAndSelected(x - 4, y + 4, color):
                    result = True
        return result
    def check7Line(self, x, y, color):
        result = False
        if self.checkPointIsValueAndSelected(x, y + 2, color):
            if self.checkPointIsValueAndSelected(x, y + 3, color):
                if self.checkPointIsValueAndSelected(x, y + 4, color):
                    result = True
        return result
    def check8Line(self, x, y, color):
        result = False
        if self.checkPointIsValueAndSelected(x + 2, y + 2, color):
            if self.checkPointIsValueAndSelected(x + 3, y + 3, color):
                if self.checkPointIsValueAndSelected(x + 4, y + 4, color):
                    result = True
        return result
    def check1and8Line(self,x, y, color):
        result = False
        if self.checkPointIsValueAndSelected(x - 2, y - 2, color):
            if self.checkPointIsValueAndSelected(x - 3, y - 3, color):
                result = True
        if self.checkPointIsValueAndSelected(x + 2, y + 2, color):
            if self.checkPointIsValueAndSelected(x + 3, y + 3, color):
                result = True
        return result
    def check2and7Line(self,x, y, color):
        result = False
        if self.checkPointIsValueAndSelected(x, y - 2, color):
            if self.checkPointIsValueAndSelected(x, y - 3, color):
                result = True
        if self.checkPointIsValueAndSelected(x, y + 2, color):
            if self.checkPointIsValueAndSelected(x, y + 3, color):
                result = True
        return result
    def check3and6Line(self,x, y, color):
        result = False
        if self.checkPointIsValueAndSelected(x + 2, y - 2, color):
            if self.checkPointIsValueAndSelected(x + 3, y - 3, color):
                result = True
        if self.checkPointIsValueAndSelected(x - 2, y + 2, color):
            if self.checkPointIsValueAndSelected(x - 3, y + 3, color):
                result = True
        return result
    def check4and5Line(self,x, y, color):
        result = False
        if self.checkPointIsValueAndSelected(x - 2, y, color):
            if self.checkPointIsValueAndSelected(x - 3, y, color):
                result = True
        if self.checkPointIsValueAndSelected(x + 2, y, color):
            if self.checkPointIsValueAndSelected(x + 3, y, color):
                result = True
        return result
    #第三步：判断某点上是否被选上
    def checkPointIsValueAndSelected(self,x,y,color):
        if (x < 0) or (x > (self.hight - 1)) or (y < 0) or (y > (self.width - 1)):
            #print "Position (%d %d)"%(x, y) + "is not exist"
            return False
        Curcolor =  int(color[1:3],16)+int(color[3:5],16)+int(color[5:7],16)
        Selectcolor =  int(self.__dict__['button%d_%d' % (x, y)].GetBackgroundColour()[0] +
                           self.__dict__['button%d_%d' % (x, y)].GetBackgroundColour()[1] +
                           self.__dict__['button%d_%d' % (x, y)].GetBackgroundColour()[2])
        if Curcolor == Selectcolor:
            return True
        else:
            #print "Position (%d %d)" % (x, y) + "is not select"
            return False
    
    def _getCurrentPosition(self, event):
        name = self.FindWindowById(event.GetId()).GetName()
        pattern = re.compile('[0-9]+ ?')
        position = pattern.findall(name)
        return (position[0],position[1])
    
    def _checkFlag(self, flag, num):
        oliver = 0b00000001
        if (flag & (oliver << (num - 1))) > 0:
            return True
        else:
            return False

        
    
                
        

        