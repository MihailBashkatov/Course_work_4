from classes.abstract_clases.abstract_classes import SortFilterAbstract
from classes.functionality_classes.class_get_vacancy import GetVacancy


class SortFilterHeadhunter(GetVacancy, SortFilterAbstract):
    """ Class is used to filter and sort vacancies upon user's choice"""

    def get_filtered(self, param: int):
        """ Return filtered data upon user's choice"""
        filtered_data = None

        if param == 1:
            filtered_data: list = self.vacancies_all

        if param == 2:
            filtered_data: list = list(filter(lambda x: self.name in x.employer_name.lower(), self.vacancies_all))

        elif param == 3:
            filtered_data: list = list(filter(lambda x: self.name in x.vacancy_name.lower(), self.vacancies_all))

        elif param == 4:
            filtered_data: list = list(filter(lambda x: self.name in x.vacancy_description.lower(), self.vacancies_all))

        elif param == 5:
            filtered_data: list = self.vacancies_favorite

        return filtered_data

    def get_sorted(self, param, sort_mode):
        """ Return sorted data upon user's choice"""

        sorted_data = None
        needed_data = self.get_filtered(param)

        if sort_mode == 1:
            sorted_data: list = list(sorted(needed_data, key=lambda x: x.vacancy_name.lower(), reverse=True))
        elif sort_mode == 2:
            sorted_data: list = list(sorted(needed_data, key=lambda x: x.vacancy_name.lower(), reverse=False))

        return sorted_data
