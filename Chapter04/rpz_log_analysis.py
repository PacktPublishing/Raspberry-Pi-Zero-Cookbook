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
import argparse
startuplog = "/var/log/rpz_startup.log"
templog = "/var/log/rpz_temp.log"
graphfile = "/home/pi/share/ch4/rpz_temp_plot.png"
csvfile = "/home/pi/share/ch4/rpz_temps.csv"

def main():
	parser = argparse.ArgumentParser(description="Raspberry Pi Zero Log Analysis Utility",epilog="Select any function or combination of functions.")
	parser.add_argument("--summary",help="Show RPZ Logs Summary",action="store_true")
	parser.add_argument("--stats",help="Show RPZ Temperature Log Statistics", action="store_true")
	parser.add_argument("--plot",metavar="READINGS",help="Show RPZ Plot for X measurements",type=int)
	parser.add_argument("--email",metavar="READINGS",help="Email RPZ Plot for X measnurements",type=int)
	parser.add_argument("--csv",help="Export CSV File of Temperature Data",action="store_true")
	parser.add_argument("--spreadsheet",help="Upload RPZ Temperature Data to Google Spreadsheets",action="store_true")
	args = parser.parse_args()
	if args.summary:
		summary()
	if args.stats:
		rpztempstats()
	if args.plot:
		rpzplottemp(args.plot,0)
	if args.email:
		rpzemailgraph(args.email)
	if args.csv:
		rpztempcsvexport()
	if args.spreadsheet:
		rpztempgoogleexport()
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

	
def rpztempcsvexport():
	from time import strptime, strftime
	import csv
	csvdata = [[]]
	for row in open(templog):
		data = row.replace("RPZ Temperature at ","").split(": ")
		humandate = data[0]
		pydate = strptime(humandate,'%a %d %b %H:%M:%S %Z %Y')
		tempcelcius = float(data[1].split("'")[0])
		csvdateformat = strftime('%Y%m%d %H:%M:%S %Z',pydate)
		csvdata.append([csvdateformat,tempcelcius])
		#print csvdateformat
	#print csvdata
	csvout = csv.writer(open(csvfile,"w"))
	csvout.writerows(csvdata)
	print "File written to %s" % csvfile
	return 0
	
def rpztempgoogleexport():
	from apiclient.discovery import build
	from time import strptime, strftime
	import oauth2client
	from oauth2client import client, file, tools
	from httplib2 import Http
	
	nowtime = datetime.datetime.now()
	sheetname = "RPZ Templog as of " + str(nowtime)
	SCOPES = "https://www.googleapis.com/auth/spreadsheets"
	CLIENT_SECRET_FILE = "/home/pi/client_secrets.json"
	APPLICATION_NAME = "RPZ"
	store = file.Storage('storage.json')
	creds = store.get()
	if not creds or creds.invalid:
		flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
		creds = tools.run_flow(flow,store)
	NEWSHEET = build('sheets','v4', http=creds.authorize(Http()))
	DATA = {"properties": {"title": sheetname}}
	sheet = NEWSHEET.spreadsheets().create(body=DATA).execute()
	SHEET_ID = sheet['spreadsheetId']
	FIELDS = ["LogDate","TempC"]
	sheetdata = [FIELDS]
	for row in open(templog):
		data = row.replace("RPZ Temperature at ","").split(": ")
		humandate = data[0]
		pydate = strptime(humandate,'%a %d %b %H:%M:%S %Z %Y')
		sheetdate = strftime('%Y/%m/%d %H:%M:%S %Z',pydate)
		tempcelcius = float(data[1].split("'")[0])
		sheetdata.append([sheetdate,tempcelcius])
	NEWSHEET.spreadsheets().values().update(spreadsheetId=SHEET_ID,range="A1", body={"values":sheetdata},valueInputOption="RAW").execute()
	print "Your new spreadsheet is available or your account named %s" % sheetname
	return 0	
	
if __name__ == '__main__':
	main()

