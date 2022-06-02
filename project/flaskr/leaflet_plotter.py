import folium
import geopandas as gpd
import pandas as pd
import pandas.io.sql as psql
import project.utils.ArithmeticModule as am

from project.modules.Old.FirstModule import FirstModule
from project.utils import ConnectionHandler
from project.utils.DatasModule import DatasModule


def plot(parameters):
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
    addLand = folium.Choropleth(
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

    # ----------------------------------------------------

    dmodule = pd.DataFrame(data=dm.installed_power_ROOF, columns=["roof"])
    provinces.insert(1, 'roof', dmodule)

    # ----------------------------------------------------

    # ROOF
    addRoof = folium.Choropleth(
        geo_data=shapefile,
        name="Roof Consumption",
        data=provinces,
        columns=["province", "roof"],
        key_on='feature.properties.den_uts',
        fill_color="YlOrRd",
        fill_opacity=0.8,
        line_opacity=0.5,
        legend_name="Roof Consumption",
    ).add_to(my_map)

    # -----------------------------------------------------

    dmodule = pd.DataFrame(data=FirstModule().get_base_distribution(DatasModule(), parameters, 0),
                           columns=["base_distribution_roof"])
    provinces.insert(1, 'base_distribution_roof', dmodule)

    # base_distribution_roof
    addBaseDistributionRoof = folium.Choropleth(
        geo_data=shapefile,
        name="Base Distribution Roof",
        data=provinces,
        columns=["province", "base_distribution_roof"],
        key_on='feature.properties.den_uts',
        fill_color="BuPu",
        fill_opacity=0.8,
        line_opacity=0.5,
        legend_name="Base Distribution Roof",
    ).add_to(my_map)

    print(am.sum_array(DatasModule().built_surface))
    provinces.to_csv("provinces.csv")

    folium.LayerControl().add_to(my_map)

    out = "templates/base_map.html"
    my_map.save(out)
