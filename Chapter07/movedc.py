#!/usr/bin/env python
# Raspberry Pi Zero Cookbook
# DC Motor Control
import RPi.GPIO as GPIO
import time
import argparse
GPIO.setmode(GPIO.BCM)

input1 = 4  #To Red DC Lead
input2 = 17 #To Black DC Lead
enable1 = 18
GPIO.setwarnings(False)
GPIO.setup(input1, GPIO.OUT)
GPIO.setup(input2, GPIO.OUT)
GPIO.setup(enable1, GPIO.OUT)
motor = GPIO.PWM(enable1, 100)
motor.start(0)
def main():
        parser = argparse.ArgumentParser()
        parser.add_argument("speed",type=int,help="Motor Speed 0-99",choices=range(0,100))
        parser.add_argument("time",type=int,help="Time to run motor, in seconds")
        parser.add_argument("direction",help="Direction to turn the motor",choices=['forward','back'])
        args = parser.parse_args()
        if args.direction == "back":
                motor.start(1)
                back()
                time.sleep(args.time)
        else:
                motor.start(1)
                forward()
                time.sleep(args.time)
def forward():
        GPIO.output(input1, GPIO.HIGH)
        GPIO.output(input2, GPIO.LOW)
def back():
        GPIO.output(input1, GPIO.LOW)
        GPIO.output(input2, GPIO.HIGH)
if __name__ == "__main__":
        main()
