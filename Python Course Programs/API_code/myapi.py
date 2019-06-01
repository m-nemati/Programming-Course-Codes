import requests

def inform_me():
    print ('Hurry up to Buy Bitcoin')

def email_me():
    print ('Email me!')

myGoodPrice = 9000

#Call API
response = requests.get('https://api.coinbase.com/v2/prices/spot?currency=USD')

bitcoinPrice = response.json()['data']['amount']
bitcoinPrice = float(bitcoinPrice)
print ('BitCoin Prices now: %f $US' %bitcoinPrice)

if bitcoinPrice < myGoodPrice:
    inform_me()
    email_me()