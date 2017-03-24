__author__ = 'benvc'
# this application is part of the AI that is known as
# this section contains an alarm clock, plus clock.
# in the future it will contain light controls + basic
# robotic code for opening blinds.
import time
import speech_recognition as sr
import pyttsx
from BeautifulSoup import BeautifulSoup
import urllib2
import os

# Load voice engine settings
engine = pyttsx.init()
# rate for how fast the voice speaks
engine.setProperty('rate', 167)
voices = engine.getProperty('voices')
# Welcome into Alarm clock function
engine.say("Alarm clock")
engine.runAndWait()
request = ""
global aRequest
Alarmset = False
global alarmtime
global repeat, setfor1, setfor2
repeat = False
alarmtime = []
# infinite loop measure
x = 0
#Alarm clock functions
def Alarmclock(request):
    global aRequest, setfor1, setfor2, datetype

    datetype = "am"
    if "p.m." in str(request):
        datetype = "pm"
    request = request.replace("jarvis","")
    request = request.replace("set an alarm ", "")
    request = request.replace("set alarm ", "")
    request = request.replace("for", "")
    request = request.replace(" ", "")
    request = request.replace("p.m.", "")
    request = request.replace("a.m.", "")
    aRequest = request
    alarmtime = request.split(":")
    setfor1 = alarmtime[0]
    setfor2 = alarmtime[1]
def AlarmChecker():
    global repeat, datatype
    import time
    if Alarmset == True:
        dt = list(time.localtime())
        hour = dt[3]
        minute = dt[4]
        #Calculate AM/PM plus hours and minutes
        if hour > 12:
             hour -= 12
             timeOfDay = "pm"
        else:
             timeOfDay = "am"
        setfor3 = datetype
        Tsetfor = str(setfor1) + str(setfor2) + str(setfor3)
        Tactually = (str(hour) + str(minute)+ str(timeOfDay))
        print(Tsetfor)
        print(Tactually)
        if Tactually == Tsetfor:
            repeat = True
            AlarmSet = False
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
def day():
    import datetime
    dayow = datetime.datetime.today().weekday()
    # find the day of the week.
    if dayow == 1:
        return "Sunday"
    elif dayow == 2:
        return "Money"
    elif dayow == 3:
        return "Tuesday"
    elif dayow == 4:
        return "Wednesday"
    elif dayow == 5:
        return "Thursday"
    elif dayow == 6:
        return "Friday"
    elif dayow == 7:
        return "Saturday"

# Mic on and record then Speech to Text


while(x == 0):
    # Try to pick up microphone audio, if it doesn't it fails

    try:
        # request = ""
        # recognize speech using Google Speech Recognition
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("..")
            audio = r.listen(source)
        # recognize speech using Google Speech Recognition
        request = r.recognize_google(audio)
            # Fetch the problem problem to give the proper output
        try:
            print("Accepted Speech: " + request)
            if Alarmset == True:
                AlarmChecker()
        except sr.UnknownValueError:
            print("No Audio Detected")
            if Alarmset == True:
                AlarmChecker()
        except sr.RequestError as e:
            print("Internal Error")
            if Alarmset == True:
                AlarmChecker()

        # Make the request in lower
        request = request.lower()
        # Set alarm
        if "set alarm" in str(request)or "set an alarm" in str(request):
            Alarmset = True
            Alarmclock(request)
            engine.say("Alarm is set")
            engine.runAndWait()
        # Turn off the alarm
        elif "turn off" in str(request):
            Alarmset = False
            repeat = False
            engine.say("Alarm disabled")
            engine.runAndWait()
        # time
        elif "what time is it?" in str(request):
            engine.say("It is " + str(day()) + str(machineTime()) + " sir")
            engine.runAndWait()
        #snooozzee
        elif "snooze" in str(request):
            setfor2 = setfor2 + 5

        #return to AI Main
        elif "return" in str(request):
            os.system("JarvisAlphav1.py")
            os.quit()
    except:
        print("...")
        if Alarmset == True:
                AlarmChecker()
        request = ""
        if repeat == True:
            wakeUp = "Time to wake up Sir, it is " + day() + " at " + machineTime()
            print(wakeUp)
            engine.say(wakeUp)
            engine.runAndWait()