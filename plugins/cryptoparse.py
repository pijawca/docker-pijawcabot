import requests
from config import API_KEY_MARKETCAP as api_key


def get_ton_data(symbol, convert):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {
        'symbol': symbol,
        'convert': convert
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
    }
    response = requests.get(url, headers=headers, params=parameters)
    return response.json()


def ton_status():
    data = get_ton_data('TON', 'USD')
    if 'data' in data and 'TON' in data['data']:
        ton_data = data['data']['TON']
        price_usd = f"{ton_data['quote']['USD']['price']:.2f}"
        percent_change_24h = f"{ton_data['quote']['USD']['percent_change_24h']:.2f}"
        percent_change_1h = f"{ton_data['quote']['USD']['percent_change_1h']:.2f}"
        percent_change_7d = f"{ton_data['quote']['USD']['percent_change_7d']:.2f}"
        volume = f"{ton_data['quote']['USD']['volume_24h']:.2f}"
    else:
        price_usd = None
        percent_change_24h = None
        percent_change_1h = None
        percent_change_7d = None
        volume = None

    data = get_ton_data('TON', 'RUB')
    if 'data' in data and 'TON' in data['data']:
        ton_data = data['data']['TON']
        price_rub = f"{ton_data['quote']['RUB']['price']:.2f}"
    else:
        price_rub = None

    return price_usd, percent_change_24h, price_rub, percent_change_1h, percent_change_7d, volume
