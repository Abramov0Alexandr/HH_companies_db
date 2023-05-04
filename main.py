import pprint
import requests


def parce_company(key_words: list | str):
    url = 'https://api.hh.ru/employers?only_with_vacancies=true'
    params = {'text': ' & '.join(key_words),
              'per_page': 10,
              'area': '113'}
    response = requests.get(url, params=params).json()['items']
    return response


row_data = parce_company(['IT', 'разработка'])
print(row_data)
pprint.pprint(row_data)

