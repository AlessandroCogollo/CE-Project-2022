import json

import pandas as pd
import geopandas as gpd
from bokeh.models import GeoJSONDataSource, LinearColorMapper
from bokeh.plotting import show, figure
from bokeh.palettes import brewer

df = pd.read_csv("../../docs/input/installed.csv")
shapefile = "../map_borders/provinces/ProvCM01012022_g_WGS84.shp"
gdf = gpd.read_file(shapefile)[['DEN_PROV', 'COD_PROV', 'geometry']]
df.Province.to_csv("provinces_installed.csv")
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
