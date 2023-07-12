import requests
import json
from config import keys


class ConvertionException(Exception):
    pass


class Convertor:
    @staticmethod
    def convert(quote: str, base: str, amount: str):

        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}')


        quote_ticker, base_tiker = keys[quote], keys[base]
        r = requests.get(
            f"https://v6.exchangerate-api.com/v6/2aea2fd4c35557cbecfb18ca/pair/{quote_ticker}/{base_tiker}/{amount}")
        total_base = json.loads(r.content)

        return total_base