import json
import requests
from config import curency

class ConversionExeption(Exception):
    pass


class CurrensyConverter:
    def get_pryce(quote = str, base = str, amount = str):
        if quote == base:
            raise ConversionExeption('Укажите разные валюты')

        try:
            quote_ticker = curency[quote]
        except KeyError:
            raise ConversionExeption(f'Не удалось обрабовать валюту {quote}')

        try:
            base_ticker = curency[base]
        except KeyError:
            raise ConversionExeption(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConversionExeption(f'Введите верное число.')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}').content
        total_base = json.loads(r)[curency[base]]
        return total_base