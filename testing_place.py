import pprint
import requests


def create_database(data_base_name: str, params: dict):
    pass


def save_data_to_db(data: list[dict], db_name: str, params: dict):
    pass


def parce_company(key_word: str):
    url = 'https://api.hh.ru/employers?only_with_vacancies=true'
    params = {'text': key_word,
              'per_page': 10,
              'area': '113'}
    response = requests.get(url, params=params).json()['items']
    return response


pprint.pprint(parce_company('IT'))
