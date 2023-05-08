import psycopg2
import pandas as pd
from pandas import DataFrame


class DataBaseManager:
    pd.set_option('display.max_columns', None)

    def __init__(self, data_base_name: str, connection_settings):
        self.__data_base_name = data_base_name
        self.__connection_settings = connection_settings

    def get_companies_and_vacancies_count(self) -> DataFrame:

        try:
            with psycopg2.connect(dbname=self.__data_base_name, **self.__connection_settings) as connection:

                sql_query = """SELECT employer_title, vacancy_count
                                FROM public.employers"""

                result = pd.read_sql(sql_query, connection)

            return result

        except Exception as e:
            print('[ERROR] Ошибка при выполнении запроса')
            print(e)

        finally:
            if connection:
                connection.close()

    def get_all_vacancies(self) -> DataFrame:

        try:
            with psycopg2.connect(dbname=self.__data_base_name, **self.__connection_settings) as connection:

                sql_query = """SELECT vacancy_title, employer_title, salary_from, salary_to, vacancies.url
                                FROM employers
                                JOIN public.vacancies USING(employer_id)"""

                result = pd.read_sql(sql_query, connection)

            return result

        except Exception as e:
            print('[ERROR] Ошибка при выполнении запроса')
            print(e)

        finally:
            if connection:
                connection.close()

    def get_avg_salary(self) -> DataFrame:

        try:
            with psycopg2.connect(dbname=self.__data_base_name, **self.__connection_settings) as connection:

                sql_query = """SELECT vacancy_title, AVG((salary_from + salary_to) / 2) AS avg_salary, url
                                FROM public.vacancies
                                GROUP BY vacancy_title, url
                                ORDER BY avg_salary DESC"""

                result = pd.read_sql(sql_query, connection)

            return result

        except Exception as e:
            print('[ERROR] Ошибка при выполнении запроса')
            print(e)

        finally:
            if connection:
                connection.close()

    def get_vacancies_with_higher_salary(self) -> DataFrame:

        try:
            with psycopg2.connect(dbname=self.__data_base_name, **self.__connection_settings) as connection:

                sql_query = """SELECT vacancy_title, salary_from, url
                                FROM vacancies
                                WHERE salary_from > (SELECT AVG((salary_from + salary_to) / 2) FROM vacancies)
                                ORDER BY salary_from DESC"""

                result = pd.read_sql(sql_query, connection)

            return result

        except Exception as e:
            print('[ERROR] Ошибка при выполнении запроса')
            print(e)

        finally:
            if connection:
                connection.close()

    def get_vacancies_with_keyword(self, keyword: str) -> DataFrame:

        try:
            with psycopg2.connect(dbname=self.__data_base_name, **self.__connection_settings) as connection:

                sql_query = f"""SELECT *
                            FROM vacancies
                            WHERE vacancy_title LIKE '%{keyword}%'"""

                result = pd.read_sql(sql_query, connection)

            return result

        except Exception as e:
            print('[ERROR] Ошибка при выполнении запроса')
            print(e)

        finally:
            if connection:
                connection.close()
