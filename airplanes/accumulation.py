print('start accumulation')
from opensky_api import OpenSkyApi
import mysql.connector
import time
import datetime
import manage


delay = 300 # количество секунд, через которое обновляются данные базы
# from Main import user, password
while True:
    now = datetime.datetime.now()
    print(f'start while accum {now}')
    api = OpenSkyApi()

    # необходимо ввести user  и password
    cnx = mysql.connector.connect(user='', password='',
                                  host='127.0.0.1',
                                  database='opensky')

    cursor = cnx.cursor()

    '''Отбор и запись всех воздушных средств без дубликатов'''
    query = ('DELETE FROM vehicle')
    cursor.execute(query)
    query = ('ALTER TABLE vehicle AUTO_INCREMENT=0') # начинает отсчет нумерации ID в таблицс 0
    cursor.execute(query)
    # cnx.commit()

    states = api.get_states()
    for s in states.states:
        query = ("REPLACE INTO vehicle (icao24, callsign, origin_country, on_ground, longitude, latitude, velocity, category) "
                 "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")

        cursor.execute(query, (s.icao24, s.callsign, s.origin_country, s.on_ground, s.longitude, s.latitude, s.velocity, s.category))


    cnx.commit()


    cnx.close()
    time.sleep(delay)