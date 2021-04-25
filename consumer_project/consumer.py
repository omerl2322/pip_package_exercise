import time
from datetime import datetime

import schedule
from tinydb import TinyDB
from universities_api import get_universities


def export_universities_data():
    url = 'http://universities.hipolabs.com/search?country=Israel'
    universities_data = get_universities(url)
    return universities_data


def store_data_on_db(data, db):
    time_stamp = datetime.now()
    timestamp = time_stamp.replace(microsecond=0)
    for item in data:
        university_name = item['name']
        university_domain = item['domains'][0]
        web_page = item['web_pages'][0]
        alpha_code = item['alpha_two_code']
        db.insert({'datetime': str(timestamp),
                   'university_name': university_name,
                   'university_domain': university_domain,
                   'web_page': web_page,
                   'alpha_code': alpha_code})


def main_process():
    print('starting the main process')
    db = TinyDB('db.json')
    # get data from api
    universities_data = export_universities_data()
    # store the data on db
    store_data_on_db(universities_data, db)
    print('the main process finished')


# schedule the main process - once a day
schedule.every().day.at('10:30').do(main_process)
while True:
    schedule.run_pending()
    time.sleep(1)
