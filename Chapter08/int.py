# Raspberry Pi Zero Cookbook
# Chapter 8
# Handing input interrupts
import time
import os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
#LED output pins
redpin=17
greenpin=18
bluepin=27
#Pushbutton input pin
buttonpin=23
togglea=20
toggleb=21
#Buzzer output pin
buzzerpin=22
#Configure inputs and outputs
GPIO.setup(redpin, GPIO.OUT)
GPIO.setup(greenpin, GPIO.OUT)
GPIO.setup(bluepin, GPIO.OUT)
GPIO.setup(buttonpin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(togglea, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(toggleb, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buzzerpin, GPIO.OUT)
buzzer = GPIO.PWM(buzzerpin, 0.5)
def main():
        alloff()
        print "Toggle Switch and press button"
        GPIO.add_event_detect(buttonpin,GPIO.FALLING,callback= buttonpress,bouncetime=200)
        try:
                while True:
                        time.sleep(0.5)
        except KeyboardInterrupt:
                print "Finished"
        finally:
                GPIO.cleanup()
def buttonpress(buttonpin):
        if GPIO.input(togglea)==False:
                print "Lights!"
                playlights()
        elif GPIO.input(toggleb)==False:
                print "Sounds!"
                playsounds()
        else:
                print "System!"
                print "Logged ",os.popen('vcgencmd measure_temp').readline()," at ",time.time()
def playsounds():
        e7=2637
        c7=2093
        g6=1568
        g7=3136
        e6=1319
        a6=1760
        b6=1976
        as6=1865
        seq=[g6,c7,g6,e6,a6,b6,as6,a6]
        buzzer.start(50)
        for note in seq:
                buzzer.ChangeFrequency(note)
                time.sleep(0.15)
        alloff()
def alloff():
        rgblight(0,0,0)
        buzzer.stop()
def playlights():
        for loop in range(0,3):
                for x in range(1,8):
                        colorcycle(x)
                        time.sleep(0.2)
        alloff()
def colorcycle(bincolor):
        rgb=list(bin(bincolor).replace("0b",""))
        if (len(rgb)==1):
                rgblight(0,0,1)
        if (len(rgb)==2):
                rgblight(0,int(rgb[0]),int(rgb[1]))
        if (len(rgb)==3):
                rgblight(int(rgb[0]),int(rgb[1]),int(rgb[2]))
def rgblight(r,g,b):
        #print r,g,b
        GPIO.output(redpin,r)
        GPIO.output(greenpin,g)
        GPIO.output(bluepin,b)
if __name__=="__main__":
        main()
