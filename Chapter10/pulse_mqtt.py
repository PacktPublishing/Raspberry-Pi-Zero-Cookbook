#!/usr/bin/env python
# Raspberry Pi Zero Cookbook
# Chapter 10
# Pulse Sensor to MQTT
#
import sys
import math
import time
import mcp3008
import paho.mqtt.publish as publish

def main():
        with mcp3008.MCP3008() as adc:
                while True:
                        p1 = adc.read([mcp3008.CH2])[0]
                        publish.single("humannode1/pulse",p1,  hostname="192.168.2.83")
                        time.sleep(0.2)
if __name__=="__main__":
        main()
