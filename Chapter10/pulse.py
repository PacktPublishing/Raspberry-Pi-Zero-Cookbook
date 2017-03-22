#!/usr/bin/env python
# Raspberry Pi Zero Cookbook
# Chapter 10
# Pulse Sensor with Python!
#
import sys
import math
import time
import mcp3008
def main():
        with mcp3008.MCP3008() as adc:
                while True:
                        p1 = adc.read([mcp3008.CH2])[0]
                        print p1
                        for i in range(p1 / 100):
                                print ".",
                        time.sleep(0.1)
if __name__=="__main__":
        main()
