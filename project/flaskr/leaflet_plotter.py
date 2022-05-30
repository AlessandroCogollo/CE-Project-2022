import json

import folium
import geopandas as gpd
import pandas as pd
import pandas.io.sql as psql

from project.utils import ConnectionHandler
from project.utils.DatasModule import DatasModule


def plot():

    centre_coords = [42.3, 12]
    my_map = folium.Map(location=centre_coords, zoom_start=6)

    connection = ConnectionHandler.get_connection(ConnectionHandler)
    provinces = psql.read_sql('SELECT province FROM installed', connection)
    shapefile = gpd.read_postgis('SELECT cod_prov, den_uts, geom FROM borders', connection)

    # ----------------------------------------------------

    dm = DatasModule()
    dmodule = pd.DataFrame(data=dm.installed_power_LAND, columns=["land"])
    provinces.insert(1, 'land', dmodule)

    # ----------------------------------------------------

    # LAND
    folium.Choropleth(
        geo_data=shapefile,
        name="Land Consumption",
        data=provinces,
        columns=["province", "land"],
        key_on='feature.properties.den_uts',
        fill_color="YlGn",
        fill_opacity=0.8,
        line_opacity=0.5,
        legend_name="Land Consumption",
    ).add_to(my_map)

    folium.LayerControl().add_to(my_map)

    out = "templates/base_map.html"
    my_map.save(out)
