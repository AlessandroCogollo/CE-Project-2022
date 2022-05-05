from ..modules import FourthBlock as fb
from ..modules import ThirdBlock as tb
from ..utils import DatasModule as dm


# block 6
class FourthModule:
    @staticmethod
    def get_pv_power_target(pv_density_target_land, weight_equivalent_hours_pv, weight_agricultural_added_value, weight_domestic_consumption_per_capita, weight_taxable_income_per_capita, scenario_pv_power, percentage_pv_target_roof):
        pv_power_target = []
        pv_power_target_roof = fb.FourthModule.get_pv_power_target_roof(weight_equivalent_hours_pv, weight_agricultural_added_value, weight_domestic_consumption_per_capita, weight_taxable_income_per_capita, scenario_pv_power, percentage_pv_target_roof)
        pv_power_target_land = tb.ThirdModule.get_pv_power_target_land(pv_density_target_land, weight_equivalent_hours_pv,
                                                                       weight_agricultural_added_value, weight_domestic_consumption_per_capita,
                                                                       weight_taxable_income_per_capita, scenario_pv_power)
        for i in range(len(pv_power_target_roof)):
            pv_power_target.append(pv_power_target_land[i] + pv_power_target_roof[i])
        return pv_power_target

    @staticmethod
    def get_production_profiles(pv_density_target_land, weight_equivalent_hours_pv, weight_agricultural_added_value, weight_domestic_consumption_per_capita, weight_taxable_income_per_capita, scenario_pv_power, percentage_pv_target_roof):
        production_profiles = []
        hourly_producibility = dm.get_datas(10)
        pv_power_target = FourthModule.get_pv_power_target(pv_density_target_land, weight_equivalent_hours_pv, weight_agricultural_added_value, weight_domestic_consumption_per_capita, weight_taxable_income_per_capita, scenario_pv_power, percentage_pv_target_roof)
        for i in range(len(hourly_producibility)):
            production_profiles.append(pv_power_target[i] * hourly_producibility[i])
        return production_profiles
