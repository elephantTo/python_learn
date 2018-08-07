#! /usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import city
import json

def getCityCode(name):
    cityCode = city.city.get(name)
    if cityCode:
        return cityCode
    else:
        print "th name is err"
def getCityHtml(cityCode):
    url = (('http://www.weather.com.cn/data/cityinfo/%s.html' % cityCode))
    print url
    return url
def searchCityWeather(cityHtml):
    print cityHtml
    content = urllib2.urlopen(cityHtml).read()
    data = json.loads(content)["weatherinfo"]
    print ("%s %s~%s %s %s")%(data["city"],data["temp1"],data["temp2"],data["weather"],data["ptime"])
    return ("%s %s~%s %s %s")%(data["city"],data["temp1"],data["temp2"],data["weather"],data["ptime"])
    