#! /usr/bin/python
# -*- coding: utf-8 -*-

import mCalculatorFrame
import mMainFrame
import mWeatherFrame
import mGobangFrame

id_frame = {"weather": mWeatherFrame .mWeatherFrame,
            "calculator": mCalculatorFrame.mCalculatorFrame,
            "main": mMainFrame.mMainFrame,
            "gobang": mGobangFrame.mGobangFrame}

class manager():
    frameDict = id_frame
    def getFrame(self,id):
        return self.frameDict[id]
    
    


