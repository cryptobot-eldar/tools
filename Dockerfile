FROM egaraev/basecentos:latest
COPY aftercount.py check_ai.py check_market_profits.py enable_market.py statistic.py candles.py check_candle_signals.py config.py start.sh /usr/local/bin/
RUN mkdir /usr/local/bin/data
WORKDIR /usr/local/bin
RUN chmod +x start.sh
ENTRYPOINT ["/usr/local/bin/start.sh"]
