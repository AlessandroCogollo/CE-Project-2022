import json

import pandas as pd
import geopandas as gpd
from bokeh.models import GeoJSONDataSource, LinearColorMapper
from bokeh.plotting import show, figure
from bokeh.palettes import brewer


def plot():
    df = pd.read_csv("../../docs/input/installed.csv")
    shapefile = "../map_borders/provinces/ProvCM01012022_g_WGS84.shp"
    gdf = gpd.read_file(shapefile)[['DEN_PROV', 'COD_PROV', 'geometry']]
    # TODO: refactor province mapping --
    gdf.loc[gdf.COD_PROV == 1, 'DEN_PROV'] = 'Torino'
    gdf.loc[gdf.COD_PROV == 10, 'DEN_PROV'] = 'Genova'
    gdf.loc[gdf.COD_PROV == 15, 'DEN_PROV'] = 'Milano'
    gdf.loc[gdf.COD_PROV == 27, 'DEN_PROV'] = 'Venezia'
    gdf.loc[gdf.COD_PROV == 37, 'DEN_PROV'] = 'Bologna'
    gdf.loc[gdf.COD_PROV == 48, 'DEN_PROV'] = 'Firenze'
    gdf.loc[gdf.COD_PROV == 58, 'DEN_PROV'] = 'Roma'
    gdf.loc[gdf.COD_PROV == 63, 'DEN_PROV'] = 'Napoli'
    gdf.loc[gdf.COD_PROV == 72, 'DEN_PROV'] = 'Bari'
    gdf.loc[gdf.COD_PROV == 80, 'DEN_PROV'] = 'Reggio Di Calabria'
    gdf.loc[gdf.COD_PROV == 82, 'DEN_PROV'] = 'Palermo'
    gdf.loc[gdf.COD_PROV == 83, 'DEN_PROV'] = 'Messina'
    gdf.loc[gdf.COD_PROV == 87, 'DEN_PROV'] = 'Catania'
    gdf.loc[gdf.COD_PROV == 92, 'DEN_PROV'] = 'Cagliari'
    # ---------------------------------
    gdf[['DEN_PROV', 'COD_PROV']].to_csv("provinces_shapefile.csv")
    merged_df = gdf.merge(df, left_on='DEN_PROV', right_on='Province')
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
