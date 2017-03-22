#!/usr/bin/env python
# Raspberry Pi Cookbook
# Chapter 6
# Multiple LEDs on Shift Register
import PiShiftPy as shift
import time
def main():
	shift.init()
	shift.write_all(0x00)
	while True:
		try:
			ledseq(1,0,0,0,0,0,0,0)
			ledseq(1,1,0,0,0,0,0,0)
			ledseq(1,1,1,0,0,0,0,0)
			ledseq(0,1,1,1,0,0,0,0)
			ledseq(0,0,1,1,1,0,0,0)
			ledseq(0,0,0,1,1,1,0,0)
			ledseq(0,0,0,0,1,1,1,0)
			ledseq(0,0,0,0,0,1,1,1)
			ledseq(0,0,0,0,0,0,1,1)
			ledseq(0,0,0,0,0,0,0,1)
			ledseq(0,0,0,0,0,0,1,1)
			ledseq(0,0,0,0,0,1,1,1)
			ledseq(0,0,0,0,1,1,1,0)
			ledseq(0,0,0,1,1,1,0,0)
			ledseq(0,0,1,1,1,0,0,0)
			ledseq(0,1,1,1,0,0,0,0)
			ledseq(1,1,1,0,0,0,0,0)
			ledseq(1,1,0,0,0,0,0,0)
		finally:
			ledseq(0,0,0,0,0,0,0,0)	

def ledseq(a,b,c,d,e,f,g,h):
	shift.push_bit(a)
	shift.push_bit(b)
	shift.push_bit(c)
	shift.push_bit(d)
	shift.push_bit(e)
	shift.push_bit(f)
	shift.push_bit(g)
	shift.push_bit(h)
	shift.write_latch()
	time.sleep(0.1)
if __name__ == "__main__":
	main()
