__author__ = 'benvc'
import __lib__
class Main(object):

    # Start actual code here:

    welcome = "Welcome sir"
    voiceIn = ""
    __lib__.engine(welcome)

    while(voiceIn != "quit"):
        voiceIn = __lib__.record()
        voiceIn = voiceIn.lower()
        print(voiceIn)
        print(__lib__.runTime())
        __lib__.sender(voiceIn)
        __lib__.CheckAlarm()


