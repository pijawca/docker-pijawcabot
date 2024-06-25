import requests
from config import API_KEY_MARKETCAP as api_key


def ton_status():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

    parameters = {
        'symbol': 'TON',
        'convert': 'USD'
    }

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
    }

    response = requests.get(url, headers=headers, params=parameters)
    data = response.json()

    if 'data' in data and 'TON' in data['data']:
        ton_data = data['data']['TON']
        priceUsd = (f"{ton_data['quote']['USD']['price']}")[:4]
        percentChange24h = f"{ton_data['quote']['USD']['percent_change_24h']:.2f}"
        percentChange1h = f"{ton_data['quote']['USD']['percent_change_1h']:.2f}"
        percentChange7d = f"{ton_data['quote']['USD']['percent_change_7d']:.2f}"
        volume = f"{ton_data['quote']['USD']['volume_24h']:.2f}"
        
    else:
        priceUsd = None
        percentChange24h = None
    
    parameters = {
        'symbol': 'TON',
        'convert': 'RUB'
    }
    
    response = requests.get(url, headers=headers, params=parameters)
    data = response.json()

    if 'data' in data and 'TON' in data['data']:
        ton_data = data['data']['TON']
        pricerub = (f"{ton_data['quote']['RUB']['price']}")[:6]
    else:
        pricerub = None
        
    return priceUsd, percentChange24h, pricerub, percentChange1h, percentChange7d, volume

def news():
    pass