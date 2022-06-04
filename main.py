import requests
from db import DB
from parser import HHParser

if __name__ == '__main__':
    db = DB()
    hh = HHParser()
    list_vac = hh.get_vacancies('python')
    for vac in list_vac:
        response = requests.get(url=vac['url'], timeout=10)
        vac_data = response.json()
        db.add_to_db(vac_data)
