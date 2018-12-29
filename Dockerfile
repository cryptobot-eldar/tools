FROM egaraev/basecentos:latest
COPY aftercount.py check_ai.py check_market_profits.py enable_market.py statistic.py config.py start.sh /usr/local/bin/
WORKDIR /usr/local/bin
RUN chmod +x start.sh
RUN touch /var/log/work.log
ENTRYPOINT ["/usr/local/bin/start.sh"]
