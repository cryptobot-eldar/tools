#Imports from modules, libraries and config files
import config
from pybittrex.client import Client
import requests
import time
import datetime
import hmac
import hashlib
import MySQLdb
import sys
import smtplib
#c = Client(api_key=config.key, api_secret=config.secret)   #Configuring bytrex client with API key/secret from config file
c=Client(api_key="", api_secret="")

TICK_INTERVAL = 900  # seconds


#The main function
def main():
    print('Starting buy module')


    # Running clock forever
    while True:
        start = time.time()
        tick()
        end = time.time()
        # Sleep the thread if needed
        if end - start < TICK_INTERVAL:
            time.sleep(TICK_INTERVAL - (end - start))

################################################################################################################
#what will be done every loop iteration
def tick():
    market_summ = c.get_market_summaries().json()['result']
    currtime = int(time.time())



    #global active
    for summary in market_summ: #Loop trough the market summary
        try:
            if available_market_list(summary['MarketName']):
                market = summary['MarketName']
                #Candle analisys
                lastcandle = get_candles(market, 'thirtymin')['result'][-1:]
                currentopen = float(lastcandle[0]['O'])
                currenthigh = float(lastcandle[0]['H'])
                hourpreviouscandle4 = get_candles(market, 'hour')['result'][-5:]
                hourprevopen4 = float(hourpreviouscandle4[0]['O'])
                fivehourcurrentopen = hourprevopen4
                hourpreviouscandle9 = get_candles(market, 'hour')['result'][-10:]
                hourprevopen9 = float(hourpreviouscandle9[0]['O'])
                hourpreviouscandle5 = get_candles(market, 'hour')['result'][-6:]
                hourprevclose5 = float(hourpreviouscandle5[0]['C'])
                fivehourprevopen = hourprevopen9
                fivehourprevclose = hourprevclose5
                lastcandle5 = get_candles(market, 'fivemin')['result'][-1:]
                currentlow5 = float(lastcandle5[0]['L'])
                currentopen5 = float(lastcandle5[0]['O'])
                currenthigh5 = float(lastcandle5[0]['H'])
                hourlastcandle = get_candles(market, 'hour')['result'][-1:]
                hourcurrentopen = float(hourlastcandle[0]['O'])
                hourcurrenthigh = float(hourlastcandle[0]['H'])
                timestamp = int(time.time())
            #Current prices
                last = float(summary['Last'])  #last price

                now = datetime.datetime.now()
                currenttime = now.strftime("%Y-%m-%d %H:%M")



                fivemin='NONE'
                thirtymin='NONE'
                hour='NONE'
                candles_status='OK'


                if last>currentopen5:
                    fivemin='U'
                elif last==currenthigh5:
                    fivemin='H'
                else:
                    fivemin='D'

                if last>currentopen:
                    thirtymin='U'
                elif last==currenthigh:
                    thirtymin='H'
                else:
                    thirtymin='D'

                if last>hourcurrentopen:
                    hour='U'
                elif last==hourcurrenthigh:
                    hour='H'
                else:
                    hour='D'


                try:
                    db = MySQLdb.connect("database-service", "cryptouser", "123456", "cryptodb")
                    cursor = db.cursor()
                    if status_orders(market, 4) == 1:
                        cursor.execute('insert into orderlogs(market, signals, time, orderid) values("%s", "%s", "%s", "%s")' % (market, str(currenttime)+' H: ' + str(hour) + ' 30min: ' + str(thirtymin)+ ' 5min: ' + str(fivemin)+' ' , currtime, status_orders(market, 0)))
                    else:
                        pass
                    db.commit()
                except MySQLdb.Error, e:
                    print "Error %d: %s" % (e.args[0], e.args[1])
                    sys.exit(1)
                finally:
                    db.close()


            else:
                pass
        except:
            continue





#Allowed currencies function for SQL
def available_market_list(marketname):
    db = MySQLdb.connect("database-service", "cryptouser", "123456", "cryptodb")
    cursor = db.cursor()
    market = marketname
    cursor.execute("SELECT * FROM markets WHERE active =1 and market = '%s'" % market)
    r = cursor.fetchall()
    for row in r:
        if row[1] == marketname:
            return True

    return False





def parameters():
    db = MySQLdb.connect("database-service", "cryptouser", "123456", "cryptodb")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM parameters")
    r = cursor.fetchall()
    for row in r:
        return (row[1]), (row[2]), (row[3]), (row[4]), (row[5]), (row[6]), (row[7]), (row[8]), (row[9]), (row[10]), (row[11]), (row[12]), (row[13]), (row[14]), (row[15]), (row[16]), (row[17]), (row[18]), (row[19]), (row[20]), (row[21]), (row[22]), (row[23]), (row[24])

    return 0







#Check active orders in mysql
def active_orders(marketname):
    db = MySQLdb.connect("database-service", "cryptouser", "123456", "cryptodb")
    cursor = db.cursor()
    market=marketname
    cursor.execute("SELECT * FROM orders WHERE active = 1 and market = '%s'" % market)
    #cursor.execute("SELECT o.*, m.market FROM orders o, markets m WHERE o.active = 1 and o.market_id = m.id and m.market like '%%'" % market)
    r = cursor.fetchall()
    for row in r:
        return int(row[4])

    return 0


#Check the status of active orders
# 2 - is quantity, 3 -is price, 4 - active/passive
def status_orders(marketname, value):
    db = MySQLdb.connect("database-service", "cryptouser", "123456", "cryptodb")
    cursor = db.cursor()
    market=marketname
    cursor.execute("SELECT * FROM orders WHERE active = 1 and market = '%s'" % market)
    #cursor.execute("SELECT o.*, m.market FROM orders o, markets m WHERE o.active = 1 and o.market_id = m.id and m.market like '%%'" % market)
    r = cursor.fetchall()
    for row in r:
        if row[1] == marketname:
            return row[value]

    return 0




def get_candles(market, tick_interval):
    url = 'https://bittrex.com/api/v2.0/pub/market/GetTicks?apikey=' + config.key + '&MarketName=' + market +'&tickInterval=' + str(tick_interval)
    return signed_request(url)


def signed_request(url):
    now = time.time()
    url += '&nonce=' + str(now)
    signed = hmac.new(config.secret, url.encode('utf-8'), hashlib.sha512).hexdigest()
    headers = {'apisign': signed}
    r = requests.get(url, headers=headers)
    return r.json()



def format_float(f):
    return "%.4f" % f


if __name__ == "__main__":
    main()
