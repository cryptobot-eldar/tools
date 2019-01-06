#!/bin/bash
#exec &>>/var/log/work.log

while true
do

SERVICE0='aftercount.py'

if ps ax | grep -v grep | grep $SERVICE0 > /dev/null
then
    echo "$SERVICE0 service running "
else
    echo there is no such "$SERVICE0 service, starting"
    python /usr/local/bin/aftercount.py
fi


SERVICE1='check_ai.py'

if ps ax | grep -v grep | grep $SERVICE1 > /dev/null
then
    echo "$SERVICE1 service running "
else
    echo there is no such "$SERVICE1 service, starting"
    python /usr/local/bin/check_ai.py
fi



SERVICE2='check_market_profits.py'

if ps ax | grep -v grep | grep $SERVICE2 > /dev/null
then
    echo "$SERVICE2 service running "
else
    echo there is no such "$SERVICE2 service, starting"
    python /usr/local/bin/check_market_profits.py
fi


SERVICE3='enable_market.py'

if ps ax | grep -v grep | grep $SERVICE3 > /dev/null
then
    echo "$SERVICE3 service running "
else
    echo there is no such "$SERVICE3 service, starting"
    python /usr/local/bin/enable_market.py
fi


SERVICE4='statistic.py'

if ps ax | grep -v grep | grep $SERVICE4 > /dev/null
then
    echo "$SERVICE4 service running "
else
    echo there is no such "$SERVICE4 service, starting"
    python /usr/local/bin/statistic.py
fi


SERVICE5='candles.py'

if ps ax | grep -v grep | grep $SERVICE5 > /dev/null
then
    echo "$SERVICE5 service running "
else
    echo there is no such "$SERVICE5 service, starting"
    python /usr/local/bin/candles.py
fi



SERVICE6='check_candle_signals.py'

if ps ax | grep -v grep | grep $SERVICE6 > /dev/null
then
    echo "$SERVICE6 service running "
else
    echo there is no such "$SERVICE6 service, starting"
    python /usr/local/bin/check_candle_signals.py
fi






sleep 10
done
