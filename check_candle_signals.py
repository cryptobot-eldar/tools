import MySQLdb
from pybittrex.client import Client
import os

c=Client(api_key='', api_secret='')

def main():
    print('Starting candle signals checking module')

    AI()


def AI():
    market_summ = c.get_market_summaries().json()['result']
    open('data/out18_tmp.csv', 'w').close()
    open('data/out19_tmp.csv', 'w').close()
    open('data/out20_tmp.csv', 'w').close()
    for summary in market_summ: #Loop trough the market summary
            if available_market_list(summary['MarketName']):
                market = summary['MarketName']
                if summ_ai(market)>-1:
                    print market, summ_ai(market), count(market)
                    f= open('data/out18_tmp.csv', 'a')
                    print >> f, str(market)
                    f1=open('data/out19_tmp.csv', 'a')
                    print >>f1, summ_ai(market)
                    f2 = open('data/out20_tmp.csv', 'a')
                    print >> f2, count(market)
    os.rename('data/out18_tmp.csv', 'data/out18.csv')
    os.rename('data/out19_tmp.csv', 'data/out19.csv')
    os.rename('data/out20_tmp.csv', 'data/out20.csv')




def summ_ai(marketname):
    db = MySQLdb.connect("database-service", "cryptouser", "123456", "cryptodb")
    cursor = db.cursor()
    market=marketname
    cursor.execute("SELECT SUM(result) FROM candlepredict where market= '%s'" % market)
    r = cursor.fetchall()
    for row in r:
#        if row[0] is not None:
        if row[0]!=0:
            return row[0]

    return 0




def count(marketname):
    db = MySQLdb.connect("database-service", "cryptouser", "123456", "cryptodb")
    cursor = db.cursor()
    market=marketname
    cursor.execute("SELECT COUNT(*) FROM candlepredict where market= '%s'" % market)
    r = cursor.fetchall()
    for row in r:
#        if row[0] is not None:
        if row[0] != 0:
            return row[0]

    return 0


def available_market_list(marketname):
    db = MySQLdb.connect("database-service", "cryptouser", "123456", "cryptodb")
    cursor = db.cursor()
    market = marketname
    cursor.execute("SELECT * FROM markets WHERE enabled =1")
    r = cursor.fetchall()
    for row in r:
        if row[1] == marketname:
            return True

    return False






if __name__ == "__main__":
    main()
