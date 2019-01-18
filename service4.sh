#!/bin/bash


while true
do

SERVICE4='statistic.py'

ps -ef | grep $SERVICE4 | grep -v grep
[ $?  -eq "0" ] && echo "$SERVICE4 process is running" || echo "$SERVICE4 process is not running, starting"; python /usr/local/bin/statistic.py

done
