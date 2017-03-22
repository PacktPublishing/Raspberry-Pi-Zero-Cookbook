#!/bin/env python
# Chapter 7 Hardware Control
# RPZ Health Monitoring and Alerting
import time
import os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
redpin=18
greenpin=17
bluepin=27
buzzerpin=22
GPIO.setup(redpin, GPIO.OUT)
GPIO.setup(bluepin, GPIO.OUT)
GPIO.setup(greenpin, GPIO.OUT)
GPIO.setup(buzzerpin, GPIO.OUT)
buzzer = GPIO.PWM(buzzerpin, 0.5)
tempyellow = 42.0
tempred= 50.0
tempbuzz = 55.0
def rgblight(r,g,b):
        GPIO.output(redpin,r)
        GPIO.output(greenpin,g)
        GPIO.output(bluepin,b)
def greenlight():
        rgblight(1,0,0)
def yellowlight():
        rgblight(1,0,1)
def redlight():
        rgblight(0,0,1)
def offlight():
        rgblight(0,0,0)
def buzz():
        buzzer.start(50)
        for x in range(0,10):
                buzzer.ChangeFrequency(500)
                time.sleep(.4)
                buzzer.ChangeFrequency(750)
                time.sleep(.4)
        buzzer.stop()
def checkrpz():
        loadavg=os.getloadavg()
        rpztemp=os.popen('vcgencmd measure_temp').readline()
        rpztemp=float(rpztemp.replace("temp=","").replace("'C\n",""))
        print rpztemp
        if loadavg[0] >= 0.99 or rpztemp>=tempyellow:
                yellowlight()
        if loadavg[1] >= 0.99 or rpztemp>=tempred:
                redlight()
        if loadavg[2] >= 0.99 or rpztemp>=tempbuzz:
                redlight()
                buzz()
        if loadavg[0]<0.99 and loadavg[1]<0.99 and loadavg[2]<0.99 and rpztemp<tempyellow:
                greenlight()
def main():
        print "Monitoring System Health"
        while True:
                try:
                        checkrpz()
                        time.sleep(5)
                except KeyboardInterrupt:
                        offlight()
                        break
if __name__ == '__main__':
        main()
