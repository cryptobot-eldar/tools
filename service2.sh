#!/bin/bash


while true
do

SERVICE2='check_market_profits.py'

ps -ef | grep $SERVICE2 | grep -v grep
[ $?  -eq "0" ] && echo "$SERVICE2 process is running" || echo "$SERVICE2 process is not running, starting"; python2.7 /usr/local/bin/check_market_profits.py

sleep 170

done