#!/bin/bash
#Raspberry Pi Zero Cookbook
#Logs current RPZ System Temp 
TEMP=`/opt/vc/bin/vcgencmd measure_temp | cut -d "=" -f 2`
DATE=`date`
echo RPZ Temperature at $DATE: $TEMP
