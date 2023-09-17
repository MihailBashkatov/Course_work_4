import json

import requests

from classes.abstract_clases.abstract_classes import AbstractHeadHunterAPI


class HeadHunterAPI(AbstractHeadHunterAPI):
    """ Class defines to get json file with searched vacancies in HeadHunter"""
    def __init__(self, name):
        self.name = name

    def get_page_headhunter(self, page=0):

        # Defining entering data
        param = {'text': self.name,
                 'area': 1,
                 'page': page,
                 'per_page': 100}

        # pulling info from Headhunter and transform it in json format
        request = requests.get('https://api.hh.ru/vacancies', param)

        data = request.content.decode()

        json_object = json.loads(data)

        return json_object
