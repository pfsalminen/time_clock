#!/usr/bin/env python

import time
try:
    import Tkinter
except:
    print 'Tkinter not found'
import tkMessageBox

# Globals
top = Tkinter.Tk()
time1 = ''
startHMS = []
running = True

def timeDiff(curTime, startTime):
    timeDiff = curInts[0]*3600 + timeInts[1]*60 + timeInts[2] - time

def startTime():
    global startHMS
    global running
    running = True
    initial = time.strftime('%H:%M:%S')
    beginBox.config(text=("Start Time: %s" % initial))
    startHMS = [int(x) for x in initial.split(':')]
    elapsedTime()

def elapsedTime():
    global startHMS
    global runnng
    curHMS = [int(x) for x in time.strftime('%H:%M:%S').split(':')]
    elapHMS = []
    for i,x in enumerate(startHMS):
        elapHMS.append(curHMS[i] - startHMS[i])
    elapHMS = ':'.join([str(x) for x in elapHMS])
    elapsedBox.config(text=("Elapsed time: %s" % elapHMS))
    if running: elapsedBox.after(200, elapsedTime)

def stopTime():
    global running
    final = time.strftime('%H:%M:%S')
    stopBox.config(text=("End Time: %s" % final))
    running = False
    return final

def saveTimes():
    print "Yay"

def tick():
    global time1
    time2 = time.strftime('%H:%M:%S')
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    clock.after(200, tick)

# Widgets
clock = Tkinter.Label(top, font=('times', 20, 'bold'), bg='gray')
beginBox = Tkinter.Label(top, font=('times', 12), bg='gray')
stopBox = Tkinter.Label(top, font=('times', 12), bg='gray')
elapsedBox = Tkinter.Label(top, font=('times', 12), bg='gray')
Start = Tkinter.Button(top, text="Start", command=startTime)
Stop = Tkinter.Button(top, text="Stop", command=stopTime)
Quit = Tkinter.Button(top, text="Quit", command=top.quit)
Save = Tkinter.Button(top, text="Save Time", command=saveTimes)

# Pack
clock.pack()
beginBox.pack()
elapsedBox.pack()
stopBox.pack()
Start.pack()
Stop.pack()
Save.pack()
Quit.pack()

# Run
tick()
top.mainloop()
