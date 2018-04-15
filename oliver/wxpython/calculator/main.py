#! /usr/bin/python
# -*- coding: utf-8 -*-

import wx
import numpy
from frameManager import frameManager

class MainApp(wx.App):
    def OnInit(self):
        self.manager = frameManager.manager()
        self.frame = self.manager.getFrame("main")(updateFrame = self.updateFrame)
        self.frame.Show(True)
        return True
    def updateFrame(self,id):
        self.frame.Show(False)
        self.frame = self.manager.getFrame(id)(updateFrame = self.updateFrame)
        self.frame.Show(True)
       
def main():
    app = MainApp()
    app.MainLoop()
    
if __name__ == "__main__":
    main()




