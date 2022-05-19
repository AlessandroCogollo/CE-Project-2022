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

    # TODO: refactor province mapping --
    shapefile.loc[shapefile.cod_prov == 1, 'den_prov'] = 'Torino'
    shapefile.loc[shapefile.cod_prov == 10, 'den_prov'] = 'Genova'
    shapefile.loc[shapefile.cod_prov == 15, 'den_prov'] = 'Milano'
    shapefile.loc[shapefile.cod_prov == 27, 'den_prov'] = 'Venezia'
    shapefile.loc[shapefile.cod_prov == 37, 'den_prov'] = 'Bologna'
    shapefile.loc[shapefile.cod_prov == 48, 'den_prov'] = 'Firenze'
    shapefile.loc[shapefile.cod_prov == 58, 'den_prov'] = 'Roma'
    shapefile.loc[shapefile.cod_prov == 63, 'den_prov'] = 'Napoli'
    shapefile.loc[shapefile.cod_prov == 72, 'den_prov'] = 'Bari'
    shapefile.loc[shapefile.cod_prov == 80, 'den_prov'] = 'Reggio di Calabria'
    shapefile.loc[shapefile.cod_prov == 82, 'den_prov'] = 'Palermo'
    shapefile.loc[shapefile.cod_prov == 83, 'den_prov'] = 'Messina'
    shapefile.loc[shapefile.cod_prov == 87, 'den_prov'] = 'Catania'
    shapefile.loc[shapefile.cod_prov == 92, 'den_prov'] = 'Cagliari'
    # ---------------------------------

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
