import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
#Set up GPIO 17,27,22 as our LED outputs
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

red = GPIO.PWM(22,50)
green = GPIO.PWM(23,50)
yellow = GPIO.PWM(24,50)

red.start(0)
green.start(0)
yellow.start(0)
while True:
        try:
                print "up!"
                for brightness in range(0, 101):
                        red.ChangeDutyCycle(brightness)
                        green.ChangeDutyCycle(brightness)
                        yellow.ChangeDutyCycle(brightness)
                        time.sleep(0.07)
                print "down!"
                for brightness in range (100, 0, -1):
                        red.ChangeDutyCycle(brightness)
                        green.ChangeDutyCycle(brightness)
                        yellow.ChangeDutyCycle(brightness)
                        time.sleep(0.07)
        except KeyboardInterrupt:
                print "Finished!"
        finally:
                red.stop()
                green.stop()
                yellow.stop()
                break
