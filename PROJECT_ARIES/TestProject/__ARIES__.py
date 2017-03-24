__author__ = 'benvc'
import __lib__
import os
class aries(object):

    request = ""
    print("Ares Main")
    for x in range(250):
        request = ""
        voiceIn = __lib__.record()
        __lib__.functioncheck(voiceIn)
        __lib__.CheckAlarm()
        # __lib__.CheckAlarm(__lib__.AlarmTwo)
        # __lib__.CheckAlarm(__lib__.AlarmThree)
        # __lib__.CheckAlarm(__lib__.AlarmFour)
    os.system('C:/Users/benvc/Documents/PyCharm/PROJECT_ARIES/__mainjarvis__.py')