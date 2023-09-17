from classes.abstract_clases.abstract_classes import ShowDataAbstract
from classes.functionality_classes.class_sort_filter import SortFilterHeadhunter


class ShowDataHeadhunter(SortFilterHeadhunter, ShowDataAbstract):
    """ Class is used to show searched vacancies and filtered vacancies"""
    @staticmethod
    def get_show(data_list):
        """ Static method is defining a message"""

        for vacancy in data_list:
            print(f'Vacancy id: {vacancy.vacancy_id}\n'
                  f'Vacancy name: {vacancy.vacancy_name}\n'
                  f'Employer name: {vacancy.employer_name}\n'
                  f'Salary from: {vacancy.salary_from}\n'
                  f'Salary to: {vacancy.salary_to}\n'
                  f'Salary currency: {vacancy.salary_currency}\n'
                  f'URL: {vacancy.url}\n'
                  f'City: {vacancy.city}\n')

        print(f'Total vacancies in chosen mode: {len(data_list)}')

    def get_show_filter(self, param):
        """ Return showed filtered vacancies"""

        filtered_vacancies: list = self.get_filtered(param)
        show_filtered_vacancies = self.get_show(filtered_vacancies)

        return show_filtered_vacancies

    def get_show_sorted(self, param, sort_mode):
        """ Return showed sorted vacancies"""

        sorted_vacancies: list = self.get_sorted(param, sort_mode)
        show_sorted_vacancies = self.get_show(sorted_vacancies)

        return show_sorted_vacancies

    def get_show_favorites(self):
        """ Return showed Favorites vacancies"""
        favorite_vacancies: list = self.vacancies_favorite
        show_sorted_vacancies = self.get_show(favorite_vacancies)

        return show_sorted_vacancies
