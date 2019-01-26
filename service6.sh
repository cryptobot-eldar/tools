#!/bin/bash


while true
do



SERVICE6='check_candle_signals.py'

ps -ef | grep $SERVICE6 | grep -v grep
[ $?  -eq "0" ] && echo "$SERVICE6 process is running" || echo "$SERVICE6 process is not running, starting"; python2.7 /usr/local/bin/check_candle_signals.py


done