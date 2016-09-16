__author__ = 'benvc'
import time
import datetime
import SendKeys
from BeautifulSoup import BeautifulSoup
import urllib2
import sys
import os
import requests

# GLOBALS
global Alarm
Alarm = ""
# FUNCTIONS


def functioncheck(request):
    if "make a note" in str(request) or "make note" in str(request) or "write a note" in str(request) or "take note" in str(request):
        writeNote(request)

    # Weather right now
    elif "what's the weather like" in str(request) or "how is the weather" in str(request):
        weather(requests)


    # Idle Aries for a time amount
    elif "idle for" in str(request):
        AriesIdle(request)

    # Clear the notepad file
    elif "clear my notes" in str(request) or "clear notes" in str(request) or "clear my nose" in str(request):
        closeNotes()

    # Make Aries Tab
    elif "tab" in str(request):
        #Tab using Sendkeys
        SendKeys.SendKeys("%{TAB}")

    # Chrome switch tab
    elif "switch tab" in str(request):
        #Tab using Sendkeys
        SendKeys.SendKeys("^{TAB}")

    # Google search
    elif "search this" in str(request) or "Aries google" in str(request) or "Aries look up" in str(request):
        Googling(request)

    # Get Aries to type things out
    elif "type" in str(request):
        AriesType(request)

    # Open anything
    elif "open" in str(request):
        openexes(request)

    elif "close" in str(request):
        print("close")
        closeExe(request)

    elif "set alarm" in str(request):
        SetAlarm(request)


    elif "restart 202" in str(request):
        restart()

    # print process time
    elif "current process time" in str(request):
        runtime = time.clock()
        engine(str(runtime.format(2)) + " seconds of run time.")


    else:
        print("Nothing Triggered")


def record():
    import speech_recognition as sr
    request = ""
    try:
        # recognize speech using Google Speech Recognition
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, 1)
            audio = r.listen(source)
        # recognize speech using Google Speech Recognition
        request = r.recognize_google(audio)

        # Fetch the problem problem to give the proper output
    except(sr.UnknownValueError):
        b = 0
    except sr.RequestError as e:
        print("Internal Error")
    print(request)
    return str(request)


def engine(message):
    import pyttsx

    # Load voice engine settings
    engine = pyttsx.init()
    # rate for how fast the voice speaks
    engine.setProperty('rate', 115)
    engine.say(message)
    engine.runAndWait()


def sender(message):
    if "Jarvis" in str(message):
        os.system('C:/Users/benvc/Documents/PyCharm/PROJECT_ARIES/__ARIES__.py')


def Googling(i):
    import os
    #base google results url
    googlelink = "https://www.google.ca/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q="

    # Replace all text implementations
    i = i.replace("Jarvis ", "")
    i = i.replace("google ", "")
    i = i.replace(" please", "")
    i = i.replace(" for me", "")
    # speech
    engine("searching for " + i)
    # replace spaces with %20 for google search
    i = i.replace(" ", "%20")
    # Concatenation of string
    googlelink = 'start chrome "%s%s"' % (googlelink, i)
    # open Chrome
    os.system(googlelink)
    # for x in range(3):
    #     r = sr.Recognizer()
    #     with sr.Microphone() as source:
    #         print("--")
    #         audio = r.listen(source)
    #     # recognize speech using Google Speech Recognition
    #     request = r.recognize_google(audio)
    #     # Fetch the problem problem to give the proper output
    #     try:
    #         print("Google Request: " + request)
    #     except sr.UnknownValueError:
    #         print("No Audio Detected")
    #     except sr.RequestError as e:
    #         print("Internal Error")
    #     if "open first link" in str(request):
    #         SendKeys.SendKeys('{DOWN}')
    #         SendKeys.SendKeys('{ENTER}')
    #     elif "open second link" in str(request):
    #         for x in range(2):
    #             SendKeys.SendKeys('{DOWN}')
    #         SendKeys.SendKeys('{ENTER}')
    #     elif "open third link" in str(request):
    #         for x in range(3):
    #             SendKeys.SendKeys('{DOWN}')
    #         SendKeys.SendKeys('{ENTER}')
    #     elif "open fourth link" in str(request):
    #         for x in range(4):
    #             SendKeys.SendKeys('{DOWN}')
    #         SendKeys.SendKeys('{ENTER}')
    #     elif "open fifth link" in str(request):
    #         for x in range(5):
    #             SendKeys.SendKeys('{DOWN}')
    #         SendKeys.SendKeys('{ENTER}')
    #     elif "open sixth link" in str(request):
    #         for x in range(6):
    #             SendKeys.SendKeys('{DOWN}')
    #         SendKeys.SendKeys('{ENTER}')


