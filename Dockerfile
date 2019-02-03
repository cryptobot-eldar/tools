FROM egaraev/basecentos:latest
COPY aftercount.py check_ai.py check_market_profits.py enable_market.py statistic.py candles.py check_candle_signals.py config.py start.sh service0.sh service1.sh service2.sh service3.sh service4.sh service5.sh service6.sh service7.sh btc_status.py service8.sh candle_situation.py /usr/local/bin/
RUN mkdir /usr/local/bin/data
WORKDIR /usr/local/bin
RUN chmod +x start.sh service0.sh service1.sh service2.sh service3.sh service4.sh service5.sh service6.sh service7.sh service8.sh
RUN rm -rf /etc/localtime
RUN ln -s /usr/share/zoneinfo/Europe/Warsaw /etc/localtime
ENTRYPOINT ["/usr/local/bin/start.sh"]
