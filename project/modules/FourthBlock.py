from ..modules import ThirdBlock as tb
from ..utils import DatasModule as dm


# block 6
class FourthModule:
    @staticmethod
    def get_pv_power_target_roof(weight_equivalent_hours_pv, weight_agricultural_added_value, weight_domestic_consumption_per_capita, weight_taxable_income_per_capita, scenario_pv_power, percentage_pv_target_roof):
        pv_power_target_roof = []
        installed_power_roof = dm.get_datas(1)
        other_areas_roof = dm.get_datas(3)
        additional_power_distribution_roof = tb.ThirdModule.get_additional_power_distribution(1, weight_equivalent_hours_pv, weight_agricultural_added_value, weight_domestic_consumption_per_capita, weight_taxable_income_per_capita, scenario_pv_power, percentage_pv_target_roof)
        for i in range(len(installed_power_roof)):
            pv_power_target_roof.append(installed_power_roof[i] + additional_power_distribution_roof[i] + other_areas_roof[i])
        return pv_power_target_roof

    @staticmethod
    def get_additional_pv_occupation_roof(weight_equivalent_hours_pv, weight_agricultural_added_value, weight_domestic_consumption_per_capita, weight_taxable_income_per_capita, scenario_pv_power, percentage_pv_target_roof, pv_occupation_coefficient_target_roof):
        additional_pv_occupation_roof = []
        built_surface = dm.get_datas(4)
        additional_power_distribution_roof = tb.ThirdModule.get_additional_power_distribution(1, weight_equivalent_hours_pv, weight_agricultural_added_value, weight_domestic_consumption_per_capita, weight_taxable_income_per_capita, scenario_pv_power, percentage_pv_target_roof)
        for i in range(len(additional_power_distribution_roof)):
            additional_pv_occupation_roof.append((additional_power_distribution_roof[i]*pv_occupation_coefficient_target_roof)/built_surface)
        return additional_pv_occupation_roof

    @staticmethod
    def get_target_pv_occupation_roof(weight_equivalent_hours_pv, weight_agricultural_added_value, weight_domestic_consumption_per_capita, weight_taxable_income_per_capita, scenario_pv_power, percentage_pv_target_roof, pv_occupation_coefficient_base_roof):
        target_pv_occupation_roof = []
        built_surface = dm.get_datas(4)
        installed_power_roof = dm.get_datas(1)
        additional_power_distribution_roof = tb.ThirdModule.get_additional_power_distribution(1, weight_equivalent_hours_pv, weight_agricultural_added_value, weight_domestic_consumption_per_capita, weight_taxable_income_per_capita, scenario_pv_power, percentage_pv_target_roof)
        for i in range(len(installed_power_roof)):
            target_pv_occupation_roof.append((installed_power_roof[i] * pv_occupation_coefficient_base_roof + additional_power_distribution_roof[i] * pv_occupation_coefficient_base_roof) / built_surface[i])
        return target_pv_occupation_roof
