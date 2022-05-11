from ..utils import ArithmeticModule as am


# block 3 & 4
class SecondModule:
    @staticmethod
    def get_percentage_additional_power(data_obj, typology, scenario_pv_power=None, percentage_pv_target_roof=None):
        percentage_pv_target = 0
        surface_other = []
        surface_installed = []

        if typology == 0:  # get LAND
            surface_other = data_obj.other_areas_LAND
            surface_installed = data_obj.installed_power_LAND
        elif typology == 1:  # get ROOF
            surface_other = data_obj.other_areas_ROOF
            surface_installed = data_obj.installed_power_ROOF
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
    def get_actual_pv_occupation_roof(data_obj, pv_occupation_coefficient_base_roof):
        installed_power_roof = data_obj.installed_power_ROOF
        built_surface = data_obj.built_surface
        actual_pv_occupation_roof = []
        for i in range(len(built_surface)):
            actual_pv_occupation_roof.append(installed_power_roof[i] * pv_occupation_coefficient_base_roof / built_surface[i])
        return actual_pv_occupation_roof
