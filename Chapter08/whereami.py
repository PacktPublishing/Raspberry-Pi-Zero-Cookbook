#/usr/bin/env python
#Raspberry Pi Zero Cookbook
#Chapter 8 - Using a GPS Board
import time
import requests
import RPi.GPIO as GPIO
from gps import *
import json
apikey = "<<YOUR GOOGLE API KEY HERE>>"
logfile = "whereami.log"
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
buttonpin = 23
#Google geocode API exmaple
#https://maps.googleapis.com/maps/api/geocode/json?latlng=40.714224,-73.961452&key=YOUR_API_KEY
mapurl = "https://maps.googleapis.com/maps/api/geocode/json"
GPIO.setup(buttonpin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
def main():
        print "Press the button to log your location"
        try:
                while True:
                        if GPIO.input(buttonpin)==False:
                                time.sleep(0.2)
                                getfix()
        except KeyboardInterrupt:
                print "Finished!"
        finally:
                GPIO.cleanup()
def getfix():
        global ts
        whereami = gps(mode=WATCH_ENABLE)
        whereami.next()
        while whereami.data['class'] != 'TPV':
                whereami.next()
        lat = whereami.fix.latitude
        lng = whereami.fix.longitude
        alt = whereami.fix.altitude
        ts = whereami.data['time']
        latlng=str(lat)+","+str(lng)
        whereami.close()
        apiparams = {"latlng":latlng,"location_type":"APPROXIMATE","key":apikey}
        response = requests.get(mapurl,params=apiparams)
        #If you run into problems you can test the URL output by uncommenting the line below
        #print response.url
        y = json.loads(response.text,object_hook=findloc)
        logout = open(logfile,'a+')
        logout.write(ts+"\t"+str(lat)+"\t"+str(lng)+"\t"+str(alt)+"\n")
        logout.close()
def findloc(dct):
        global ts
        detail_level=["locality","political"]
        if "formatted_address" in dct:
                if dct["types"]==detail_level:
                        print "GPS fix in",dct["formatted_address"],"at",ts
                        #return dct["formatted_address"];
if __name__=="__main__":
        main()
