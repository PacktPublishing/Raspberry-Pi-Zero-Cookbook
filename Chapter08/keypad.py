#!/usr/bin/env python
# Raspberry Pi Zero Cookbook
# Chapter 8 - Keypad Input
import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#Keypad Inputs
cols=[5,6,13,19]
rows=[26,16,20,21]
#4x4 Keypad matrix
keypad=[
[1,2,3,"A"],
[4,5,6,"B"],
[7,8,9,"C"],
["*",0,"#","D"]]
def main():
        #Set Pull-Up to Down on Row Pins
        for row in rows:
                GPIO.setup(row, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        #Set Column Pins for Output, Default LOW
        for col in cols:
                GPIO.setup(col, GPIO.OUT)
                GPIO.output(col, GPIO.LOW)
        print "Keypad Ready"
        while True:
                try:
                        #Turn on Column Pins in Sequence
                        for x, col in enumerate(cols):
                                if x==0:
                                        GPIO.output(cols[3], GPIO.LOW)
                                else:
                                        GPIO.output(cols[x-1], GPIO.LOW)
                                GPIO.output(cols[x], GPIO.HIGH)
                                #Check row inputs for each HIGH column and display if caught
                                for y,row in enumerate(rows):
                                        if GPIO.input(row)==1:
                                                print "Pressed: ",keypad[x][y]
                        time.sleep(0.2)
                except KeyboardInterrupt:
                        print "Crtl-C Detected"
                        break
if __name__=='__main__':
        main()
