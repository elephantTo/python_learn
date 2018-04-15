# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class CalculatorFrame
###########################################################################

class CalculatorFrame(wx.Frame):
    
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"计算器", pos=wx.DefaultPosition, size=wx.Size(300, 500),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.Colour(211, 211, 211))
        
        bSizer4 = wx.BoxSizer(wx.VERTICAL)
        
        bSizer6 = wx.BoxSizer(wx.VERTICAL)
        
        bSizer6.SetMinSize(wx.Size(40, 50))
        self.m_textCtrl2 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(500, 30),
                                       wx.TE_RIGHT)
        bSizer6.Add(self.m_textCtrl2, 0, wx.ALL, 5)
        
        self.m_textCtrl3 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(500, 30),
                                       wx.TE_RIGHT)
        bSizer6.Add(self.m_textCtrl3, 0, wx.ALL, 5)
        
        bSizer4.Add(bSizer6, 1, wx.EXPAND, 5)
        
        bSizer5 = wx.BoxSizer(wx.HORIZONTAL)
        
        bSizer5.SetMinSize(wx.Size(-1, 50))
        self.button_PRE = wx.Button(self, wx.ID_ANY, u"%", wx.DefaultPosition, wx.Size(62, 50), 0)
        self.button_PRE.SetBackgroundColour(wx.Colour(229, 229, 229))
        
        bSizer5.Add(self.button_PRE, 0, wx.ALL, 5)
        
        self.button_SQU = wx.Button(self, wx.ID_ANY, u"√", wx.DefaultPosition, wx.Size(62, 50), 0)
        self.button_SQU.SetBackgroundColour(wx.Colour(229, 229, 229))
        
        bSizer5.Add(self.button_SQU, 0, wx.ALL, 5)
        
        self.button_SQR = wx.Button(self, wx.ID_ANY, u"x²", wx.DefaultPosition, wx.Size(62, 50), 0)
        bSizer5.Add(self.button_SQR, 0, wx.ALL, 5)
        
        self.button_REC = wx.Button(self, wx.ID_ANY, u"¹/x", wx.DefaultPosition, wx.Size(62, 50), 0)
        bSizer5.Add(self.button_REC, 0, wx.ALL, 5)
        
        bSizer4.Add(bSizer5, 1, wx.EXPAND, 5)
        
        bSizer51 = wx.BoxSizer(wx.HORIZONTAL)
        
        bSizer51.SetMinSize(wx.Size(-1, 50))
        self.button_CE = wx.Button(self, wx.ID_ANY, u"CE", wx.DefaultPosition, wx.Size(62, 50), 0)
        self.button_CE.SetBackgroundColour(wx.Colour(229, 229, 229))
        
        bSizer51.Add(self.button_CE, 0, wx.ALL, 5)
        
        self.button_C = wx.Button(self, wx.ID_ANY, u"C", wx.DefaultPosition, wx.Size(62, 50), 0)
        self.button_C.SetBackgroundColour(wx.Colour(229, 229, 229))
        
        bSizer51.Add(self.button_C, 0, wx.ALL, 5)
        
        self.button_DEL = wx.Button(self, wx.ID_ANY, u"<-", wx.DefaultPosition, wx.Size(62, 50), 0)
        bSizer51.Add(self.button_DEL, 0, wx.ALL, 5)
        
        self.button_DIV = wx.Button(self, wx.ID_ANY, u"÷", wx.DefaultPosition, wx.Size(62, 50), 0)
        bSizer51.Add(self.button_DIV, 0, wx.ALL, 5)
        
        bSizer4.Add(bSizer51, 1, wx.EXPAND, 5)
        
        bSizer52 = wx.BoxSizer(wx.HORIZONTAL)
        
        bSizer52.SetMinSize(wx.Size(-1, 50))
        self.button7 = wx.Button(self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.Size(62, 50), 0)
        self.button7.SetBackgroundColour(wx.Colour(246, 246, 246))
        
        bSizer52.Add(self.button7, 0, wx.ALL, 5)
        
        self.button8 = wx.Button(self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.Size(62, 50), 0)
        self.button8.SetBackgroundColour(wx.Colour(246, 246, 246))
        
        bSizer52.Add(self.button8, 0, wx.ALL, 5)
        
        self.button9 = wx.Button(self, wx.ID_ANY, u"9", wx.DefaultPosition, wx.Size(62, 50), 0)
        self.button9.SetBackgroundColour(wx.Colour(246, 246, 246))
        
        bSizer52.Add(self.button9, 0, wx.ALL, 5)
        
        self.button_MUL = wx.Button(self, wx.ID_ANY, u"×", wx.DefaultPosition, wx.Size(62, 50), 0)
        bSizer52.Add(self.button_MUL, 0, wx.ALL, 5)
        
        bSizer4.Add(bSizer52, 1, wx.EXPAND, 5)
        
        bSizer521 = wx.BoxSizer(wx.HORIZONTAL)
        
        bSizer521.SetMinSize(wx.Size(-1, 50))
        self.button4 = wx.Button(self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.Size(62, 50), 0)
        self.button4.SetBackgroundColour(wx.Colour(246, 246, 246))
        
        bSizer521.Add(self.button4, 0, wx.ALL, 5)
        
        self.button5 = wx.Button(self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.Size(62, 50), 0)
        self.button5.SetBackgroundColour(wx.Colour(246, 246, 246))
        
        bSizer521.Add(self.button5, 0, wx.ALL, 5)
        
        self.button6 = wx.Button(self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.Size(62, 50), 0)
        self.button6.SetBackgroundColour(wx.Colour(246, 246, 246))
        
        bSizer521.Add(self.button6, 0, wx.ALL, 5)
        
        self.button_SUB = wx.Button(self, wx.ID_ANY, u"－", wx.DefaultPosition, wx.Size(62, 50), 0)
        self.button_SUB.SetBackgroundColour(wx.Colour(229, 229, 229))
        
        bSizer521.Add(self.button_SUB, 0, wx.ALL, 5)
        
        bSizer4.Add(bSizer521, 1, wx.EXPAND, 5)
        
        bSizer522 = wx.BoxSizer(wx.HORIZONTAL)
        
        bSizer522.SetMinSize(wx.Size(-1, 50))
        self.button1 = wx.Button(self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size(62, 50), 0)
        self.button1.SetBackgroundColour(wx.Colour(246, 246, 246))
        
        bSizer522.Add(self.button1, 0, wx.ALL, 5)
        
        self.button2 = wx.Button(self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.Size(62, 50), 0)
        self.button2.SetBackgroundColour(wx.Colour(246, 246, 246))
        
        bSizer522.Add(self.button2, 0, wx.ALL, 5)
        
        self.button3 = wx.Button(self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.Size(62, 50), 0)
        self.button3.SetBackgroundColour(wx.Colour(246, 246, 246))
        
        bSizer522.Add(self.button3, 0, wx.ALL, 5)
        
        self.button_ADD = wx.Button(self, wx.ID_ANY, u"+", wx.DefaultPosition, wx.Size(62, 50), 0)
        self.button_ADD.SetBackgroundColour(wx.Colour(229, 229, 229))
        
        bSizer522.Add(self.button_ADD, 0, wx.ALL, 5)
        
        bSizer4.Add(bSizer522, 1, wx.EXPAND, 5)
        
        bSizer5211 = wx.BoxSizer(wx.HORIZONTAL)
        
        bSizer5211.SetMinSize(wx.Size(-1, 50))
        self.button_NOT = wx.Button(self, wx.ID_ANY, u"±", wx.DefaultPosition, wx.Size(62, 50), 0)
        self.button_NOT.SetBackgroundColour(wx.Colour(229, 229, 229))
        
        bSizer5211.Add(self.button_NOT, 0, wx.ALL, 5)
        
        self.button0 = wx.Button(self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size(62, 50), 0)
        self.button0.SetBackgroundColour(wx.Colour(246, 246, 246))
        
        bSizer5211.Add(self.button0, 0, wx.ALL, 5)
        
        self.button_POT = wx.Button(self, wx.ID_ANY, u".", wx.DefaultPosition, wx.Size(62, 50), 0)
        self.button_POT.SetBackgroundColour(wx.Colour(229, 229, 229))
        
        bSizer5211.Add(self.button_POT, 0, wx.ALL, 5)
        
        self.button_EQL = wx.Button(self, wx.ID_ANY, u"=", wx.DefaultPosition, wx.Size(62, 50), 0)
        bSizer5211.Add(self.button_EQL, 0, wx.ALL, 5)
        
        bSizer4.Add(bSizer5211, 1, wx.EXPAND, 5)
        
        self.SetSizer(bSizer4)
        self.Layout()
        
        self.Centre(wx.BOTH)
        
        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.gotoMainFrame)
        self.button_SQU.Bind(wx.EVT_LEFT_DOWN, self.handleOperator)
        self.button_SQR.Bind(wx.EVT_LEFT_DOWN, self.handleOperator)
        self.button_REC.Bind(wx.EVT_LEFT_DOWN, self.handleOperator)
        self.button_CE.Bind(wx.EVT_LEFT_DOWN, self.handleOperator)
        self.button_C.Bind(wx.EVT_LEFT_DOWN, self.handleOperator)
        self.button_DEL.Bind(wx.EVT_LEFT_DOWN, self.handleOperator)
        self.button_DIV.Bind(wx.EVT_LEFT_DOWN, self.handleOperator)
        self.button7.Bind(wx.EVT_LEFT_DOWN, self.handleNum)
        self.button8.Bind(wx.EVT_LEFT_DOWN, self.handleNum)
        self.button9.Bind(wx.EVT_LEFT_DOWN, self.handleNum)
        self.button_MUL.Bind(wx.EVT_LEFT_DOWN, self.handleOperator)
        self.button4.Bind(wx.EVT_LEFT_DOWN, self.handleNum)
        self.button5.Bind(wx.EVT_LEFT_DOWN, self.handleNum)
        self.button6.Bind(wx.EVT_LEFT_DOWN, self.handleNum)
        self.button_SUB.Bind(wx.EVT_LEFT_DOWN, self.handleOperator)
        self.button1.Bind(wx.EVT_LEFT_DOWN, self.handleNum)
        self.button2.Bind(wx.EVT_LEFT_DOWN, self.handleNum)
        self.button3.Bind(wx.EVT_LEFT_DOWN, self.handleNum)
        self.button_ADD.Bind(wx.EVT_LEFT_DOWN, self.handleOperator)
        self.button0.Bind(wx.EVT_LEFT_DOWN, self.handleNum)
        self.button_POT.Bind(wx.EVT_LEFT_DOWN, self.handleNum)
        self.button_EQL.Bind(wx.EVT_LEFT_DOWN, self.handleOperator)
    
    def __del__(self):
        pass
    
    # Virtual event handlers, overide them in your derived class
    def gotoMainFrame(self, event):
        event.Skip()
    
    def handleOperator(self, event):
        event.Skip()
    
    def handleNum(self, event):
        event.Skip()
















