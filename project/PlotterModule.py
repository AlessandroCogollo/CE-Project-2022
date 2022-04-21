import array

from DatasModule import DatasModule


class PlotterModule:

    @staticmethod
    def get_actual_pv_occupation_roof(pv_occupation_coefficient_base_roof):
        installed_power_roof = DatasModule.get_datas(1)
        built_surface = DatasModule.get_datas(4)
        tmp = array.array('f', [])
        for i in range(0, len(installed_power_roof)):
            tmp.append((installed_power_roof[i] * pv_occupation_coefficient_base_roof) / built_surface[i])
        return tmp

    @staticmethod
    def get_target_pv_occupied_surface_land():
        pass

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
