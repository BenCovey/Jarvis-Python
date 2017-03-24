__author__ = 'benvc'
import os
import sys
import urllib3
sys.path.append(os.getcwd())
import library as lib



class jarvis(object):
    request = ""
    print("Jarvis Main")

    voiceIn = "gmail"
    lib.functioncheck(voiceIn)

    for x in range(250):
        request = ""
        voiceIn = lib.record()
        #voiceIn = "search images of cat fails"
        lib.functioncheck(voiceIn)

    os.system('C:/Users/Ben/Documents/GitHub/NSCC-IT/PROJECT_ARIES/__jarvis__.py')