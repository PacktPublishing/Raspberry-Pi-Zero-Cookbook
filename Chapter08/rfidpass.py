#!/usr/bin/env python
# Raspberry Pi Zero Cookbook
# Chapter 8 - RFID Card Reader Control
import time
import RPi.GPIO as GPIO
from pirc522 import RFID
#Use Board Mode to stay consistent with RFID and SPI Libraries
GPIO.setmode(GPIO.BOARD)
#Set allow and deny files
allowfile="./rfid_allow.txt"
denyfile="./rfid_deny.txt"
#led output pins
redpin=38
greenpin=40
GPIO.setwarnings(False)
GPIO.setup(redpin,GPIO.OUT)
GPIO.setup(greenpin,GPIO.OUT)
GPIO.output(redpin,1)
GPIO.output(greenpin,0)
scanner = RFID()
def main():
        print "Scanner Ready"
        try:
                while True:
                        (error,resp) = scanner.request()
                        if not error:
                                (error,uid)=scanner.anticoll()
                                if not error:
                                        print "Detected ",uid
                                        checkpass(uid)
        except KeyboardInterrupt:
                print "Scanner Stopped"
        finally:
                GPIO.output(redpin,0)
                GPIO.output(greenpin,0)
def checkpass(uid):
        nolist=open(denyfile,'a+')
        for baduid in nolist:
                idsplit=baduid.split(",")
                if int(idsplit[0])==uid[0] and int(idsplit[1])==uid[1] and int(idsplit[2])==uid[2] and int(idsplit[3])==uid[3] and int(idsplit[4])==uid[4]:
                        print "Detected UID on blocked list"
                        for x in range(0,20):
                                GPIO.output(redpin,0)
                                time.sleep(0.1)
                                GPIO.output(redpin,1)
                                time.sleep(0.1)
                        return
        yeslist=open(allowfile,'a+')
        for gooduid in yeslist.readlines():
                idsplit=gooduid.split(",")
                if int(idsplit[0])==uid[0] and int(idsplit[1])==uid[1] and int(idsplit[2])==uid[2] and int(idsplit[3])==uid[3] and int(idsplit[4])==uid[4]:
                        print "Detected UID on allow list"
                        GPIO.output(redpin,0)
                        for x in range(0,20):
                                GPIO.output(greenpin,1)
                                time.sleep(0.1)
                                GPIO.output(greenpin,0)
                                time.sleep(0.1)
                        GPIO.output(redpin,1)
                        return
        newrfid = raw_input('New ID Detected. (A)dd\(B)lock\(I)gnore?')
        print newrfid
        if newrfid=="A":
                addrfid=str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])+","+str(uid[4])+"\n"
                yeslist.write(addrfid)
                print "Added to Allow List"
        elif newrfid=="B":
                addrfid=str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])+","+str(uid[4])+"\n"
                nolist.write(addrfid)
                print "Added to blocked list"
        else:
                print "No action taken"

if __name__=='__main__':
        main()
