import array as arr
from project.modules.ComputationalModule import ComputationalModule as cm
import project.utils.ArithmeticModule as am


class OutputValues:

    def __init__(self, data_obj, params):
        self.data_obj = data_obj
        self.params = params

        self.actual_pv_occupation_roof = OutputValues.get_actual_pv_occupation_roof(self)
        self.target_pv_occupied_surface_land = OutputValues.get_target_pv_occupied_surface_land(self)
        self.pv_power_target_land = OutputValues.get_pv_power_target_land(self)
        self.pv_power_target_roof = OutputValues.get_pv_power_target_roof(self)
        self.additional_pv_occupation_roof = OutputValues.get_additional_pv_occupation_roof(self)
        self.target_pv_occupation_roof = OutputValues.get_target_pv_occupation_roof(self)
        self.pv_power_target = OutputValues.get_pv_power_target(self)
        self.production_profiles = OutputValues.get_production_profiles(self)

    def get_actual_pv_occupation_roof(self):
        return am.array_division(
            am.base_distribution(self.data_obj.installed_power_ROOF, 1 / self.params.PVbaseROOF),
            self.data_obj.built_surface)

    def get_target_pv_occupied_surface_land(self):
        return am.base_distribution(
            cm.get_additional_power_distribution(self.data_obj, self.params, 0),
            self.params.PVtargetLAND)

    def get_pv_power_target_land(self):
        pv_power_target_land = arr.array("d", [])
        for i in range(len(self.data_obj.installed_power_LAND)):
            pv_power_target_land.append(self.data_obj.installed_power_LAND[i] +
                                        cm.get_additional_power_distribution(self.data_obj, self.params, 1)[i])
        return pv_power_target_land

    def get_pv_power_target_roof(self):
        pv_power_target_roof = arr.array("d", [])
        additional_power_distribution = cm.get_additional_power_distribution(self.data_obj, self.params, 0)
        for i in range(len(self.data_obj.installed_power_ROOF)):
            pv_power_target_roof.append((self.data_obj.installed_power_ROOF[i]) + (additional_power_distribution[i]) + (
                self.data_obj.other_areas_ROOF[i]))
        return pv_power_target_roof

    def get_additional_pv_occupation_roof(self):
        return am.array_division(
            am.base_distribution(
                cm.get_additional_power_distribution(self.data_obj, self.params, 0),
                1 / self.params.PVtargetROOF),
            self.data_obj.built_surface)

    def get_target_pv_occupation_roof(self):
        target_pv_occupation_roof = arr.array("d", [])
        for i in range(len(self.data_obj.installed_power_ROOF)):
            target_pv_occupation_roof.append(
                (am.base_distribution(self.data_obj.installed_power_ROOF, 1 / self.params.PVbaseROOF)[i] +
                 am.base_distribution(cm.get_additional_power_distribution(self.data_obj, self.params, 0),
                                      1 / self.params.PVtargetROOF)[i]) / self.data_obj.built_surface[i])
        return target_pv_occupation_roof

    def get_pv_power_target(self):
        pv_power_target = arr.array("d", [])
        for i in range(len(OutputValues.get_pv_power_target_roof(self))):
            pv_power_target.append(OutputValues.get_pv_power_target_roof(self)[i] +
                                   OutputValues.get_pv_power_target_land(self)[i])
        return pv_power_target

    def get_production_profiles(self):
        return am.array_product(OutputValues.get_pv_power_target(self),
                                self.data_obj.hourly_producibility)
