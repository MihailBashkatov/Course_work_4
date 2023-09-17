class InitializeVacancy:
    """ Class is making attributes initialization of searched vacancies
    and store all searched vacancies and favorite vacancies"""
    vacancies_all = []
    vacancies_favorite = []

    def __init__(self, name, vacancy_id=None, vacancy_name=None, employer_name=None, vacancy_description=None,
                 salary_from=None, salary_to=None, salary_currency=None, url=None, city=None):
        self.name = name
        self.vacancy_id = vacancy_id
        self.vacancy_name = vacancy_name
        self.employer_name = employer_name
        self.vacancy_description = vacancy_description
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.salary_currency = salary_currency
        self.url = url
        self.city = city
