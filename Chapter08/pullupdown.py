#!/usr/bin/env python
# Raspberry Pi Zero Cookbook
# Chapter 8
# Pull-up and Pull-down Cicuit GPIO Settings
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#LED output pins
#Pull-up circuit goes to ground
pullup=23
#Pull-down circuit goes to 3V
pulldown=17
#Set Up GPIO pins for buttons
GPIO.setup(pullup, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pulldown, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
def main():
        print "Started. "
        print "Pull-up Circuit reads ",GPIO.input(pullup),"(",bool(GPIO.input(pullup)),")"
        print "Pull-down Circuit reads ", GPIO.input(pulldown),"(",bool(GPIO.input(pulldown)),")"
        try:
                while True:
                        if GPIO.input(pulldown)==True:
                                print "Pull-down Pressed and now reads",GPIO.input(pulldown),"(",bool(GPIO.input(pulldown)),")"
                                time.sleep(0.5)
                        elif GPIO.input(pullup)==False:
                                print "Pull-up Pressed and now reads",GPIO.input(pullup),"(",bool(GPIO.input(pullup)),")"
                                time.sleep(0.5)
        except KeyboardInterrupt:
                print "Finished"
        finally:
                GPIO.cleanup()
if __name__=="__main__":
        main()
