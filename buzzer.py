import os
import datetime
from playsound import playsound
from AppKit import NSSound

os. system('clear')
alarmH = int(input("What hour do you want the alarm to ring? "))
alarmM = int(input("What minute do you want the alarm to ring? "))
amPm = str(input("am or pm? "))
os. system('clear')
print("Waiting for alarm",alarmH,alarmM,amPm)
if (amPm == "pm"):
        alarmH = alarmH + 12
while(1 == 1):
    if(alarmH == datetime.datetime.now().hour and
        alarmM == datetime.datetime.now().minute) :
        print("Time to wake up")
        playsound('C: / Users / varad / PycharmProjects / AlarmSystem / buzzer.mp3')
        break

