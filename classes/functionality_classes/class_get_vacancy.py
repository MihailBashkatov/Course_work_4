from classes.functionality_classes.class_initialize_vacancy import InitializeVacancy
from classes.headhunter.class_headhunter_api import HeadHunterAPI
from classes.superjob.class_superjob_api import SuperJobAPI


class GetVacancy(HeadHunterAPI, SuperJobAPI, InitializeVacancy):
    """Class is defined to get json file with vacancies, reformat it to object of class InitializeVacancy """
    def __init__(self, name):
        super().__init__(name)

    def initialize_vacancies_headhunter(self):

        # if list with all vacancies does have more, then one vacancy, the list becomes empty
        if len(self.vacancies_all) > 0:

            # list with all vacancies is stored in class InitializeVacancy
            self.vacancies_all: list = []

        # There is a set for 10 pages in Headhunter
        for page in range(0, 10):

            # Json list is created by function from HeadHunterAPI
            json_list: dict = self.get_page_headhunter(page)
            for data in json_list['items']:

                # If no key 'salary', key 'salary' is defining
                if not data.get('salary'):
                    data['salary'] = {'from': None, 'to': None, 'currency': None}

                # If values 'from', 'to', 'currency' are None
                if (data['salary'].get('from') is None or data['salary'].get('to') is None
                                                       or data['salary'].get('currency') is None):
                    data['salary']['from'] = 'No info available'
                    data['salary']['to'] = 'No info available'
                    data['salary']['currency'] = 'No info available'

                # If value 'requirements' is Nona
                if data['snippet'].get('requirements') is None:
                    data['snippet']['requirement'] = 'No info available'

                # Unifying json_list parameters to attributes of class InitializeVacancy
                vacancy_id: int = int(data['id'])
                vacancy_name: str = data['name']
                employer_name: str = data['employer']['name']
                vacancy_description: str = data['snippet']['requirement']
                salary_from: str = data['salary']['from']
                salary_to: str = data['salary']['to']
                salary_currency: str = data['salary']['currency']
                url: str = data['url']
                city: str = data['area']['name']
                self.vacancies_all.append(InitializeVacancy(self.name,
                                                            vacancy_id,
                                                            vacancy_name,
                                                            employer_name,
                                                            vacancy_description,
                                                            salary_to,
                                                            salary_from,
                                                            salary_currency,
                                                            url,
                                                            city))

    def initialize_vacancies_superjob(self):
        # if list with all vacancies does have more, then one vacancy, the list becomes empty
        if len(self.vacancies_all) > 0:

            # list with all vacancies is stored in class InitializeVacancy
            self.vacancies_all = []

        # There is a set for 5 pages in Superjob
        for page in range(0, 5):

            # Json list is created by function from SuperJobAPI
            json_list = self.get_page_superjob(page)
            for data in json_list['objects']:

                # If values 'payment_from', 'payment_to' == 0
                if data['payment_from'] == 0:
                    data['payment_from'] = 'No info available'
                if data['payment_to'] == 0:
                    data['payment_to'] = 'No info available'

                # Unifying json_list parameters to attributes of class InitializeVacancy
                vacancy_id: int = int(data['id'])
                vacancy_name: str = data['profession']
                employer_name: str = data['firm_name']
                vacancy_description: str = data['candidat']
                salary_from: str = data['payment_from']
                salary_to: str = data['payment_to']
                salary_currency: str = data['currency']
                url: str = data['link']
                city: str = data['town']['title']
                self.vacancies_all.append(InitializeVacancy(self.name,
                                                            vacancy_id,
                                                            vacancy_name,
                                                            employer_name,
                                                            vacancy_description,
                                                            salary_to,
                                                            salary_from,
                                                            salary_currency,
                                                            url,
                                                            city))
