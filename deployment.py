from getpass import getpass
from subprocess import Popen, PIPE, STDOUT
import webbrowser
import time
import os

SQL_SCRIPT = r'openSky.sql'

if input('Full deployment? [y/n]') == 'y':
    with open('test.log','wb') as out, open('test-error.log','wb') as err:
        p = Popen([r'python', '-m', 'venv', 'venv'], stdout=out, stderr=err)
    with open('test.log','wb') as out, open('test-error.log','wb') as err:
        p = Popen([r'.\venv\Scripts\python', '-m', 'pip', 'install', '-r', 'requirements.txt'], stdout=out, stderr=err)


    from mysql.connector import connect
    from mysql.connector import DatabaseError
    
    host = input('Enter the IP address or DNS name of your MySQL instance: ')
    user = input('Enter the username of your MySQL instance: ')
    password = getpass(f'Enter the password for user {user} on your MySQL instance: ')
    db_name = input(f'Enter the name of the database to be created on your MySQL instance: ')
    with connect(
        host=host,
        user=user,
        password=password,
    ) as connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute(f'CREATE DATABASE {db_name}')
            except DatabaseError as err:
                if err.msg == f"Can't create database '{db_name}'; database exists":
                    if input(f'Database {db_name} already exists. Do you want to drop it [y/n]? ') == 'y':
                        cursor.execute(f'DROP DATABASE {db_name}')
                        cursor.execute(f'CREATE DATABASE {db_name}')
            file = open(SQL_SCRIPT, encoding='UTF-8')
            sql = file.read()
            sql = sql.replace('DELIMITER ;;\n', '').replace('DELIMITER ;\n', '').replace('END ;;\n','END\n')
            sql = sql.split('\n\n')
            sql = [f'USE {db_name};\n\nSET FOREIGN_KEY_CHECKS=0;\n\n'] + sql + ['SET FOREIGN_KEY_CHECKS=1;\n\n']
            for statement in sql:
                print('-' * 40)
                print(statement)
                if statement.strip() == '':
                    continue
                for result in cursor.execute(statement, multi=True):
                    if result.with_rows:
                        print("Rows produced by statement '{}':".format(
                            result.statement))
                        print(result.fetchall())
                    else:
                        print("Number of rows affected by statement '{}': {}".format(
                            result.statement, result.rowcount))
    with open('.\OpenSky\settings.py', 'r+') as inp:
        for line in inp:
            line = line.replace("'USER': 'Sergei'", f"'USER': '{user}'") \
                .replace("'PASSWORD': ''", f"'PASSWORD': '{password}'") \
                .replace("'HOST': 'localhost'",
                         f"'HOST': '{host}'") \
                .replace("'NAME': 'opensky'", f"'NAME': '{db_name}'")
            inp.write(line)
    #Внесение изменений в .\airplanes\accumulation.py
    with open(r'.\airplanes\accumulation.py', 'r+') as inp:
        for line in inp:
            line = line.replace("user=''", f"user='{user}'") \
                .replace("password=''", f"password='{password}'") \
                .replace("host='localhost'",
                         f"host='{host}'") \
                .replace("database=''", f"database='{db_name}'")
            inp.write(line)

    with open('.\OpenSky\settings.py', 'r') as inp, open('.\OpenSky\settings2.py', 'w') as outp:
        for line in inp:
            line = line.replace("'USER': 'Sergei'", f"'USER': '{user}'") \
                .replace("'PASSWORD': ''", f"'PASSWORD': '{password}'") \
                .replace("'HOST': 'localhost'",
                         f"'HOST': '{host}'") \
                .replace("'NAME': 'opensky'", f"'NAME': '{db_name}'")
            outp.write(line)
    # Внесение изменений в .\airplanes\accumulation.py
    with open(r'.\airplanes\accumulation.py', 'r') as inp, open(r'.\airplanes\accumulation2.py', 'w') as outp:
        for line in inp:
            line = line.replace("user=''", f"user='{user}'") \
                .replace("password=''", f"password='{password}'") \
                .replace("host='localhost'",
                         f"host='{host}'") \
                .replace("database=''", f"database='{db_name}'")
            outp.write(line)

    os.remove(r'.\airplanes\accumulation.py')
    os.rename(r'.\airplanes\accumulation2.py', r'.\airplanes\accumulation.py')
    os.remove('.\OpenSky\settings.py')
    os.rename('.\OpenSky\settings2.py', '.\OpenSky\settings.py')

with open('test.log', 'wb') as out, open('test-error.log', 'wb') as err:
    os.system("manage.py runserver --noreload")


