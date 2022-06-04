import sqlite3
from parser.hh_parser import HHParser

class DB:

    def __init__(self):
        self.connection = sqlite3.connect(database='hh_vacancies.db')
        self.cursor = self.connection.cursor()
        self.prepare()

    def prepare(self):
        # Creating vacancy table
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS vacancies(
           vacancy_id INT PRIMARY KEY,
           vacancy_url TEXT,
           name TEXT,
           description TEXT,
           skills TEXT,
           salary TEXT,
           experience TEXT,
           region TEXT,
           schedule TEXT,
           employer TEXT,
           employer_url TEXT,
           professional_role TEXT,
           published_at TEXT
           );""")
        self.connection.commit()

    def get_all(self):
        sql = 'SELECT * FROM vacancies'
        cur = self.cursor.execute(sql).fetchall()
        return cur

    def add_to_db(self, vacancy):
        hh = HHParser()
        # Writing data to db
        vacancy_data = (vacancy['id'], vacancy['alternate_url'], vacancy['name'], hh.cleanText(vacancy['description']),
                        hh.get_skills_as_string(vacancy['key_skills']), hh.get_salary_as_string(vacancy),
                        vacancy['experience']['name'], vacancy['area']['name'],
                        vacancy['schedule']['name'], vacancy['employer']['name'],
                        vacancy['employer']['alternate_url'], vacancy['professional_roles'][0]['name'],
                        vacancy['published_at'])
        self.cursor.execute("INSERT INTO vacancies VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", vacancy_data)
        self.connection.commit()