def machineTime():
    import time
    #Time (localtime off machine)
    dt = list(time.localtime())
    hourtime = dt[3]
    minutetime = dt[4]
    #Calculate AM/PM plus hours and minutes
    if hourtime > 12:
        hourtime -= 12
        timeOfDay = "PM"
    else:
        timeOfDay = "AM"
    if minutetime < 10:
        minute1 = 0
    else:
        minute1 = ""
    time = str(hourtime) + ":" + str(minute1) + str(minutetime) + str(timeOfDay)
    return(time)


def openexes(i):
    if "open wow" in str(i) or "open world or warcraft" in str(i):
        engine("Opening World of Warcraft")
        # Open WoW
        os.system('C:\Program Files (x86)\World of Warcraft')

    elif "open mine craft" in str(i) or "open minecraft" in str(i):
        engine("Opening minecraft")
        # open Minecraft
        os.system('"C:/Users/benvc/Desktop/Minecraft.exe"')

    elif "open steam" in str(i):
        engine("Opening Steam")
        # open Steam
        os.system('"C:/Users/benvc/Desktop/Steam.exe"')
    else:

        # Replace all text implementations and obsurities
        i = i.replace("Aries ", "")
        i = i.replace("open", "")
        i = i.replace("please", "")
        i = i.replace("dot", ".")
        i = i.replace(" ", "")
        # Get engine to speak
        engine("Opening " + i)
        # format the website URL with the chrome starter
        SiteURL = 'start chrome "%s"' % i
        # actually open it
        os.system(SiteURL)


def AriesIdle(i):
    # Remove the text leaving time and h/m/s
    i = i.replace("Aries", "")
    # Speech
    engine(i)
    i = i.replace("idle", "")
    i = i.replace("for", "")
    i = i.replace(" ", "")
    # If statements
    if "hour" in str(i) or "hours" in str(i):
        i = i.replace("hour","")
        i = i.replace("s","")
        i = float(i) * 60 * 60
        time.sleep(float(i))

    elif "minute" in str(i) or "minutes" in str(i):
        i = i.replace("minute","")
        i = i.replace("s","")
        i = float(i) * 60
        time.sleep(float(i))

    elif "second" in str(i) or "seconds" in str(i):
        i = i.replace("second","")
        i = i.replace("s","")
        time.sleep(float(i))


def writeNote(i):
    # Remove Aries and commands
    i = i.replace("Aries", "")
    i = i.replace("make a note", "")
    i = i.replace("make note", "")
    i = i.replace("write a note", "")
    i = i.replace("take note", "")
    ts = time.time()
    date1 = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    f = open("C://Users/benvc/Desktop/AriesNotes.txt", "a")
    f.write(str(date1) + ": " + i + "\n")
    f.close()
    # Speech
    engine("Note Written")

#TODO

def closeExe(i):
    i = i.replace("aries", "")
    i = i.replace("close", "")
    i = i.replace(" ", "")

    engine("closing " + i)
    if i == "chrome":
        os.system('taskkill /im chrome.exe')

    else:
        os.system('taskkill /f /im {0}.exe'.format("i"))


def closeNotes():
    f = open("C://Users/benvc/Desktop/AriesNotes.txt", "w")
    f.write("")
    f.close()
    # Speech
    engine("Notes Cleared")



def AriesType(i):
    # Remove the question and replace spaces
    i = i[4:]
    i = i.replace(" ", "{SPACE}")
    # Send keystrokes through
    SendKeys.SendKeys(str(i))



def weather(i):
    #site URL
    url = 'https://weather.gc.ca/city/pages/ns-19_metric_e.html'
    r = requests.get(url)
    #Open page as HTML
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(r.text)
    temp = soup.find("dd", {"class": "mrgn-bttm-0"}).contents
    soup = soup.findAll("td")
        #Print statement
    if "today" in str(i):
        weatherapp = soup[1]
        weatherapp = weatherapp.replace("<td>", "")
        weatherapp = weatherapp.replace("</td>","")
        engine(weatherapp)
    if "tomorrow" in str(i):
        weatherapp = soup[3]
        weatherapp = weatherapp.replace("<td>", "")
        weatherapp = weatherapp.replace("</td>","")
        engine(weatherapp)

def restart():
    os.execl(sys.executable, sys.executable, *sys.argv)

def runTime():
    runtime = time.clock()
    runtime = round(runtime,2)
    return((str(runtime) + " seconds of run time."))

