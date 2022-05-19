import ConnectionHandler


class DatasModule:

    def __init__(self):
        # open connection
        self.cur = ConnectionHandler.get_cursor(self)
        # --------Photovoltaic Installed (installed.csv)-------
        self.installed_power_LAND = ConnectionHandler.set_query('"Land"', "installed", self.cur)
        self.installed_power_ROOF = ConnectionHandler.set_query('"Roof"', "installed", self.cur)
        self.other_areas_LAND = ConnectionHandler.set_query('"Other Land"', "installed", self.cur)
        self.other_areas_ROOF = ConnectionHandler.set_query('"Other Roof"', "installed", self.cur)
        # --------Variables (variables.csv)--------------------
        self.built_surface = ConnectionHandler.set_query('"Built surface [km2]"', "variables", self.cur)
        self.domestic_consumption = ConnectionHandler.set_query('"Domestic consumption [GWh]"', "variables", self.cur)
        self.province_population = ConnectionHandler.set_query('"Population"', "variables", self.cur)
        self.taxable_income_per_capita = ConnectionHandler.set_query('"Taxable income per capita"', "variables",
                                                                     self.cur)
        self.arable_land_area = ConnectionHandler.set_query('"Arable land area [km2]"', "variables", self.cur)
        self.agricultural_added_value = ConnectionHandler.set_query('"Agricultural added value "', "variables",
                                                                    self.cur)
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
