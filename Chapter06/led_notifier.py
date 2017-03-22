#!/usr/bin/env python
# Raspberry Pi Zero Cookbook
# Chapter 6
# New Email and Tweet LED Notifier
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time
import imaplib
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
#Set up GPIO 22,23,24 as our LED outputs
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

red = GPIO.PWM(22,50)
green = GPIO.PWM(23,50)
blue = GPIO.PWM(24,50)

#Twitter API Key Information
consumer_token = "DGgV5UDKteuySrEOf9TI3a6s7" 
consumer_secret = "3XH0YojKCSQUUl8PmYg9sWOywm1A74jPehDv84HMmXrxFMMIa8"
access_token = "1929310489-AzPLsAJYAn8Vxg7XPQzFZx1KhLCfvowZWPPt5S3"
access_secret = "4Awv8riHjzw4jeeSoCBwbaaLiT1eTqGhsjaNwM3z861Vm"

#String to Search on Twitter
searchstring = "python"

#Set up Listener for Twitter
class RPZStreamListener(StreamListener):
        def on_data(self, data):
                blinkblue()
                return True
        def on_error(self, status):
                print(status)

def main():
	red.start(0)
	green.start(0)
	blue.start(0)
	print "online"
	green.ChangeDutyCycle(100)
	auth = OAuthHandler(consumer_token, consumer_secret)
        auth.set_access_token(access_token, access_secret)
        sl = RPZStreamListener()
        stream = Stream(auth, sl)
        #Start Stream to Check for New Tweets
	stream.filter(track=[searchstring],async=True)
	#Run Loop to check for new email every 10 seconds
	while True:
		try:
			emailcheck()
			time.sleep(10)
		except KeyboardInterrupt:
			print "Finished!"			
			red.stop()
			green.stop()
			blue.stop()
			break
		except:
			print "Error: ", sys.exc_info()[0]
def blinkred():
	for x in range(0,5):
		red.ChangeDutyCycle(100)
		time.sleep(0.1)
		red.ChangeDutyCycle(0)
		time.sleep(0.1)
def blinkblue():
	for x in range(0,5):
		blue.ChangeDutyCycle(100)
		time.sleep(0.1)
		blue.ChangeDutyCycle(0)
		time.sleep(0.1)
def emailcheck():
	mailin = imaplib.IMAP4_SSL('imap.gmail.com')
        mailin.login('esnajder@gmail.com','mpfy mnha jdgo pcpq')
	mailin.list()
	mailin.select('inbox')
	(retcode, messages) = mailin.search(None, 'UNSEEN')
	if retcode == 'OK':
		if messages[0] != "":
			blinkred()
if __name__ == "__main__":
	main()
