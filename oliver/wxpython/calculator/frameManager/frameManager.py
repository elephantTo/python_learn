#! /usr/bin/python
# -*- coding: utf-8 -*-

import mCalculatorFrame
import mMainFrame
import mWeatherFrame

id_frame = {"weather": mWeatherFrame .mWeatherFrame,
            "calculator": mCalculatorFrame.mCalculatorFrame,
            "main": mMainFrame.mMainFrame}

class manager():
    frameDict = id_frame
    def getFrame(self,id):
        return self.frameDict[id]
    
    


