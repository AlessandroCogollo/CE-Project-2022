import array
import math

import ArithmeticModule
from DatasModule import DatasModule
from project.modules.ThirdBlock import ThirdModule


class PlotterModule:

    @staticmethod
    def get_actual_pv_occupation_roof(data_obj, pv_occupation_coefficient_base_roof, self):
        installed_power_roof = data_obj.installed_power_ROOF
        built_surface = data_obj.built_surface
        actual_pv_occupation_roof = array.array('f', [])
        for i in range(0, len(installed_power_roof)):
            actual_pv_occupation_roof.append(
                (installed_power_roof[i] * pv_occupation_coefficient_base_roof) / built_surface[i])
        self.actual_pv_occupation_roof = actual_pv_occupation_roof
        return self.actual_pv_occupation_roof

    @staticmethod
    def get_target_pv_occupied_surface_land(data_obj, percentage_pv_target_roof, weight_equivalent_hours_pv,
                                            weight_agricultural_added_value, scenario_pv_power, pv_density_target_land,
                                            self):
        data_obj = DatasModule()
        installed_power_land = data_obj.installed_power_LAND
        other_areas_land = data_obj.other_areas_LAND
        annual_sum_equivalent_hours_pv = data_obj.hourly_producibility
        arable_land_area = data_obj.arable_land_area
        agricultural_added_value = data_obj.agricultural_added_value
        sum_arable_land_area = data_obj.arable_land_area
        base_distribution_land = ArithmeticModule.base_distribution(arable_land_area, sum_arable_land_area)
        mean_sum_annual_equivalent_hours_pv = ArithmeticModule.sum_array(annual_sum_equivalent_hours_pv)
        indicator_equivalent_hours_pv = ArithmeticModule.base_distribution(annual_sum_equivalent_hours_pv,
                                                                           mean_sum_annual_equivalent_hours_pv)
        mean_agricultural_added_value = ArithmeticModule.sum_array(agricultural_added_value)
        indicator_agricultural_added_value = ArithmeticModule.base_distribution(agricultural_added_value,
                                                                                mean_agricultural_added_value)
        synthetical_indicator_land = math.exp(weight_equivalent_hours_pv * math.log(
            indicator_equivalent_hours_pv) - weight_agricultural_added_value * math.log(
            indicator_agricultural_added_value))
        synthetical_coefficient_land = synthetical_indicator_land * base_distribution_land
        sum_synthetical_coefficient_land = ArithmeticModule.sum_array(synthetical_coefficient_land)
        final_distribution_for_land = ArithmeticModule.base_distribution(synthetical_coefficient_land,
                                                                         sum_synthetical_coefficient_land)
        percentage_pv_target_land = 1 - percentage_pv_target_roof
        sum_installed_power_land = ArithmeticModule.sum_array(installed_power_land)
        percentage_pv_installed_land = sum_installed_power_land / scenario_pv_power
        sum_other_areas_land = ArithmeticModule.sum_array(other_areas_land)
        percentage_pv_additional_land = sum_other_areas_land / scenario_pv_power
        percentage_additional_land = percentage_pv_target_land - percentage_pv_installed_land - percentage_pv_additional_land
        percentage_additional_power_land = scenario_pv_power * percentage_additional_land
        additional_power_distribution_land = ArithmeticModule.base_distribution(final_distribution_for_land,
                                                                                percentage_additional_power_land)
        self.target_pv_occupied_surface_land = ArithmeticModule.base_distribution(additional_power_distribution_land,
                                                                                  pv_density_target_land)
        return self.target_pv_occupied_surface_land

    @staticmethod
    def get_target_pv_occupation_roof(data_obj, pv_occupation_coefficient_base_roof,
                                      pv_occupation_coefficient_target_roof, self, weight_equivalent_hours_pv,
                                      weight_agricultural_added_value, weight_domestic_consumption_per_capita,
                                      weight_taxable_income_per_capita, scenario_pv_power,
                                      percentage_pv_target_roof):
        installed_power_roof = data_obj.installed_power_ROOF
        built_surface = data_obj.built_surface
        additional_power_distribution_roof = ThirdModule.get_additional_power_distribution(data_obj, 0,
                                                                                           weight_equivalent_hours_pv,
                                                                                           weight_agricultural_added_value,
                                                                                           weight_domestic_consumption_per_capita,
                                                                                           weight_taxable_income_per_capita,
                                                                                           scenario_pv_power,
                                                                                           percentage_pv_target_roof)
        temp_sum = []
        for i in range(len(installed_power_roof)):
            temp_sum.append((installed_power_roof[i] * pv_occupation_coefficient_base_roof +
                             additional_power_distribution_roof[i] * pv_occupation_coefficient_target_roof) /
                            built_surface[i])
        self.target_pv_occupied_surface_roof = temp_sum
        return self.target_pv_occupied_surface_roof

    @staticmethod
    def get_pv_power_target_land():
        pass

    @staticmethod
    def get_pv_power_target_roof():
        pass

    @staticmethod
    def get_pv_power_target():
        pass

    @staticmethod
    def get_production_profiles():
        pass
