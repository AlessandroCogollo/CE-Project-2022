import array

from project.utils import ConnectionHandler
import numpy as np
import pandas as pd


class DatasModule:

    def __init__(self):
        # open connection
        self.conn = ConnectionHandler.get_connection(self)
        self.cur = ConnectionHandler.get_cursor(self)

        # --------Photovoltaic Installed (installed.csv)-------
        self.installed_power_LAND = [item for sublist in
                                     np.array(ConnectionHandler.set_query('land', "installed", self.cur),
                                              dtype=float) for item in sublist]
        self.installed_power_ROOF = [item for sublist in
                                     np.array(ConnectionHandler.set_query('roof', "installed", self.cur),
                                              dtype=float) for item in sublist]
        self.other_areas_LAND = [item for sublist in
                                 np.array(ConnectionHandler.set_query('otherland', "installed", self.cur),
                                          dtype=float) for item in sublist]
        self.other_areas_ROOF = [item for sublist in
                                 np.array(ConnectionHandler.set_query('otherroof', "installed", self.cur),
                                          dtype=float) for item in sublist]

        # --------Variables (variables.csv)--------------------
        self.built_surface = [item for sublist in
                              np.array(ConnectionHandler.set_query('"Built surface [km2]"', "variables", self.cur),
                                       dtype=float) for item in sublist]
        self.domestic_consumption = [item for sublist in np.array(
            ConnectionHandler.set_query('"Domestic consumption [GWh]"', "variables", self.cur), dtype=float)
                                     for item in sublist]
        self.province_population = [item for sublist in
                                    np.array(ConnectionHandler.set_query('"Population"', "variables", self.cur),
                                             dtype=float)
                                    for item in sublist]
        self.taxable_income_per_capita = [item for sublist in np.array(
            ConnectionHandler.set_query('"Taxable income per capita"', "variables",
                                        self.cur), dtype=float)
                                          for item in sublist]
        self.arable_land_area = [item for sublist in np.array(
            ConnectionHandler.set_query('"Arable land area [km2]"', "variables", self.cur), dtype=float)
                                 for item in sublist]
        self.agricultural_added_value = [item for sublist in np.array(
            ConnectionHandler.set_query('"Agricultural added value "', "variables",
                                        self.cur), dtype=float) for item in sublist]

        # --Hourly Producibility (hourly_producibility..csv)---
        hourly_producibility = []
        df = pd.read_sql('SELECT * FROM hourly_producibility', self.conn)
        for col in df:
            if col != 'Province':
                hourly_producibility.append(df[col].sum())

        self.hourly_producibility = hourly_producibility

        # close connection
        ConnectionHandler.close_connection(self)
