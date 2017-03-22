#!/usr/bin/env python
# Raspberry Pi Cookbook
# Chapter 6
# Controlling an 8x8 LED Matrix
# Requires the MAX7219 Library
import max7219.led as led

device = led.matrix()
message = raw_input('Enter message: ')
device.show_message(message)

