#!/usr/bin/env python
# Raspberry Pi Zero Cookbook
# Chapter 6 
# Controlling a 16x2 LCD Display

import time
import subprocess
from lcdscreen import LCDScreen

def main():
	#Setup LCD Screen
	lcd = LCDScreen({'pin_rs':25,'pin_e':24,'pins_db':[23,17,21,22],'dimensions':[16,2]})
	lcd.clear()
	while True:
		try:
			#Collect Information to Display
			dt = subprocess.check_output(["date","+%F"])
			tm = subprocess.check_output(["date","+%T"])
			tmp = subprocess.check_output(["vcgencmd","measure_temp"])
			clk = subprocess.check_output(["cat","/sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq"])
			clock_mhz = str(float(clk)/1000000.00) + " MHz" 
			#Push information on to LCD
			l1 = lcd.push_up(dt)
			lcd.delay(2)
			l2 = lcd.push_up(tm)
			lcd.delay(2)
			l3 = lcd.push_up(tmp)
			lcd.delay(2)
			l4 = lcd.push_up(clock_mhz)
			lcd.delay(2)
		finally:
			lcd.clear()
if __name__ == "__main__":
	main()
