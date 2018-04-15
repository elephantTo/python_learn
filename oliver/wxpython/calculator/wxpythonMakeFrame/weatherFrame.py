# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from misc import city


###########################################################################
## Class WeatherFrame
###########################################################################

class WeatherFrame(wx.Frame):
    
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"查询天气", pos=wx.DefaultPosition, size=wx.Size(467, 419),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        
        gSizer2 = wx.GridSizer(2, 2, 40, 0)
        
        city_comboBoxChoices = city.city.keys()
        self.city_comboBox = wx.ComboBox(self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize,
                                         city_comboBoxChoices, wx.CB_DROPDOWN | wx.CB_SORT)
        gSizer2.Add(self.city_comboBox, 0, wx.ALL, 5)
        
        self.enter_button = wx.Button(self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.Size(-1, 25), 0)
        gSizer2.Add(self.enter_button, 0, wx.ALL, 5)
        
        self.hide_textCtrl = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1), 0)
        self.hide_textCtrl.Hide()
        
        gSizer2.Add(self.hide_textCtrl, 0, wx.ALL, 5)
        
        self.weather_textCtrl = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(260, -1), 0)
        gSizer2.Add(self.weather_textCtrl, 0, wx.ALL, 5)
        
        self.SetSizer(gSizer2)
        self.Layout()
        
        self.Centre(wx.BOTH)
        
        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.gotoMainFrame)
        self.enter_button.Bind(wx.EVT_LEFT_DOWN, self.searchWeather)
    
    def __del__(self):
        pass
    
    # Virtual event handlers, overide them in your derived class
    def gotoMainFrame(self, event):
        event.Skip()
    
    def searchWeather(self, event):
        event.Skip()


