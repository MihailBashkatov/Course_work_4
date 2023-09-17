import json
import requests
from classes.abstract_clases.abstract_classes import AbstractSuperJobAPI
from secret_key import SECRET_KEY


class SuperJobAPI(AbstractSuperJobAPI):
    """ Class defines to get json file with searched vacancies in SupperJob"""
    def __init__(self, name):
        self.name = name

    def get_page_superjob(self, url_params=None, page=0):

        # Defining entering data
        headers = {'X-Api-App-Id': SECRET_KEY}
        url_params = {'page': page,
                      'count': 100,
                      'keyword': self.name}

        # pulling info from Superjob and transgform it in json format
        request = requests.get('https://api.superjob.ru/2.0/vacancies',
                               params=url_params,
                               headers=headers)

        data = request.content.decode()

        json_object = json.loads(data)

        return json_object
