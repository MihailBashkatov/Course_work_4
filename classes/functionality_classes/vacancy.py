from classes.functionality_classes.class_save import Saver


class Vacancy(Saver):
    """ Class us used for comparison two vacancies around minimum salary level"""
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return self.vacancy_name

    def __eq__(self, other):
        return self.salary_from == other.salary_from

    def __le__(self, other):
        return self.salary_from <= other.salary_from

    def __ge__(self, other):
        return self.salary_from >= other.salary_from
