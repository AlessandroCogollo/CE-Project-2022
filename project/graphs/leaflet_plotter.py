import folium
import folium.plugins
import geopandas as gpd
import pandas as pd
import pandas.io.sql as psql

import random
import string

from project.computational.Orchestrator import Orchestrator
from project.utils import ConnectionHandler


def plot(parameters1, parameters2=None):
    # init arrays to iterate on
    global choropleth_plot
    index = 0
    left = True
    parameters = [parameters1]
    if parameters2 is not None:
        parameters.append(parameters2)
    orchestrators = []
    finalValues = []

    # init coords and connection to retrieve values
    centre_coords = [42.3, 12]
    connection = ConnectionHandler.get_connection(ConnectionHandler)

    # interrogate db to array and shapefile
    shapefile = gpd.read_postgis('SELECT cod_prov, den_uts, geom FROM borders', connection)

    # instantiate orchestrator and get final values, based on number of input
    for parameter in parameters:
        orchestrators.append(Orchestrator(parameter))
        finalValues.append(clean_finalValues(orchestrators[parameters.index(parameter)]))

    # choose map type based on number of inputs
    if len(parameters) == 1:
        print("---- init single map ----")
        my_map = folium.Map(location=centre_coords, zoom_start=5)
    elif len(parameters) == 2:
        print("---- init dual map ----")
        my_map = folium.plugins.DualMap(location=centre_coords, zoom_start=5)

    for finalValue in finalValues:
        provinces = psql.read_sql('SELECT province FROM installed', connection)
        for i in finalValue:
            temp_orchestrator = orchestrators[index]
            datas_module = pd.DataFrame(data=getattr(temp_orchestrator.output_obj, i), columns=[i])
            provinces.insert(1, i, datas_module)

            choropleth_plot = folium.Choropleth(
                geo_data=shapefile,
                name=i,
                data=provinces,
                columns=["province", i],
                key_on='feature.properties.den_uts',
                fill_color="YlGn",
                fill_opacity=0.8,
                line_opacity=0.5,
            )

            for key in choropleth_plot._children:
                if key.startswith('color_map'):
                    del (choropleth_plot._children[key])

            if len(parameters) == 1:
                print("---- add choropleth_plot to my_map ----")
                choropleth_plot.add_to(my_map)
            elif len(parameters) == 2:
                print("---- add choropleth_plot to my_map ----")
                if index == 0:
                    choropleth_plot.add_to(my_map.m1)
                else:
                    choropleth_plot.add_to(my_map.m2)

        # counting index
        index = index + 1

        # ----------- ADD TOOLTIPS --------------

        outputValues = shapefile.merge(provinces, left_on='den_uts', right_on='province', how='left')

        highlight_function = lambda x: {'fillColor': '#000000',
                                        'color': '#000000',
                                        'fillOpacity': 0.50,
                                        'weight': 0.1}
        tooltip = folium.features.GeoJson(outputValues,
                                          name='Labels',
                                          style_function=lambda x: {'color': 'transparent', 'fillColor': 'transparent',
                                                                    'weight': 0},
                                          highlight_function=highlight_function,
                                          tooltip=folium.features.GeoJsonTooltip(
                                              fields=['den_uts',
                                                      'target_pv_occupied_surface_land',
                                                      'target_pv_occupation_roof',
                                                      'pv_power_target_roof',
                                                      'pv_power_target_land',
                                                      'pv_power_target',
                                                      'production_profiles',
                                                      'additional_pv_occupation_roof',
                                                      'actual_pv_occupation_roof'],
                                              aliases=['Province',
                                                       'Target PV Occupied Surface Land',
                                                       'Target PV Occupation Roof',
                                                       'PV Power Target Roof',
                                                       'PV Power Target Land',
                                                       'PV Power Target',
                                                       'Production Profiles ',
                                                       'Additional PV Occupation Roof',
                                                       'Actual PV Occupation Roof'],
                                              labels=True,
                                              sticky=False
                                          ))

        # --------------- ADD ELEMENTS TO MAP ------------------------

        if len(parameters) == 1:
            print("---- one map template ----")
            print("---- add child (tooltip) ----")
            my_map.add_child(tooltip)
            my_map.keep_in_front(tooltip)
        elif len(parameters) == 2:
            print("---- two map template ----")
            print("---- add child (tooltip) ----")
            if left == True:
                print("---- plotting left map ----")
                my_map.m1.add_child(tooltip)
                my_map.m1.keep_in_front(tooltip)
                left = False
            else:
                print("---- plotting right map ----")
                my_map.m2.add_child(tooltip)
                my_map.m2.keep_in_front(tooltip)

    folium.LayerControl().add_to(my_map)

    print("---- saving output ----")
    token = get_random_token()
    print("---- token: " + token + " ----")
    out = "templates/plots/" + token + ".html"
    my_map.save(out)
    return token


def clean_finalValues(orchestrator):
    finalValues = [x for x in dir(orchestrator.output_obj) if not x.startswith('__')]
    finalValues = [x for x in finalValues if not x.startswith('get')]
    finalValues = [x for x in finalValues if not x.startswith('data_obj')]
    finalValues = [x for x in finalValues if not x.startswith('params')]

    return finalValues


def get_random_token():
    length = 6
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
