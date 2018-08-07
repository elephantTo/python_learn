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
## Class MainFrame
###########################################################################

class MainFrame(wx.Frame):
    
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"民叔的工具箱", pos=wx.DefaultPosition, size=wx.Size(283, 200),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        
        firstColumn = wx.GridSizer(0, 2, 0, 0)
        
        self.calculator_button = wx.Button(self, wx.ID_ANY, u"计算器", wx.DefaultPosition, wx.Size(120, 50), 0)
        self.calculator_button.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWFRAME))
        self.calculator_button.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INFOBK))
        
        firstColumn.Add(self.calculator_button, 0, wx.ALL, 5)
        
        self.gobang_button = wx.Button(self, wx.ID_ANY, u"五子棋", wx.DefaultPosition, wx.Size(120, 50), 0)
        self.gobang_button.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWFRAME))
        self.gobang_button.SetBackgroundColour(wx.Colour(255, 0, 128))
        
        firstColumn.Add(self.gobang_button, 0, wx.ALL, 5)
        
        self.weather_button = wx.Button(self, wx.ID_ANY, u"查询天气", wx.Point(200, 5), wx.Size(120, 50), 0)
        self.weather_button.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWFRAME))
        self.weather_button.SetBackgroundColour(wx.Colour(128, 128, 192))
        
        firstColumn.Add(self.weather_button, 0, wx.ALL, 5)
        
        self.SetSizer(firstColumn)
        self.Layout()
        
        self.Centre(wx.BOTH)
        
        # Connect Events
        self.calculator_button.Bind(wx.EVT_LEFT_DOWN, self.gotoFrame)
        self.gobang_button.Bind(wx.EVT_LEFT_DOWN, self.gotoFrame)
        self.weather_button.Bind(wx.EVT_LEFT_DOWN, self.gotoFrame)
    
    def __del__(self):
        pass
    
    # Virtual event handlers, overide them in your derived class
    def gotoFrame(self, event):
        event.Skip()




