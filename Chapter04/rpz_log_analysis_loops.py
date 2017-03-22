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
# the main function
def main():
	#Execute the summary function
	summary()
	#If the function returns without an error, return a 0 for success
	return 0
	
def summary():
	#Create variables for filenames of log files.
	startuplog = "/var/log/rpz_startup.log"
	templog = "/var/log/rpz_temp.log"
	#Set loop counters to zero
	temprows = 0
	rpzstarts = 0
	#Open the templog file, and read each line
	for row in open(templog):
		#Increment the log file counter
		temprows += 1
	#Print results
	print "There are " + str(temprows) + " measurements in the file " + templog
	#Loop through startup log file
	for row in open(startuplog):
		if row.startswith("RPZ startup"):
			rpzstarts += 1
	print "There are " + str(rpzstarts) + " RPZ Startups logged in file " + startuplog
	return 0

if __name__ == '__main__':
	main()

