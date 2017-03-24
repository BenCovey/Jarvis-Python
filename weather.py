#!/usr/bin/env python
#Author : Ben Covey
import urllib3
import py2exe
import json
import pytemperature
import time
from tkinter import *
http = urllib3.PoolManager()
Time = time.ctime()
#print(Time)
#Create Page and use get to obtain data


page = http.request('GET', 'api.openweathermap.org/data/2.5/weather?id=6324729&units=metric&APPID=118f85017faf22935ce9ed5ca5ea1eac')
# page = http.request('GET', 'api.openweathermap.org/data/2.5/weather?q=London&APPID=118f85017faf22935ce9ed5ca5ea1eac')

def weathernow():
    page = http.request('GET', 'api.openweathermap.org/data/2.5/weather?id=6324729&APPID=118f85017faf22935ce9ed5ca5ea1eac')
    currentweather = str(page.data)
    currentweather = currentweather.replace("b'", "")
    currentweather = currentweather.replace("'", "")
    parsed_weather = json.loads((currentweather))
    desc = parsed_weather['weather'][0]['description']

    temp = parsed_weather['main']['temp']
    temp = int(pytemperature.k2c(temp))

    high = parsed_weather['main']['temp_max']
    high = int(pytemperature.k2c(high))

    low = parsed_weather['main']['temp_min']
    low = int(pytemperature.k2c(low))

    windspd = parsed_weather['wind']['speed']
    winddirec = parsed_weather['wind']['deg']
    dirs = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
            "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    ix = int((winddirec + 11.25)/22.5)
    winddirec= dirs[ix % 16]

    weatherdata = "Current weather " + desc + ", temperature is " + str(low) + " with a high of " + str(high) + " and a low of " + str(low) + ", " + str(windspd) + " wind in blowing " + winddirec
    print(weatherdata)
    return weatherdata
def Today():
    weather = page.data
    weather = str(weather)
    weather = weather.split("<item>")
    weather = weather[1]
    weather = weather.replace('"','')
    weather = weather.replace("\\r","")
    weather = weather.replace("\\n","")
    weather = weather.replace("\\t","")
    weather = weather.replace("\\h","")
    weather = weather.replace("<title>","")
    weather = weather.replace("</title><guid>http://www.theweathernetwork.com/weather/cans0317?ref=current_obs</guid><link>http://www.theweathernetwork.com/weather/cans0317?ref=current_obs</link><pubDate>","\n")
    weather = weather.replace("-0500</pubDate><description>","\n")
    weather = weather.replace(",, ","")
    weather = weather.replace("&amp;nbsp;&amp;deg;","")
    weather = weather.replace("C,","C\n")
    weather = weather.replace("</description></item>","\n")
    weather = weather.replace("Humidity","Humidity ")
    weather = weather.replace("Wind","Wind ")
    Today = weather
    return Today

def Tomorrow():
    weather = page.data
    weather = str(weather)
    weather = weather.split("<item>")
    NextDay = weather[2]
    NextDay = NextDay.replace('"','')
    NextDay = NextDay.replace("\\r","")
    NextDay = NextDay.replace("\\n","")
    NextDay = NextDay.replace("\\t","")
    NextDay = NextDay.replace("\\h","")
    NextDay = NextDay.replace("<title>", "")
    NextDay = NextDay.replace("</title><guid>http://www.theweathernetwork.com/weather/cans0317?ref=day1#ltermfx</guid><link>http://www.theweathernetwork.com/weather/cans0317?ref=day1#ltermfx</link><pubDate>","\n")
    NextDay = NextDay.replace("-0500</pubDate><description>","\n")
    NextDay = NextDay.replace(",, ","")
    NextDay = NextDay.replace("&amp;nbsp;&amp;deg;","")
    NextDay = NextDay.replace("C,","C\n")
    NextDay = NextDay.replace("</description></item>","\n")
    NextDay = NextDay.replace("Humidity","Humidity ")
    NextDay = NextDay.replace("Wind","Wind ")
    return NextDay
def TwoDay():
    weather = page.data
    weather = str(weather)
    weather = weather.split("<item>")
    TwoDay = weather[3]
    ThreeDay = weather[4]
    TwoDay = TwoDay.replace('"','')
    TwoDay = TwoDay.replace("\\r","")
    TwoDay = TwoDay.replace("\\n","")
    TwoDay = TwoDay.replace("\\t","")
    TwoDay = TwoDay.replace("<title>", "")
    TwoDay = TwoDay.replace("</title><link>http://www.theweathernetwork.com/weather/cans0317?ref=day2#ltermfx</link><guid>http://www.theweathernetwork.com/weather/cans0317?ref=day2#ltermfx</guid><pubDate>","\n")
    TwoDay = TwoDay.replace("-0500</pubDate><description>","\n")
    TwoDay = TwoDay.replace(",, ","")
    TwoDay = TwoDay.replace("&amp;nbsp;&amp;deg;","")
    TwoDay = TwoDay.replace("C,","C\n")
    TwoDay = TwoDay.replace("</description></item>","\n")
    TwoDay = TwoDay.replace("Humidity","Humidity ")
    TwoDay = TwoDay.replace("Wind","Wind ")
    return TwoDay

