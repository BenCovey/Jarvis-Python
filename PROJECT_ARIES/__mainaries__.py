__author__ = 'benvc'
import __lib__
import os
os.system('record.py')
class Main(object):

    # Start actual code here:
            
    welcome = "Welcome sir"
    voiceIn = ""
    print("                                          _____    ____ _    ___________             ")
    print("                                         / /   |  / __ \ |  / /  _/ ___/            ")
    print("                                    __  / / /| | / /_/ / | / // / \__ \             ")
    print("                                   / /_/ / ___ |/ _, _/| |/ // / ___/ /             ")
    print("                                   \____/_/  |_/_/ |_| |___/___//____/              ")
    print("                           _       __     __                             _____ _      ")
    print("                          | |     / /__  / /________  ____ ___  ___     / ___/(_)____   ")
    print("                          | | /| / / _ \/ / ___/ __ \/ __ `__ \/ _ \    \__ \/ / ___/  ")
    print("                          | |/ |/ /  __/ / /__/ /_/ / / / / / /  __/   ___/ / / /     ")
    print("                          |__/|__/\___/_/\___/\____/_/ /_/ /_/\___/   /____/_/_/      ")
    __lib__.engine(welcome)

    while(voiceIn != "quit"):
        voiceIn = __lib__.record()
        voiceIn = voiceIn.lower()
        __lib__.sender(voiceIn)
        __lib__.CheckAlarm()


