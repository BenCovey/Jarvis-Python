__author__ = 'benvc'
import os
import sys
import urllib3
sys.path.append(os.getcwd())
import library as lib



class jarvis(object):

    print("Jarvis Main")

    for x in range(250):
        voiceIn = lib.record()
        lib.functioncheck(voiceIn)

    os.system('C:/Users/Ben/Documents/GitHub/NSCC-IT/PROJECT_ARIES/__jarvis__.py')