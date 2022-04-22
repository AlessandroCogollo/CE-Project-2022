import array
import math

from ArithmeticModule import ArithmeticModule
from DatasModule import DatasModule


class PlotterModule:

    @staticmethod
    def get_actual_pv_occupation_roof(pv_occupation_coefficient_base_roof):
        installed_power_roof = DatasModule.get_datas(1)
        built_surface = DatasModule.get_datas(4)
        actual_pv_occupation_roof = array.array('f', [])
        for i in range(0, len(installed_power_roof)):
            actual_pv_occupation_roof.append((installed_power_roof[i] * pv_occupation_coefficient_base_roof) / built_surface[i])
        return actual_pv_occupation_roof

    @staticmethod
    def get_target_pv_occupied_surface_land(percentage_pv_target_roof, weight_equivalent_hours_pv, weight_agricultural_added_value, scenario_pv_power, pv_density_target_land):
        installed_power_land = DatasModule.get_datas(0)
        other_areas_land = DatasModule.get_datas(2)
        annual_sum_equivalent_hours_pv = DatasModule.get_datas(10)
        arable_land_area = DatasModule.get_datas(8)
        agricultural_added_value = DatasModule.get_datas(9)
        sum_arable_land_area = sum(arable_land_area)
        base_distribution_land = ArithmeticModule.base_distribution(arable_land_area, sum_arable_land_area)
        mean_sum_annual_equivalent_hours_pv = ArithmeticModule.sum(annual_sum_equivalent_hours_pv)
        indicator_equivalent_hours_pv = ArithmeticModule.base_distribution(annual_sum_equivalent_hours_pv, mean_sum_annual_equivalent_hours_pv)
        mean_agricultural_added_value = ArithmeticModule.sum(agricultural_added_value)
        indicator_agricultural_added_value = ArithmeticModule.base_distribution(agricultural_added_value, mean_agricultural_added_value)
        synthetical_indicator_land = math.exp(weight_equivalent_hours_pv * math.log(indicator_equivalent_hours_pv) - weight_agricultural_added_value * math.log(indicator_agricultural_added_value))
        synthetical_coefficient_land = synthetical_indicator_land * base_distribution_land
        sum_synthetical_coefficient_land = ArithmeticModule.sum(synthetical_coefficient_land)
        final_distribution_for_land = ArithmeticModule.base_distribution(synthetical_coefficient_land, sum_synthetical_coefficient_land)
        percentage_pv_target_land = 1 - percentage_pv_target_roof
        sum_installed_power_land = ArithmeticModule.sum(installed_power_land)
        percentage_pv_installed_land = sum_installed_power_land / scenario_pv_power
        sum_other_areas_land = ArithmeticModule.sum(other_areas_land)
        percentage_pv_additional_land = sum_other_areas_land / scenario_pv_power
        percentage_additional_land = percentage_pv_target_land - percentage_pv_installed_land - percentage_pv_additional_land
        percentage_additional_power_land = scenario_pv_power * percentage_additional_land
        additional_power_distribution_land = ArithmeticModule.base_distribution(final_distribution_for_land, percentage_additional_power_land)
        return ArithmeticModule.base_distribution(additional_power_distribution_land, pv_density_target_land)

    @staticmethod
    def get_target_pv_occupation_roof():
        pass

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
