from bs4 import BeautifulSoup
import urllib3
import urllib.parse
import urllib.request
import json
import sys, locale
import certifi


http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())


def poloniex_market():
    url = "https://poloniex.com/public?command=returnTicker"
    r = http.request('GET', url)
    myData = json.loads(r.data.decode('utf-8'))
    print(myData['USDT_BTC']['last'])


def okcoin_market():
    url = "https://www.okcoin.com/api/v1/ticker.do?symbol=btc_usd"
    r = http.request('GET', url)
    myData = json.loads(r.data.decode('utf-8'))
    print(myData['ticker']['last'])


def mercadobitcoin_market():
    url = "https://www.mercadobitcoin.net/api/BTC/ticker/"
    r = http.request('GET', url)
    myData = json.loads(r.data.decode('utf-8'))
    print(myData['ticker']['last'])


def bitcambio_market():
    url = "https://bitcambio_api.blinktrade.com/api/v1/BRL/ticker"
    r = http.request('GET', url)
    myData = json.loads(r.data.decode('utf-8'))
    print(myData['last'])


def braziliex_market():
    url = "https://braziliex.com/api/v1/public/ticker"
    r = http.request('GET', url)
    myData = json.loads(r.data.decode('utf-8'))
    print(myData['btc_brl']['last'])


def quadrigacx_market():
    url = "https://api.quadrigacx.com/v2/ticker?book=btc_usd"
    r = http.request('GET', url)
    myData = json.loads(r.data.decode('utf-8'))
    print(myData['last'])


def blockchainluxemburgo_market():
    url = "https://blockchain.info/q/24hrprice"
    r = http.request('GET', url)
    myData = json.loads(r.data.decode('utf-8'))
    print(myData)




poloniex_market()
okcoin_market()
mercadobitcoin_market()
bitcambio_market()
braziliex_market()
quadrigacx_market()
blockchainluxemburgo_market()















