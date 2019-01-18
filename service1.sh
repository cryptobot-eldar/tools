#!/bin/bash


while true
do


SERVICE1='check_ai.py'

ps -ef | grep $SERVICE1 | grep -v grep
[ $?  -eq "0" ] && echo "$SERVICE1 process is running" || echo "$SERVICE1 process is not running, starting"; python /usr/local/bin/check_ai.py


done