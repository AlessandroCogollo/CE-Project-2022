import json

import folium
import geopandas as gpd
import pandas.io.sql as psql

from project.utils import ConnectionHandler

centre_coords = [42.3, 12]
my_map = folium.Map(location=centre_coords, zoom_start=6)

# ---------------

connection = ConnectionHandler.get_connection(ConnectionHandler)
installed = psql.read_sql('SELECT * FROM installed', connection)
shapefile = gpd.read_postgis('SELECT den_prov, cod_prov, geom FROM borders', connection)

merged_df = shapefile.merge(installed, left_on='den_prov', right_on='Province')

# merged_df.to_csv('merged.csv')
# merged_df = merged_df.set_index('den_prov')['Land']
json_to_load = merged_df.to_json()
merged_json = json.loads(json_to_load)
# geo_source = json.dumps(merged_json)

# TODO: refer to key_on
key = []
for i in range(10):
    key.append(float(merged_json["features"][i]["properties"]["Land"]))
print(key)

folium.Choropleth(
    geo_data=shapefile,
    name="Land",
    data=merged_df,
    columns=["den_prov", "Land"],
    key_on=key,
    fill_color="BuPu",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Land Consumption",
).add_to(my_map)

# folium.LayerControl().add_to(my_map)

# ---------------
outfp = "templates/base_map.html"
my_map.save(outfp)
