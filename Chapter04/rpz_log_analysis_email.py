#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  rpz_log_analysis.py
#  
#  Copyright 2016  <pi@rpz14101>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
from pylab import *
import smtplib
startuplog = "/var/log/rpz_startup.log"
templog = "/var/log/rpz_temp.log"
graphfile = "/home/pi/share/ch4/rpz_temp_plot.png"

def main():
	#summary()
	#rpztempstats()
	#rpzplottemp(1440,0)
	rpzemailgraph(1440)
	return 0
	
def summary():
	#create variables for filenames of log files 
	global startuplog
	global templog
	temprows = 0
	rpzstarts = 0
	for row in open(templog):
		temprows += 1
	print "There are " + str(temprows) + " measurements in the file " + templog
	for row in open(startuplog):
		if row.startswith("RPZ startup"):
			rpzstarts += 1
	print "There are " + str(rpzstarts) + " RPZ Startups logged in file " + startuplog
	return 0

def rpztempstats():
	from time import strptime
	maxtemp = 0.0
	totalreadings = 0
	sumreadings = 0
	for row in open(templog):
		data = row.replace("RPZ Temperature at ","").split(": ")
		humandate = data[0]
		pydate = strptime(humandate,'%a %d %b %H:%M:%S %Z %Y')
		tempcelcius = float(data[1].split("'")[0])
		if tempcelcius >= maxtemp:
			maxtemp = tempcelcius
			maxtempdate = humandate
		totalreadings += 1
		sumreadings += tempcelcius
	print "Max Temperature of " + str(maxtemp) + "C on " + maxtempdate
	print "Average Temp: %.2fC" % float(sumreadings/totalreadings)
	return 0

def rpzplottemp(readings,savepng):
	import subprocess
	from time import strptime
	grfdt = []
	grftmp = []
	for row in open(templog):
		data = row.replace("RPZ Temperature at ","").split(": ")
		humandate = data[0]
		tempcelcius = float(data[1].split("'")[0])
		grfdt.append(humandate)
		grftmp.append(tempcelcius)	
	plt.plot(grftmp[-(readings)::])
	plt.ylabel("Degrees Celcius")
	plt.xlabel("Measurements")
	plt.title("RPZ Temperatures from " + grfdt[-(readings)] + " to " + grfdt[-1])
	if savepng == 1:
		plt.savefig(graphfile)
	else:
		plt.show()
	return 0
def rpzemailgraph(readings):
	from email.mime.image import MIMEImage
	from email.mime.multipart import MIMEMultipart
	rpzplottemp(readings,1)
	msg = MIMEMultipart()
	to = "esnajder@yahoo.com"
	frm = "noreply@rpz.local"
	msg['Subject'] = "RPZ Temperature Graphs"
	msg["From"] = frm
	msg["To"] = to
	msg.preamble = "Raspberry Pi Zero Temperature Output Graph"
	rpzgraph = open(graphfile, 'rb')
	rpzgraphimg = MIMEImage(rpzgraph.read())
	rpzgraph.close()
	msg.attach(rpzgraphimg)
	mailout = smtplib.SMTP('smtp.gmail.com',587)
	mailout.ehlo()
	mailout.starttls()
	mailout.ehlo()
	mailout.login('esnajder@gmail.com','mpfy mnha jdgo pcpq')
	mailout.sendmail(frm, to, msg.as_string())
	mailout.quit
	return 0

	
def rpztempcsv():
	from time import strptime
	for row in open(templog):
		data = row.replace("RPZ Temperature at ","").split(": ")
		humandate = data[0]
		pydate = strptime(humandate,'%a %d %b %H:%M:%S %Z %Y')
		tempcelcius = float(data[1].split("'")[0])
		csvdate = strftime('%Y%m%d %H:%M:%S %Z',pydate)
	
if __name__ == '__main__':
	main()

