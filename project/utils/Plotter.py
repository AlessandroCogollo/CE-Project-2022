import json

import pandas as pd
import geopandas as gpd
from bokeh.models import GeoJSONDataSource, LinearColorMapper
from bokeh.plotting import show, figure
from bokeh.palettes import brewer

df = pd.read_csv("../../docs/input/installed.csv")
shapefile = "../map_borders/limits_IT_provinces.geojson"
gdf = gpd.read_file(shapefile)[['prov_name', 'geometry']]
merged_df = gdf.merge(df, left_on='prov_name', right_on='Province')
merged_json = json.loads(merged_df.to_json())
json_data = json.dumps(merged_json)
geo_source = GeoJSONDataSource(geojson=json_data)
palette = brewer['OrRd'][8]
color_mapper = LinearColorMapper(palette=palette)
ghg_map = figure(title="Land Distribution per province", plot_height=720, plot_width=720)
ghg_map.patches(source=geo_source, fill_color={'field' : 'Land', 'transform' : color_mapper})
show(ghg_map)
