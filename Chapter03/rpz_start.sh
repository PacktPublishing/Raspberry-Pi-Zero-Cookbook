#!/bin/bash
#Raspberry Pi Zero Cookbook
#Starup Log Script
#Logs basic RPZ Info on system startup 
TEMP=`/opt/vc/bin/vcgencmd measure_temp | cut -d "=" -f 2`
DATE=`date`
GPU=`/opt/vc/bin/vcgencmd get_mem gpu | cut -d "=" -f 2`
ARM=`/opt/vc/bin/vcgencmd get_mem arm | cut -d "=" -f 2`
STATUS=`/opt/vc/bin/vcgencmd pm_get_status`
echo RPZ startup at $DATE>>/var/log/rpz_startup.log
echo Current core temperature $TEMP>>/var/log/rpz_startup.log
echo GPU RAM $GPU - CPU RAM $ARM>>/var/log/rpz_startup.log
echo RPZ Status: $STATUS>>/var/log/rpz_startup.log
