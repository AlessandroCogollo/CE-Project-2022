from ..utils import ArithmeticModule as am
from ..utils import DatasModule as dm


# block 3 & 4
class SecondModule:
    @staticmethod
    def get_percentage_additional_power(typology, scenario_pv_power=None, percentage_pv_target_roof=None):
        percentage_pv_target = 0
        surface_other = []
        surface_installed = []
        if typology == 0:  # get LAND
            surface_other = dm.get_datas(2)
            surface_installed = dm.get_datas(0)
        elif typology == 1:  # get ROOF
            surface_other = dm.get_datas(3)
            surface_installed = dm.get_datas(1)
        else:
            print("ERROR")
        percentage_pv_additional = am.sum_array(surface_other) / scenario_pv_power
        percentage_pv_installed = am.sum_array(surface_installed) / scenario_pv_power
        if typology == 0:
            percentage_pv_target = 1 - percentage_pv_target_roof
        elif typology == 1:
            percentage_pv_target = percentage_pv_target_roof
        percentage_additional = percentage_pv_target - percentage_pv_installed - percentage_pv_additional
        return scenario_pv_power * percentage_additional

    @staticmethod
    def get_actual_pv_occupation_roof(pv_occupation_coefficient_base_roof):
        installed_power_roof = dm.get_datas(1)
        built_surface = dm.get_datas(4)
        actual_pv_occupation_roof = []
        for i in range(len(built_surface)):
            actual_pv_occupation_roof.append(installed_power_roof[i] * pv_occupation_coefficient_base_roof / built_surface[i])
        return actual_pv_occupation_roof
