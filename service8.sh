#!/bin/bash


while true
do



SERVICE8='candle_situation.py'

ps -ef | grep $SERVICE8 | grep -v grep
[ $?  -eq "0" ] && echo "$SERVICE8 process is running" || echo "$SERVICE8 process is not running, starting"; python2.7 /usr/local/bin/candle_situation.py



done