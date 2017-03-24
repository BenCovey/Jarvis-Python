#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import requests
from BeautifulSoup import BeautifulSoup
import urllib2
weatherList = []
i = "whats the weather like"
 #site URL
url = 'https://weather.gc.ca/canada_e.html'
r = requests.get(url)
#Open page as HTML
page = urllib2.urlopen(url)
soup = BeautifulSoup(r.text)
temp = soup.find("table", {"class": "table table-hover table-striped table-condensed"})
soup = soup.findAll("td")

for x in range(0,60,3):
    # Sort each city into a separate weatherList item.
    weatherList.append([soup[x], soup[x + 2], soup[x + 1]])

#REGEX EXPRESSIONS
import re
for x in range(19):
    city = str(weatherList[x])
    city = re.sub('[^-0-9a-zA-Z]+',' ', city)
    city = city.replace("td", "")
    city = city.replace(" a href", "")
    city = city.replace(" city pages ", "")
    city = city.replace(" metric e html", "")
    city = city.replace(" a ", " is ")
    city = city.replace("deg C", "Degrees Celcius and")
    city = city.replace("ns-19", "")
    city = city.replace("ab-52", "")
    city = city.replace("pe-5", "")
    city = city.replace("ab-50", "")
    city = city.replace("nb-29", "")
    city = city.replace("nu-21", "")
    city = city.replace("qc-147", "")
    city = city.replace("sk-32", "")
    city = city.replace("sk-40", "")
    city = city.replace("nl-24", "")
    city = city.replace("on-100", "")
    city = city.replace("on-143", "")
    city = city.replace("bc-74", "")
    city = city.replace("bc-85", "")
    city = city.replace("yt-16", "")
    city = city.replace("mb-38", "")
    city = city.replace("nt-24", "")
    city = city.replace("Montr al", "Montreal")
    city = city.replace("on-118 Ottawa Kanata - Orl ans", " Ottawa")
    city = city.replace("bc-79 ", " ")
    city = city.replace("qc-133 Qu bec", " Quebec")
    city = city.replace("  ", "")
    if "weather in calgary" in str(i):
        print(city[0])
    elif "weather in charlottetown" in str(i):
        print(city[1])
    elif "weather in edmonton" in str(i):
        print(city[2])
    elif "weather in fredericton" in str(i):
        print(city[3])
    elif "weather in halifax" in str(i):
        print(city[4])
    elif "weather in iqaluit" in str(i):
        print(city[5])
    elif "weather in montreal" in str(i):
        print(city[6])
    elif "weather in ottawa" in str(i):
        print(city[7])
    elif "weather in prince george" in str(i):
        print(city[8])
    elif "weather in quebec" in str(i):
        print(city[9])
    elif "weather in regina" in str(i):
        print(city[10])
    elif "weather in saskatoon" in str(i):
        print(city[11])
    elif "weather in st john's" in str(i):
        print(city[12])
    elif "weather in thunder bay" in str(i):
        print(city[13])
    elif "weather in toronto" in str(i):
        print(city[14])
    elif "weather in vancover" in str(i):
        print(city[15])
    elif "weather in victoria" in str(i):
        print(city[16])
    elif "weather in whitehorse" in str(i):
        print(city[17])
    elif "weather in winnipeg" in str(i):
        print(city[18])
    elif "weather in yellowknife" in str(i):
        print(city[19])
    print(city[0]+ city[1] + city[2] + city[3])