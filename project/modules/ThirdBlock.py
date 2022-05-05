from ..utils import DatasModule as dm
from ..modules import FirstBlock as fb
from ..modules import SecondBlock as sb


# block 5
class ThirdModule:
    @staticmethod
    def get_additional_power_distribution(typology, weight_equivalent_hours_pv, weight_agricultural_added_value,
                                          weight_domestic_consumption_per_capita,
                                          weight_taxable_income_per_capita, scenario_pv_power,
                                          percentage_pv_target_roof):
        additional_power_distribution = []
        final_distribution = fb.FirstModule.get_final_distribution(typology, weight_equivalent_hours_pv,
                                                                   weight_agricultural_added_value,
                                                                   weight_domestic_consumption_per_capita,
                                                                   weight_taxable_income_per_capita)
        for i in range(len(final_distribution)):
            additional_power_distribution.append(
                final_distribution[i] * sb.SecondModule.get_percentage_additional_power(typology, scenario_pv_power,
                                                                                        percentage_pv_target_roof))
        return additional_power_distribution

    @staticmethod
    def get_target_pv_occupied_surface_land(pv_density_target_land, weight_equivalent_hours_pv,
                                            weight_agricultural_added_value, weight_domestic_consumption_per_capita,
                                            weight_taxable_income_per_capita, scenario_pv_power,
                                            percentage_pv_target_roof):
        target_pv_occupied_surface = []
        additional_power_distribution = ThirdModule.get_additional_power_distribution(weight_equivalent_hours_pv,
                                                                                      weight_agricultural_added_value,
                                                                                      weight_domestic_consumption_per_capita,
                                                                                      weight_taxable_income_per_capita,
                                                                                      scenario_pv_power,
                                                                                      percentage_pv_target_roof)
        for i in range(len(additional_power_distribution)):
            target_pv_occupied_surface.append(additional_power_distribution[i] / pv_density_target_land)
        return target_pv_occupied_surface

    @staticmethod
    def get_pv_power_target_land(weight_equivalent_hours_pv, weight_agricultural_added_value,
                                 weight_domestic_consumption_per_capita,
                                 weight_taxable_income_per_capita, scenario_pv_power,
                                 percentage_pv_target_roof):
        pv_power_target_land = []
        installed_power_land = dm.get_datas(0)
        additional_power_distribution_land = ThirdModule.get_additional_power_distribution(
            weight_equivalent_hours_pv,
            weight_agricultural_added_value, weight_domestic_consumption_per_capita,
            weight_taxable_income_per_capita, scenario_pv_power,
            percentage_pv_target_roof)
        for i in range(len(installed_power_land)):
            pv_power_target_land.append(installed_power_land[i] + additional_power_distribution_land[i])
        return pv_power_target_land
