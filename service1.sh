#!/bin/bash


while true
do


SERVICE1='check_ai.py'

ps -ef | grep $SERVICE1 | grep -v grep
[ $?  -eq "0" ] && echo "$SERVICE1 process is running" || echo "$SERVICE1 process is not running, starting"; python2.7 /usr/local/bin/check_ai.py

sleep 3600

done