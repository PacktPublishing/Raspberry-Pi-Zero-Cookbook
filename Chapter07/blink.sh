#!/bin/bash
# Chapter 7 - Wiring Control (also used in Chapter 5 LED Control)
#parameters wiringPi Pin # and delay time in SECONDS (e.g. blink.sh 25 .5)
PIN=$1
DLY=$2
gpio mode ${PIN} output
while true; do
        gpio write ${PIN} 1;
        sleep ${DLY};
        gpio write ${PIN} 0;
        sleep ${DLY};
done
