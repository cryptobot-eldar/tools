#!/bin/bash


while true
do


SERVICE3='enable_market.py'

ps -ef | grep $SERVICE3 | grep -v grep
[ $?  -eq "0" ] && echo "$SERVICE3 process is running" || echo "$SERVICE3 process is not running, starting"; python2.7 /usr/local/bin/enable_market.py


done
