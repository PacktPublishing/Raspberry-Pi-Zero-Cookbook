#!/usr/bin/env python
# Raspberry Pi Zero Cookbook
# Chapter 8
# Toggle Switch and Debouncing
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#LED output pins
led1=19
led2=26
#Pushbutton input pin
buttonpin=23
togglea=20
toggleb=21
#Set debounce time
debounce=0.2
#Configure inputs and outputs
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.output(led1, GPIO.LOW)
GPIO.output(led2, GPIO.LOW)
GPIO.setup(buttonpin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(togglea, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(toggleb, GPIO.IN, pull_up_down=GPIO.PUD_UP)
def main():
        lastexec=time.time()
        time.sleep(debounce)
        onoff=0
        print "Ready, Toggle Switch to light an LED, push button to turn both LEDs on/off"
        while True:
                now=time.time()
                if GPIO.input(togglea)==False and now-lastexec>debounce:
                        GPIO.output(led1,GPIO.HIGH)
                        lastexec=time.time()
                elif GPIO.input(toggleb)==False and now-lastexec>debounce:
                        if GPIO.input(toggleb)==False:
                                GPIO.output(led2,GPIO.HIGH)
                                lastexec=time.time()
                        else:
                                GPIO.output(led2,GPIO.LOW)
                elif GPIO.input(buttonpin)==False and now-lastexec>debounce:
                        onoff= not onoff
                        GPIO.output(led1,onoff)
                        GPIO.output(led2,onoff)
                        lastexec=time.time()
                elif GPIO.input(togglea)==True and GPIO.input(toggleb)==True and onoff==0:
                        GPIO.output(led1,GPIO.LOW)
                        GPIO.output(led2,GPIO.LOW)
if __name__=="__main__":
        main()