def ThreeDay():
    weather = page.data
    weather = str(weather)
    weather = weather.split("<item>")
    ThreeDay = weather[4]
    ThreeDay = ThreeDay.replace('"','')
    ThreeDay = ThreeDay.replace("\\r","")
    ThreeDay = ThreeDay.replace("\\n","")
    ThreeDay = ThreeDay.replace("\\t","")
    ThreeDay = ThreeDay.replace("\\h","")
    ThreeDay = ThreeDay.replace("<title>", "")
    ThreeDay = ThreeDay.replace("</title><link>http://www.theweathernetwork.com/weather/cans0317?ref=day3#ltermfx</link><guid>http://www.theweathernetwork.com/weather/cans0317?ref=day3#ltermfx</guid><pubDate>","\n")
    ThreeDay = ThreeDay.replace("-0500</pubDate><description>","\n")
    ThreeDay = ThreeDay.replace(",, ","")
    ThreeDay = ThreeDay.replace("&amp;nbsp;&amp;deg;","")
    ThreeDay = ThreeDay.replace("C,","C\n")
    ThreeDay = ThreeDay.replace("</description></item>","\n")
    ThreeDay = ThreeDay.replace("Humidity","Humidity ")
    ThreeDay = ThreeDay.replace("Wind","Wind ")
    ThreeDay = ThreeDay.replace("</channel></rss>'","")
    return ThreeDay


def All():
    weather = page.data
    weather = str(weather)
    weather = weather.split("<item>")
    weather = weather[1]
    weather = weather.replace('"','')
    weather = weather.replace("\\r","")
    weather = weather.replace("\\n","")
    weather = weather.replace("\\t","")
    weather = weather.replace("\\h","")
    weather = weather.replace("<title>","")
    weather = weather.replace("</title><guid>http://www.theweathernetwork.com/weather/cans0317?ref=current_obs</guid><link>http://www.theweathernetwork.com/weather/cans0317?ref=current_obs</link><pubDate>","\n")
    weather = weather.replace("-0500</pubDate><description>","\n")
    weather = weather.replace(",, ","")
    weather = weather.replace("&amp;nbsp;&amp;deg;","")
    weather = weather.replace("C,","C\n")
    weather = weather.replace("</description></item>","\n")
    weather = weather.replace("Humidity","Humidity ")
    weather = weather.replace("Wind","Wind ")
    Today = weather
    weather = page.data
    weather = str(weather)
    weather = weather.split("<item>")
    NextDay = weather[2]
    NextDay = NextDay.replace('"','')
    NextDay = NextDay.replace("\\r","")
    NextDay = NextDay.replace("\\n","")
    NextDay = NextDay.replace("\\t","")
    NextDay = NextDay.replace("\\h","")
    NextDay = NextDay.replace("<title>", "")
    NextDay = NextDay.replace("</title><guid>http://www.theweathernetwork.com/weather/cans0317?ref=day1#ltermfx</guid><link>http://www.theweathernetwork.com/weather/cans0317?ref=day1#ltermfx</link><pubDate>","\n")
    NextDay = NextDay.replace("-0500</pubDate><description>","\n")
    NextDay = NextDay.replace(",, ","")
    NextDay = NextDay.replace("&amp;nbsp;&amp;deg;","")
    NextDay = NextDay.replace("C,","C\n")
    NextDay = NextDay.replace("</description></item>","\n")
    NextDay = NextDay.replace("Humidity","Humidity ")
    NextDay = NextDay.replace("Wind","Wind ")
    weather = page.data
    weather = str(weather)
    weather = weather.split("<item>")
    ThreeDay = weather[4]
    ThreeDay = ThreeDay.replace('"','')
    ThreeDay = ThreeDay.replace("\\r","")
    ThreeDay = ThreeDay.replace("\\n","")
    ThreeDay = ThreeDay.replace("\\t","")
    ThreeDay = ThreeDay.replace("\\h","")
    ThreeDay = ThreeDay.replace("<title>", "")
    ThreeDay = ThreeDay.replace("</title><link>http://www.theweathernetwork.com/weather/cans0317?ref=day3#ltermfx</link><guid>http://www.theweathernetwork.com/weather/cans0317?ref=day3#ltermfx</guid><pubDate>","\n")
    ThreeDay = ThreeDay.replace("-0500</pubDate><description>","\n")
    ThreeDay = ThreeDay.replace(",, ","")
    ThreeDay = ThreeDay.replace("&amp;nbsp;&amp;deg;","")
    ThreeDay = ThreeDay.replace("C,","C\n")
    ThreeDay = ThreeDay.replace("</description></item>","\n")
    ThreeDay = ThreeDay.replace("Humidity","Humidity ")
    ThreeDay = ThreeDay.replace("Wind","Wind ")
    ThreeDay = ThreeDay.replace("</channel></rss>'","")
    Weather = Today() + "\n" + "Forecast\n" + Tomorrow() + "\n" + NextDay + "\n" + ThreeDay()
    return Weather

# now()

