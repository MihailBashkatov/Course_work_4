from abc import ABC


class AbstractSuperJobAPI(ABC):
    def get_page_superjob(self):
        pass


class AbstractHeadHunterAPI(ABC):
    def get_page_headhunter(self):
        pass


class ShowDataAbstract(ABC):
    def get_show_filter(self, param):
        pass

    def get_show_sorted(self, param, self_mode):
        pass

    def get_show_favorites(self):
        pass


class SortFilterAbstract(ABC):
    def get_sorted(self, param, sort_mode):
        pass

    def get_filtered(self, param):
        pass


class SaverAbstract(ABC):
    def save_favorite(self, param, sort_mode):
        pass
