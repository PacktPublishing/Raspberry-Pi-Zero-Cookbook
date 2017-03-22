#!/usr/bin/env python
# Raspberry Pi Zero Cookbook
# Stepper Motor Control
import RPi.GPIO as GPIO
import time
import argparse
GPIO.setmode(GPIO.BCM)

input1 = 4  #To A1 Coil
input2 = 17 #To A2 Coil
input3 = 24 #To B1 Coil
input4 = 23 #To B2 Coil
enable1 = 18
GPIO.setwarnings(False)
GPIO.setup(enable1, GPIO.OUT)
GPIO.setup(input1, GPIO.OUT)
GPIO.setup(input2, GPIO.OUT)
GPIO.setup(input3, GPIO.OUT)
GPIO.setup(input4, GPIO.OUT)

def main():
        parser = argparse.ArgumentParser()
        parser.add_argument("steps",type=int,help="Number of steps to turn the motor")
        parser.add_argument("stepdelay",type=int,help="Delay between steps, in milliseconds")
        parser.add_argument("direction",help="Direction to turn the motor",choices=['forward','back'])
        args = parser.parse_args()
        delay = args.stepdelay/1000.00
        if args.direction == "back":
                for x in range(1,args.steps):
                        step_4(delay)
                        step_3(delay)
                        step_2(delay)
                        step_1(delay)
        else:
                for x in range(1,args.steps):
                        step_1(delay)
                        step_2(delay)
                        step_3(delay)
                        step_4(delay)

def step_1(delay):
        set_step(1,0,1,0,delay)
def step_2(delay):
        set_step(0,1,1,0,delay)
def step_3(delay):
        set_step(0,1,0,1,delay)
def step_4(delay):
        set_step(1,0,0,1,delay)
def set_step(a1,a2,b1,b2,delay):
        GPIO.output(input1,a1)
        GPIO.output(input2,a2)
        GPIO.output(input3,b1)
        GPIO.output(input4,b2)
        time.sleep(delay)

if __name__ == "__main__":
        main()
