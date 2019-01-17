#!/bin/bash
#exec &>>/var/log/work.log

while true
do

SERVICE0='aftercount.py'

ps -ef | grep $SERVICE0 | grep -v grep
[ $?  -eq "0" ] && echo "$SERVICE0 process is running" || echo "$SERVICE0 process is not running, starting"; python /usr/local/bin/aftercount.py



SERVICE1='check_ai.py'

ps -ef | grep $SERVICE1 | grep -v grep
[ $?  -eq "0" ] && echo "$SERVICE1 process is running" || echo "$SERVICE1 process is not running, starting"; python /usr/local/bin/check_ai.py




SERVICE2='check_market_profits.py'

ps -ef | grep $SERVICE2 | grep -v grep
[ $?  -eq "0" ] && echo "$SERVICE2 process is running" || echo "$SERVICE2 process is not running, starting"; python /usr/local/bin/check_market_profits.py




SERVICE3='enable_market.py'

ps -ef | grep $SERVICE3 | grep -v grep
[ $?  -eq "0" ] && echo "$SERVICE3 process is running" || echo "$SERVICE3 process is not running, starting"; python /usr/local/bin/enable_market.py




SERVICE4='statistic.py'

ps -ef | grep $SERVICE4 | grep -v grep
[ $?  -eq "0" ] && echo "$SERVICE4 process is running" || echo "$SERVICE4 process is not running, starting"; python /usr/local/bin/statistic.py



SERVICE5='candles.py'

ps -ef | grep $SERVICE5 | grep -v grep
[ $?  -eq "0" ] && echo "$SERVICE5 process is running" || echo "$SERVICE5 process is not running, starting"; python /usr/local/bin/candles.py





SERVICE6='check_candle_signals.py'

ps -ef | grep $SERVICE6 | grep -v grep
[ $?  -eq "0" ] && echo "$SERVICE6 process is running" || echo "$SERVICE6 process is not running, starting"; python /usr/local/bin/check_candle_signals.py




sleep 10
done
