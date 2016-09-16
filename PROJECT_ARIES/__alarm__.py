__author__ = 'benvc'
import __lib__ as lib
alarmOne = False
alarmTwo = False
alarmThree = False
alarmFour = False


lib.engine("Alarm Management")
for x in range(5):
    request = ""
    request = lib.record()
    if "set alarm" in str(request):
        return 0
    elif "set alarm two" in str(request):
        return 0
    elif "set alarm three" in str(request):
        return 0
    elif "set alarm four" in str(request):
        return 0
