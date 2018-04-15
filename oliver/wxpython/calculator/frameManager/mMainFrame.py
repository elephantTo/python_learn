#! /usr/bin/python
# -*- coding: utf-8 -*-

from wxpythonMakeFrame import mainFrame

class mMainFrame(mainFrame.MainFrame):
    def __init__(self, parent = None, updateFrame = None):
        mainFrame.MainFrame.__init__(self, parent = None)
        self.updateFrame = updateFrame
    def gotoFrame(self, event):
        if event.GetId() == self.calculator_button.GetId():
            self.updateFrame("calculator")
        if event.GetId() == self.weather_button.GetId():
            self.updateFrame("weather")