import sys

import folium
import geopandas as gpd
import pandas.io.sql as psql
from numpy import size

from project.utils import ConnectionHandler, FinalValuesModule
from project.utils.DatasModule import DatasModule


def plot(params):

    print('This is standard output', file=sys.stdout)
    print("Lorem Ipsum")

    centre_coords = [42.3, 12]
    my_map = folium.Map(location=centre_coords, zoom_start=6)

    connection = ConnectionHandler.get_connection(ConnectionHandler)
    installed = psql.read_sql('SELECT * FROM installed', connection)
    shapefile = gpd.read_postgis('SELECT cod_prov, den_uts, geom FROM borders', connection)

    # ----------------------------------------------------

    data_obj = DatasModule()
    actual_pv_occupation_roof = FinalValuesModule.FinalValuesModule.get_actual_pv_occupation_roof(data_obj, params)

    # ----------------------------------------------------

    # LAND
    folium.Choropleth(
        geo_data=shapefile,
        name="Land Consumption",
        data=installed,
        columns=["Province", "Land"],
        key_on='feature.properties.den_uts',
        fill_color="YlGn",
        fill_opacity=0.8,
        line_opacity=0.5,
        legend_name="Land Consumption",
    ).add_to(my_map)

    folium.LayerControl().add_to(my_map)

    out = "templates/base_map.html"
    my_map.save(out)
