import requests
import csv


class EmployersParser:

    __employer_url = 'https://api.hh.ru/employers?only_with_vacancies=true'

    def get_employers_data(self, key_word: str) -> list[dict]:
        params = {'text': key_word.lower(),
                  'per_page': 10,
                  'area': '113'}
        response = requests.get(self.__employer_url, params=params).json()['items']
        return response

    def get_employers_id(self, data: list) -> list:
        id_list = []
        for i in data:
            id_list.append(i.get('id'))

        return id_list

    def save_as_csv(self, filename: str, data: list) -> None:
        filename = f"{filename.capitalize().strip()}_employers.csv"

        with open(filename, mode='w', newline='') as csv_file:
            fieldnames = ['employer_id', 'employer_title', 'vacancy_count', 'url']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            for item in data:
                writer.writerow({'employer_id': int(item.get('id')),
                                 'employer_title': str(item.get('name')),
                                 'vacancy_count': int(item.get('open_vacancies')),
                                 'url': str(item.get('alternate_url'))})
