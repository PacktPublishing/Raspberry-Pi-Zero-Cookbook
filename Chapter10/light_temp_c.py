#!/usr/bin/env python
# Raspberry Pi Zero Cookbook
# Chapter 10
# Script for communicating temp and light to Node Red
#
import sys
import math
import time
import mcp3008
vref = 3.30
r1 = 10000.00
kelvin=273.15
bitcoeff = 3.3/1024.0
ca =  0.001176724715543
cb = 0.000235156521144
cc = 0.000000088030003
t0 = 25.00 + kelvin
r0 = 20000.00
b = 10000.00
def main():
        with mcp3008.MCP3008() as adc:
                t1 = adc.read([mcp3008.CH0])[0]*bitcoeff
                l1 = adc.read([mcp3008.CH1])[0]*bitcoeff
                lr = (vref*r1)/(vref-l1)
                tr = (vref*r1)/(vref-t1)
                #print lr
                #print l1, t1
                invtmpk = (1/t0) + (1/b)*math.log1p(tr/r0)
                tempc = (1/invtmpk) - kelvin
                print tempc, lr
if __name__=="__main__":
        main()
