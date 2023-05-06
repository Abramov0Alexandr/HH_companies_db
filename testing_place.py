import json
import pprint
import requests


def create_employers_database(data_base_name: str, params: dict):
    pass


def save_data_to_db(data: list[dict], db_name: str, params: dict):
    pass


def parce_company(key_words: list | str):
    url = 'https://api.hh.ru/employers?only_with_vacancies=true'
    params = {'text': ' & '.join(key_words),
              'per_page': 10,
              'area': '113'}
    response = requests.get(url, params=params).json()['items']
    return response


def __write_to_json_file(self, data):
    """
    Метод для записи переданных в качестве аргумента данных в формат JSON.
    Метод служит для облегчения интерфейса класса
    :param data: Данные для записи
    """
    with open(self.__filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


# @property
# def __data_from_json_file(self):
# """
# Метод для получения данных из записанного JSON файла.
# Метод служит для облегчения интерфейса класса
# """
# with open(self.__filename, encoding='utf-8') as file:
#     vacancies = json.load(file)
#     return vacancies


pprint.pprint(parce_company('IT'))


#: Тестовая заготовка черновик!!
#: С данной функции можно будет брать данные для заполнения sql
def employers_sql_info(data: list):

    result = []

    for i in data:
        res_dict = {
            'company_id': i.get('id'),
            'company_title': i.get('name'),
            'vacancy_count': i.get('open_vacancies'),
            'url': i.get('alternate_url')}

        result.append(res_dict)

    return result
