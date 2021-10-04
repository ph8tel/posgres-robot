
import psycopg2
import time as t
import os
db_url = os.environ.get("DATABASE_URL")
db_host = os.environ.get("HOST")
db_name = os.environ.get("NAME")
db_pd = os.environ.get("PWD")
db_user = os.environ.get("USER")


def stopper():
    conn = psycopg2.connect(
        host = db_host,
        database = db_name,
        user = db_user,
        password = db_pd)
    with conn.cursor() as curs:
        curs.execute("INSERT INTO commands (command, pilot) VALUES ('stop', 'webpage')")
        conn.commit()

def send_cmd(cmd):
    conn = psycopg2.connect(
        host = db_host,
        database = db_name,
        user = db_user,
        password = db_pd)
    with conn.cursor() as curs:
        curs.execute("INSERT INTO commands (command, pilot) VALUES (%s, 'webpage')", (cmd,))
        conn.commit()
    return True

def just_sql( str):
    conn = psycopg2.connect(
        host = db_host,
        database = db_name,
        user = db_user,
        password = db_pd)
    with conn.cursor() as curs:
        curs.execute(str)
        conn.commit()

    return True
