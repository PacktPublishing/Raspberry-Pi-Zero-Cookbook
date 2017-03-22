#!/usr/bin/env python
# Raspberry Pi Zero Cookbook
# Chapter 6
# Manipulating an RGB LED
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
#Set up GPIO 22,23,24 as our LED outputs
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

red = GPIO.PWM(24,50)
green = GPIO.PWM(23,50)
blue = GPIO.PWM(22,50)

#RGB Values
redbr=50
greenbr=50
bluebr=50

red.start(0)
green.start(0)
blue.start(0)

def main():
	rgblight(0,0,0)
	print "Blue"
	rgblight(0,0,100)
	time.sleep(2)
	print "Red"
	rgblight(100,0,0)
	time.sleep(2)
	print "Green"
	rgblight(0,100,0)
	time.sleep(2)
	print "Cyan"
	rgblight(0,100,100)
	time.sleep(2)
	print "Magenta"
	rgblight(100,0,100)
	time.sleep(2)
	print "Yellow"
	rgblight(100,100,0)
	time.sleep(2)
	print "White"
	rgblight(100,100,100)
	time.sleep(2)
	rgblight(0,0,0)
def rgblight(rpwm,gpwm,bpwm):
	red.ChangeDutyCycle(rpwm)
	green.ChangeDutyCycle(gpwm)
	blue.ChangeDutyCycle(bpwm)
if __name__== '__main__':
	main()
