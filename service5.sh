#!/bin/bash


while true
do


SERVICE5='candles.py'

ps -ef | grep $SERVICE5 | grep -v grep
[ $?  -eq "0" ] && echo "$SERVICE5 process is running" || echo "$SERVICE5 process is not running, starting"; python2.7 /usr/local/bin/candles.py

sleep 240

done