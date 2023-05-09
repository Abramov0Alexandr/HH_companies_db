import requests
import csv


class VacanciesParser:
    """Класс для парсинга вакансий работодателя"""

    __vacancy_url = 'https://api.hh.ru/vacancies'

    def get_employers_vacancies(self, indexes: list) -> list[dict]:
        """
        Метод позволяет получить информацию о вакансиях компаний
        :param indexes: id компаний работодателя, полученные методом 'get_employers_id'
        :return: Списковый словарь, содержащий информацию о всех вакансиях выбранных компаний
        """

        params = {'employer_id': indexes,
                  'per_page': 100}
        response = requests.get(self.__vacancy_url, params=params).json()['items']
        return response

    def save_data_as_csv(self, filename: str, data: list[dict]) -> None:
        """
        Метод для сохранения итоговой информации о компаниях в формате csv
        :param filename: Необходимо передать названия файла, для сохранения информации
        :param data: Списковый словарь с информацией о вакансиях, полученной в результате парсинга
        """
        filename = f"{filename.capitalize().strip()}_vacancies.csv"

        with open(filename, mode='w', newline='') as csv_file:
            fieldnames = ['employer_id', 'vacancy_title',
                          'salary_from', 'salary_to', 'url']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            for item in data:

                if item['salary']:
                    salary_from = 0 if not item['salary']['from'] else item['salary']['from']
                    salary_to = 0 if not item['salary']['to'] else item['salary']['to']

                    writer.writerow(
                        {'employer_id': int(item['employer'].get('id')),
                         'vacancy_title': str(item.get('name')),
                         'salary_from': f"{float(salary_from)}",
                         'salary_to': f"{float(salary_to)}",
                         'url': str(item.get('alternate_url'))})
