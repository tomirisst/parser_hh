import json
import re
import requests


class HHParser:

    def get_vacancies(self, search_value):
        list_of_vac = []
        params = {
            'text': search_value,
            'area': 40,
            # 'page': counter
        }
        response = requests.get(url='https://api.hh.ru/vacancies', params=params)
        # print(len(response.json().get('items')))
        # print(json.dumps(response.json(), indent=3, ensure_ascii=False))
        for counter in range(response.json().get('pages')):
            params = {
                'text': search_value,
                'area': 40,
                'page': counter
            }
            response = requests.get(url='https://api.hh.ru/vacancies', params=params)
            for vac in response.json().get('items'):
                list_of_vac.append(vac)

        # print(json.dumps(list_of_vac[0], indent=3, ensure_ascii=False))
        # print (list_of_vac[0]['url'])
        return list_of_vac

    def cleanText(self, text):
        CLEANR = re.compile('<.*?>')
        cleantext = re.sub(CLEANR, '', text)
        return cleantext

    def get_skills_as_string(self, skills_array):
        skills = ''
        for skill in skills_array:
            skills += skill['name'] + '; '
        return skills

    def get_salary_as_string(self, vacancy):
        output = ""
        if 'salary' in vacancy and vacancy['salary']:
            salary = vacancy['salary']
            sal_from = ''
            sal_to = ''
            if salary.get('from'):
                sal_from = 'от ' + str(salary['from'])
            if salary.get('to'):
                sal_to = ' до ' + str(salary.get('to'))
            output = sal_from + sal_to + ' ' + salary.get('currency') if salary.get('currency') else ''
        return output
