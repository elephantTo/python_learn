#! /usr/bin/python
# -*- coding: utf-8 -*-

import wx
from frameManager import mCalculatorFrame
from frameManager import mMainFrame
id_frame = {"calculator": mCalculatorFrame.mCalculatorFrame,
            "main": mMainFrame.mMainFrame}

app = wx.App()
window = id_frame["main"](None)
window.Show(True)
app.MainLoop()