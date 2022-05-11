import psycopg2


class DatasModule:
    @staticmethod
    def get_connection_cursor(self):
        self.connection = psycopg2.connect(dbname='envProjDB',
                                           user='alessandro',
                                           password='Aleric000*',
                                           host='localhost',
                                           port='5432')
        self.connection.autocommit = True  # Ensure data is added to the database immediately after write commands
        cursor = self.connection.cursor()
        cursor.execute('SELECT %s as connected;', ('Connection to postgres successful!',))
        print(cursor.fetchone())
        return cursor

    @staticmethod
    def close_connection(self):
        self.cur.close()
        self.connection.close()

    @staticmethod
    def set_query(arg, table, cur):
        cur.execute("""SELECT """ + table + """.""" + arg + """ FROM """ + table)
        array_query = cur.fetchall()
        return array_query

    def __init__(self):
        # open connection
        self.cur = DatasModule.get_connection_cursor(self)
        # --------Photovoltaic Installed (installed.csv)-------
        self.installed_power_LAND = DatasModule.set_query('"Land"', "installed", self.cur)
        self.installed_power_ROOF = DatasModule.set_query('"Roof"', "installed", self.cur)
        self.other_areas_LAND = DatasModule.set_query('"Other Land"', "installed", self.cur)
        self.other_areas_ROOF = DatasModule.set_query('"Other Roof"', "installed", self.cur)
        # --------Variables (variables.csv)--------------------
        self.built_surface = DatasModule.set_query('"Built surface [km2]"', "variables", self.cur)
        self.domestic_consumption = DatasModule.set_query('"Domestic consumption [GWh]"', "variables", self.cur)
        self.province_population = DatasModule.set_query('"Population"', "variables", self.cur)
        self.taxable_income_per_capita = DatasModule.set_query('"Taxable income per capita"', "variables", self.cur)
        self.arable_land_area = DatasModule.set_query('"Arable land area [km2]"', "variables", self.cur)
        self.agricultural_added_value = DatasModule.set_query('"Agricultural added value "', "variables", self.cur)
        # --Hourly Producibility (hourly_producibility..csv)---
        self.hourly_producibility = []
        provinces = self.set_query('"Province"', "hourly_producibility", self.cur)
        self.cur.execute("Select * FROM hourly_producibility LIMIT 0")
        colList = [desc[0] for desc in self.cur.description]
        for province in provinces:
            sum_producibility = 0
            for colName in colList:
                sum_producibility += self.cur.execute("""SELECT """ + colName + """ FROM hourly_producibility WHERE Province =""" + province)
            self.hourly_producibility.append(sum_producibility)
        # close connection
        DatasModule.close_connection(self)