def CheckAlarm():
    global Alarm
    import time
    date = time.strftime("%a, %d, %b, %Y,%H:%M,:%S +0000", time.localtime())
    date[0]
    date = date.split(',')
    time = str(date[0]) + str(date[4])
    if str(time) == str(Alarm):
        for x in range(3):
            engine("Good Morning sir ")
        Alarm = ""

def SetAlarm(request):
    global Alarm
    if "set alarm four" in str(request):
        request = request.replace("four", "")
        AlarmFour = SetAlarmTwo(request)
        print("Alarm four set for: " + str(AlarmFour))
    elif "set alarm three" in str(request):
        request = request.replace("three", "")
        AlarmThree = SetAlarmTwo(request)
        print("Alarm three set for: " + str(AlarmThree))
    elif "set alarm two" in str(request):
        request = request.replace("two", "")
        AlarmTwo = SetAlarmTwo(request)
        BooleanAlarmTwo = True
        print("Alarm two set for: " + str(AlarmTwo))
    elif "set alarm " in str(request):
        Alarm = SetAlarmTwo(request)
        print("Alarm one set for: " + str(Alarm))


def SetAlarmTwo(request):
    request = request.lower()
    if "monday" in str(request):
        pm = False
        request = request.replace(" ", "")
        request = request.replace("setalarmfor", "")
        request = request.replace("monday", "")
        request = request.replace("at", "")
        request = request.replace("a.m.", "")
        if "p.m." in str(request):
            pm = True
        request = request.replace("p.m.", "")
        request = request.split(":")
        if pm == True:
            request[0] = int(request[0]) + 12
        aDay = "Mon"
        aTime = str(request[0]) + ":" + str(request[1])

    elif "tuesday" in str(request):
        pm = False
        request = request.replace(" ", "")
        request = request.replace("setalarmfor", "")
        request = request.replace("a.m.", "")
        request = request.replace("tuesday", "")
        request = request.replace("at", "")
        if "p.m." in str(request):
            pm = True
        request = request.replace("p.m.", "")
        request = request.split(":")
        if pm == True:
            request[0] = int(request[0]) + 12
        aDay = "Tue"
        aTime = str(request[0]) + ":" + str(request[1])

    elif "wednesday" in str(request):
        pm = False
        request = request.replace(" ", "")
        request = request.replace("setalarmfor", "")
        request = request.replace("wednesday", "")
        request = request.replace("at", "")
        request = request.replace("a.m.", "")
        if "p.m." in str(request):
            pm = True
        request = request.replace("p.m.", "")
        request = request.split(":")
        if pm == True:
            request[0] = int(request[0]) + 12
        aDay = "Wed"
        aTime = str(request[0]) + ":" + str(request[1])

    elif "thursday" in str(request):
        pm = False
        request = request.replace(" ", "")
        request = request.replace("setalarmfor", "")
        request = request.replace("thursday", "")
        request = request.replace("at", "")
        request = request.replace("a.m.", "")
        if "p.m." in str(request):
            pm = True
        request = request.replace("p.m.", "")
        request = request.split(":")
        if pm == True:
            request[0] = int(request[0]) + 12
        aDay = "Thu"
        aTime = str(request[0]) + ":" + str(request[1])

    elif "friday" in str(request):
        pm = False
        request = request.replace(" ", "")
        request = request.replace("setalarmfor", "")
        request = request.replace("friday", "")
        request = request.replace("at", "")
        request = request.replace("a.m.", "")
        if "p.m." in str(request):
            pm = True
        request = request.replace("p.m.", "")
        request = request.split(":")
        if pm == True:
            request[0] = int(request[0]) + 12
        aDay = "Fri"
        aTime = str(request[0]) + ":" + str(request[1])

    elif "saturday" in str(request):
        pm = False
        request = request.replace(" ", "")
        request = request.replace("setalarmfor", "")
        request = request.replace("saturday", "")
        request = request.replace("at", "")
        request = request.replace("a.m.", "")
        if "p.m." in str(request):
            pm = True
        request = request.replace("p.m.", "")
        request = request.split(":")
        if pm == True:
            request[0] = int(request[0]) + 12
        aDay = "Sat"
        aTime = str(request[0]) + ":" + str(request[1])

    elif "sunday" in str(request):
        pm = False
        request = request.replace(" ", "")
        request = request.replace("setalarmfor", "")
        request = request.replace("sunday", "")
        request = request.replace("at", "")
        request = request.replace("a.m.", "")
        if "p.m." in str(request):
            pm = True
        request = request.replace("p.m.", "")
        request = request.split(":")
        if pm == True:
            request[0] = int(request[0]) + 12
        aDay = "Sun"

        aTime = str(request[0]) + ":" + str(request[1])

    alarm = aDay + aTime
    return alarm
# ##ALARM STUFF
