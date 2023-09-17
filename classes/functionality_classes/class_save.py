from classes.abstract_clases.abstract_classes import SaverAbstract
from classes.functionality_classes.class_show_data import ShowDataHeadhunter


class Saver(ShowDataHeadhunter, SaverAbstract):
    """ Class is used to save filtered vacancies to Favorites"""
    def save_favorite(self, param, sort_mode):
        self.vacancies_favorite.extend(self.get_sorted(param, sort_mode))
