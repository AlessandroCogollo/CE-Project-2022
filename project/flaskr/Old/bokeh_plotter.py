import json

import geopandas as gpd
import pandas.io.sql as psql
from bokeh.models import GeoJSONDataSource, LinearColorMapper
from bokeh.palettes import brewer
from bokeh.plotting import show, figure

from project.utils import ConnectionHandler


def plot():
    connection = ConnectionHandler.get_connection(ConnectionHandler)
    installed = psql.read_sql('SELECT * FROM installed', connection)
    shapefile = gpd.read_postgis('SELECT den_prov, cod_prov, geom FROM borders', connection)

    merged_df = shapefile.merge(installed, left_on='den_prov', right_on='Province')
    merged_json = json.loads(merged_df.to_json())
    json_data = json.dumps(merged_json)
    geo_source = GeoJSONDataSource(geojson=json_data)
    palette = brewer['OrRd'][8]
    color_mapper = LinearColorMapper(palette=palette)
    ghg_map = figure(title="Land Distribution per province", plot_height=720, plot_width=720)
    ghg_map.patches(source=geo_source, fill_color={'field': 'Land', 'transform': color_mapper})
    show(ghg_map)


def set_param(self, parameters):
    self.params = parameters
