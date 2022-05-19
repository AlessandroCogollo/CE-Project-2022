import psycopg2


def get_connection(self):
    self.connection = psycopg2.connect(dbname='envProjDB',
                                       user='alessandro',
                                       password='Aleric000*',
                                       host='localhost',
                                       port='5432')
    self.connection.autocommit = True  # Ensure data is added to the database immediately after write commands
    return self.connection


def get_cursor(self):
    cursor = self.connection.cursor()
    cursor.execute('SELECT %s as connected;', ('Connection to postgres successful!',))
    print(cursor.fetchone())
    return cursor


def close_connection(self):
    self.cur.close()
    self.connection.close()


def set_query(arg, table, cur):
    cur.execute("""SELECT """ + table + """.""" + arg + """ FROM """ + table)
    array_query = cur.fetchall()
    return array_query
