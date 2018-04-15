#! /usr/bin/python
# -*- coding: utf-8 -*-
from misc import weather

from wxpythonMakeFrame import weatherFrame

class mWeatherFrame(weatherFrame.WeatherFrame):
    def __init__(self, parent = None, updateFrame = None):
        weatherFrame.WeatherFrame.__init__(self, parent = None)
        self.updateFrame = updateFrame
    def gotoMainFrame(self, event):
        self.updateFrame("main")
    def searchWeather(self, event):
        city = self.city_comboBox.GetValue()
        print city.encode('gbk')
        cityCode = weather.getCityCode(city.encode('utf8'))
        if cityCode:
            data = weather.searchCityWeather(weather.getCityHtml(cityCode))
            self.weather_textCtrl.SetValue(data)
        else:
            self.weather_textCtrl.SetValue("你输入的城市有误")
        