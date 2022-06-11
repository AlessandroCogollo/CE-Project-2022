import psycopg2
from os import environ
from sqlalchemy import create_engine, select


def get_connection(self):
    #db_uri = environ.get('postgres+psycopg2://alessandro:Aleric000*@localhost:5432/envProjDB')
    self.engine = create_engine("postgresql+psycopg2://alessandro:Aleric000*@localhost:5432/envProjDB", echo=False)
    return self.engine


def get_cursor(self):
    self.connection = self.engine.connect()

    return self.connection


def close_connection(self):
    self.connection.close()


def set_query(arg, table, cur):
    tobefetched = cur.execute("""SELECT """ + table + """.""" + arg + """ FROM """ + table)
    array_query = tobefetched.fetchall()
    return array_query
