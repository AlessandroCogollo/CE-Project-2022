from project.utils import ConnectionHandler
import numpy as np


class DatasModule:

    def __init__(self):
        # open connection
        self.conn = ConnectionHandler.get_connection(self)
        self.cur = ConnectionHandler.get_cursor(self)
        # --------Photovoltaic Installed (installed.csv)-------
        self.installed_power_LAND = np.asarray(ConnectionHandler.set_query('"Land"', "installed", self.cur),
                                               dtype=float)
        self.installed_power_ROOF = np.asarray(ConnectionHandler.set_query('"Roof"', "installed", self.cur),
                                               dtype=float)
        self.other_areas_LAND = np.asarray(ConnectionHandler.set_query('"Other Land"', "installed", self.cur),
                                           dtype=float)
        self.other_areas_ROOF = np.asarray(ConnectionHandler.set_query('"Other Roof"', "installed", self.cur),
                                           dtype=float)
        # --------Variables (variables.csv)--------------------
        self.built_surface = np.asarray(ConnectionHandler.set_query('"Built surface [km2]"', "variables", self.cur),
                                        dtype=float)
        self.domestic_consumption = np.asarray(
            ConnectionHandler.set_query('"Domestic consumption [GWh]"', "variables", self.cur), dtype=float)
        self.province_population = np.asarray(ConnectionHandler.set_query('"Population"', "variables", self.cur),
                                              dtype=float)
        self.taxable_income_per_capita = np.asarray(
            ConnectionHandler.set_query('"Taxable income per capita"', "variables",
                                        self.cur), dtype=float)
        self.arable_land_area = np.asarray(
            ConnectionHandler.set_query('"Arable land area [km2]"', "variables", self.cur), dtype=float)
        self.agricultural_added_value = np.asarray(
            ConnectionHandler.set_query('"Agricultural added value "', "variables",
                                        self.cur), dtype=float)
        # --Hourly Producibility (hourly_producibility..csv)---
        self.hourly_producibility = []
        self.cur.execute("SELECT * FROM hourly_producibility LIMIT 0")
        provinces = [desc[0] for desc in self.cur.description]
        for province in provinces:
            if province != 'Province':
                province = "\"" + province + "\""
                self.cur.execute("""SELECT SUM(hourly_producibility.""" + province + """) FROM hourly_producibility""")
                query = self.cur.fetchall()
                self.hourly_producibility.append(query)
        print(self.hourly_producibility)
        # close connection
        ConnectionHandler.close_connection(self)
