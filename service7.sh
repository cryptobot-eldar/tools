#!/bin/bash


while true
do



SERVICE7='btc_status.py'

ps -ef | grep $SERVICE7 | grep -v grep
[ $?  -eq "0" ] && echo "$SERVICE7 process is running" || echo "$SERVICE7 process is not running, starting"; python2.7 /usr/local/bin/btc_status.py


done