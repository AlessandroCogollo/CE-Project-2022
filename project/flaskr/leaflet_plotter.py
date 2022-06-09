import folium
import geopandas as gpd
import pandas as pd
import pandas.io.sql as psql

from project.modules.Orchestrator import Orchestrator
from project.utils import ConnectionHandler


def plot(parameters1, parameters2=None):

    centre_coords = [42.3, 12]
    my_map = folium.Map(location=centre_coords, zoom_start=5)

    connection = ConnectionHandler.get_connection(ConnectionHandler)
    provinces = psql.read_sql('SELECT province FROM installed', connection)
    shapefile = gpd.read_postgis('SELECT cod_prov, den_uts, geom FROM borders', connection)

    # orchestrator = Orchestrator(parameters1)

    orchestrator1 = Orchestrator(parameters1)
    finalValues1 = clean_finalValues(orchestrator1)

    for i in finalValues1:
        dmodule = pd.DataFrame(data=getattr(orchestrator1.output_obj, i), columns=[i])
        datas =
        provinces.insert(1, i, dmodule)

        choroplethplot = folium.Choropleth(
            geo_data=shapefile,
            name=i,
            data=provinces,
            columns=["province", i],
            key_on='feature.properties.den_uts',
            fill_color="YlGn",
            fill_opacity=0.8,
            line_opacity=0.5,
        )

        for key in choroplethplot._children:
            if key.startswith('color_map'):
                del (choroplethplot._children[key])

        choroplethplot.add_to(my_map)

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
                                                   'Production Profiles',
                                                   'Additional PV Occupation Roof',
                                                   'Actual PV Occupation Roof'],
                                          labels=True,
                                          sticky=False
                                      )
                                      ).add_to(my_map)

    my_map.add_child(tooltip)
    my_map.keep_in_front(tooltip)

    # --------------- ADD LAYER CONTROL && SAVE MAP ------------------------

    folium.LayerControl().add_to(my_map)

    out = "templates/base_map.html"
    my_map.save(out)

    if parameters1 is not None:

        orchestrator2 = Orchestrator(parameters2)
        finalValues2 = clean_finalValues(orchestrator2)

        # return render_template('index.html', map=map._repr_html_())

        for i in finalValues2:
            dmodule2 = pd.DataFrame(data=getattr(orchestrator2.output_obj, i), columns=[i])
            provinces.insert(1, i, dmodule2)

            choroplethplot2 = folium.Choropleth(
                geo_data=shapefile,
                name=i,
                data=provinces,
                columns=["province", i],
                key_on='feature.properties.den_uts',
                fill_color="YlGn",
                fill_opacity=0.8,
                line_opacity=0.5,
            )

            for key in choroplethplot2._children:
                if key.startswith('color_map'):
                    del (choroplethplot2._children[key])

            choroplethplot2.add_to(my_map)

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
                                                       'Production Profiles',
                                                       'Additional PV Occupation Roof',
                                                       'Actual PV Occupation Roof'],
                                              labels=True,
                                              sticky=False
                                          )
                                          ).add_to(my_map)

        my_map.add_child(tooltip)
        my_map.keep_in_front(tooltip)

        # --------------- ADD LAYER CONTROL && SAVE MAP ------------------------

        folium.LayerControl().add_to(my_map)

        out = "templates/base_map1.html"
        my_map.save(out)


def clean_finalValues(orchestrator):
    # TODO: not best practice (get attributes)
    finalValues = [x for x in dir(orchestrator.output_obj) if not x.startswith('__')]
    finalValues = [x for x in finalValues if not x.startswith('get')]
    finalValues = [x for x in finalValues if not x.startswith('data_obj')]
    finalValues = [x for x in finalValues if not x.startswith('params')]

    return finalValues
