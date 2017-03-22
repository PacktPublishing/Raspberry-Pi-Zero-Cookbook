#!/bin/env python
# Chpater 7 Hardware Control
# Working with the PiFace Controller
import pifacedigitalio
pf = pifacedigitalio.PiFaceDigital()
import time
def lightseq(o0,o1,o2,o3,o4,o5,o6,o7):
        pf.output_pins[0].value=o0
        pf.output_pins[1].value=o1
        pf.output_pins[2].value=o2
        pf.output_pins[3].value=o3
        pf.output_pins[4].value=o4
        pf.output_pins[5].value=o5
        pf.output_pins[6].value=o6
        pf.output_pins[7].value=o7

def dothecylon():
        dly=0.2
        lightseq(1,0,0,0,0,0,0,0)
        time.sleep(dly)
        lightseq(1,1,0,0,0,0,0,0)
        time.sleep(dly)
        lightseq(1,1,1,0,0,0,0,0)
        time.sleep(dly)
        lightseq(0,1,1,1,0,0,0,0)
        time.sleep(dly)
        lightseq(0,0,1,1,1,0,0,0)
        time.sleep(dly)
        lightseq(0,0,0,1,1,1,0,0)
        time.sleep(dly)
        lightseq(0,0,0,0,1,1,1,0)
        time.sleep(dly)
        lightseq(0,0,0,0,0,1,1,1)
        time.sleep(dly)
        lightseq(0,0,0,0,0,0,1,1)
        time.sleep(dly)
        lightseq(0,0,0,0,0,0,0,1)
        time.sleep(dly)
        lightseq(0,0,0,0,0,0,1,1)
        time.sleep(dly)
        lightseq(0,0,0,0,0,1,1,1)
        time.sleep(dly)
        lightseq(0,0,0,0,1,1,1,0)
        time.sleep(dly)
        lightseq(0,0,0,1,1,1,0,0)
        time.sleep(dly)
        lightseq(0,0,1,1,1,0,0,0)
        time.sleep(dly)
        lightseq(0,1,1,1,0,0,0,0)
        time.sleep(dly)
        lightseq(1,1,1,0,0,0,0,0)
        time.sleep(dly)
        lightseq(1,1,0,0,0,0,0,0)
        time.sleep(dly)

def main():
        print "Press S0 to click on relay and LED"
        print "Press S1 to toggle LED"
        print "Press S2 to activate Cylon"
        print "Press S3 to exit"
        while True:
                if pf.input_pins[0].value==1:
                        time.sleep(.2)
                        pf.output_pins[0].value=1
                        time.sleep(1)
                        pf.output_pins[0].value=0
                elif pf.input_pins[1].value==1:
                        time.sleep(.2)
                        state=pf.output_pins[3].value
                        print "Value: ", state
                        time.sleep(.2)
                        if state==1:
                                pf.output_pins[3].value=0
                        else:
                                pf.output_pins[3].value=1
                elif pf.input_pins[2].value==1:
                        time.sleep(.1)
                        print "Do the Cylon! Crtl-C to Stop"
                        while True:
                                try:
                                        dothecylon()
                                except KeyboardInterrupt:
                                        lightseq(0,0,0,0,0,0,0,0)
                                        break
                elif pf.input_pins[3].value==1:
                        break
if __name__ == "__main__":
        main()
