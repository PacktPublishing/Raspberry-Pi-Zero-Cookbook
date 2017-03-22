#!/usr/bin/env python
# Raspberry Pi Zero Cookbook
# Chapter 8
# Detecting Pushbutton Inputs
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
#LED output pins
redpin=17
greenpin=18
bluepin=27
#Pushbutton input pin
buttonpin=23
#Configure inputs and outputs
GPIO.setup(redpin, GPIO.OUT)
GPIO.setup(greenpin, GPIO.OUT)
GPIO.setup(bluepin, GPIO.OUT)
GPIO.setup(buttonpin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
def main():
        print "Press Button to Change Color"
        counter=1
        rgblight(1,0,0)
        while True:
                if GPIO.input(buttonpin)==False:
                        counter+=1
                        colorcycle(counter%9)
def colorcycle(bincolor):
        print bincolor
        rgb=list(bin(bincolor).replace("0b",""))
        if (len(rgb)==1):
                rgblight(0,0,1)
        if (len(rgb)==2):
                rgblight(0,int(rgb[0]),int(rgb[1]))
        if (len(rgb)==3):
                rgblight(int(rgb[0]),int(rgb[1]),int(rgb[2]))
def rgblight(r,g,b):
        GPIO.output(redpin,r)
        GPIO.output(greenpin,g)
        GPIO.output(bluepin,b)
if __name__== '__main__':
        main()
