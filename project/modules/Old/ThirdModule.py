from project.utils import ArithmeticModule as am


class ThirdModule:

    # return percentage_additional_power_land (mod3) && percentage_additional_power_roof (mod4)
    @staticmethod
    def get_percentage_additional_power(data_obj, params, typology):
        if typology == 0:  # get ROOF
            percentage_pv_additional_roof = am.sum_array(data_obj.other_areas_ROOF) / params.ScenarioPVpower
            percentage_pv_installed_roof = am.sum_array(data_obj.installed_power_ROOF) / params.ScenarioPVpower
            percentage_additional_roof = params.PercentagePVtargetROOF - percentage_pv_installed_roof - percentage_pv_additional_roof
            return params.ScenarioPVpower * percentage_additional_roof
        elif typology == 1:  # get LAND
            percentage_pv_additional_land = am.sum_array(data_obj.other_areas_LAND)/params.ScenarioPVpower
            percentage_pv_installed_land = am.sum_array(data_obj.installed_power_LAND)/params.ScenarioPVpower
            percentage_pv_target_land = 1 - params.PercentagePVtargetROOF
            percentage_additional_land = percentage_pv_target_land - percentage_pv_installed_land - percentage_pv_additional_land
            return params.ScenarioPVpower * percentage_additional_land
        else:  # TODO: return ERROR
            print("Error")
