#!/bin/bash


while true
do

SERVICE0='aftercount.py'

ps -ef | grep $SERVICE0 | grep -v grep
[ $?  -eq "0" ] && echo "$SERVICE0 process is running" || echo "$SERVICE0 process is not running, starting"; python2.7 /usr/local/bin/aftercount.py

sleep 120

done