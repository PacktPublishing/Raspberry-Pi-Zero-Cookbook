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
startuplog = "/var/log/rpz_startup.log"
templog = "/var/log/rpz_temp.log"

def main():
	summary()
	rpztempstats()
	rpzplottemp(1440)
	return 0
	
def summary():
	#create variables for filenames of log files 
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
	maxtemp = 0.0
	totalreadings = 0
	sumreadings = 0
	for row in open(templog):
		data = row.replace("RPZ Temperature at ","").split(": ")
		humandate = data[0]
		tempcelcius = float(data[1].split("'")[0])
		if tempcelcius >= maxtemp:
			maxtemp = tempcelcius
			maxtempdate = humandate
		totalreadings += 1
		sumreadings += tempcelcius
	print "Max Temperature of " + str(maxtemp) + "C on " + maxtempdate
	print "Average Temp: %.2fC" % float(sumreadings/totalreadings)
	return 0

def rpzplottemp(readings):
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
	plt.show()
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

