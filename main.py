import pprint
import requests
import csv


class CompanyParser:

    __employer_url = 'https://api.hh.ru/employers?only_with_vacancies=true'

    def get_employers(self, key_word: str) -> list[dict]:
        params = {'text': key_word.lower(),
                  'per_page': 10,
                  'area': '113'}
        response = requests.get(self.__employer_url, params=params).json()['items']
        return response

    def get_employers_id(self, data):
        id_list = []
        for i in data:
            id_list.append(i.get('id'))

        return id_list

    def save_as_csv(self, filename: str, data: list) -> None:
        filename = f"{filename.title().strip()}.csv"

        with open(filename, mode='w', newline='', encoding='utf-16') as csv_file:
            fieldnames = ['company_id', 'company_title', 'vacancy_count', 'url']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            for item in data:
                writer.writerow({'company_id': item.get('id'),
                                 'company_title': item.get('name'),
                                 'vacancy_count': item.get('open_vacancies'),
                                 'url': item.get('alternate_url')})


class VacancyParser:

    __vacancy_url = 'https://api.hh.ru/vacancies'

    def get_employers_vacancies(self, indexes: list):

        params = {'employer_id': indexes,
                  'per_page': 100}
        response = requests.get(self.__vacancy_url, params=params).json()['items']
        return response

    def save_as_csv(self, filename: str, data: list) -> None:
        filename = f"{filename.title().strip()}.csv"

        with open(filename, mode='w', newline='', encoding='utf-16') as csv_file:
            fieldnames = ['company_id', 'vacancy_title',
                          'salary_from', 'salary_to', 'url']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            for item in data:

                if item['salary']:
                    salary_from = 0 if not item['salary']['from'] else item['salary']['from']
                    salary_to = 0 if not item['salary']['to'] else item['salary']['to']

                    writer.writerow(
                        {'company_id': item['employer'].get('id'),
                         'vacancy_title': item.get('name'),
                         'salary_from': f"{salary_from}",
                         'salary_to': f"{salary_to}",
                         'url': item.get('alternate_url')})


cp = CompanyParser()
vp = VacancyParser()


employers = cp.get_employers('it')
indexes = cp.get_employers_id(employers)
vac = vp.get_employers_vacancies(indexes)

# vp.save_as_csv('test_vac', vac)

print()


