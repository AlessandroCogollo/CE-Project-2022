from enum import Enum


# TODO: optimize db queries

class Datas(Enum):
    # --------Photovoltaic Installed (installed.csv)-------
    installed_power_LAND = 0,
    installed_power_ROOF = 1,
    other_areas_LAND = 2,
    other_areas_ROOF = 3,
    # --------Variables (variables.csv)--------------------
    built_surface = 4,
    domestic_consumption = 5,
    province_population = 6,
    taxable_income_per_capita = 7,
    arable_land_area = 8,
    agricultural_added_value = 9,
    # --Hourly Producibility (hourly_producibility..csv)---
    hourly_producibility = 10
