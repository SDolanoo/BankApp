import requests

JSON_FORMAT = "?format=json"
MAIN_REQUEST = "http://api.nbp.pl/api/exchangerates/rates/c"


class NBPapi:

    def __init__(self):
        pass

    def get_whole_table_of_main_currencies(self) -> dict:
        response = requests.get(url="https://api.nbp.pl/api/exchangerates/tables/c?format=json")
        response.raise_for_status()
        return response.json()[0]

    def ask_for_one_currency(self, curr_code: str) -> dict:
        response = requests.get(url=f"{MAIN_REQUEST}{curr_code}{JSON_FORMAT}")
        response.raise_for_status()
        return response.json()[0]
