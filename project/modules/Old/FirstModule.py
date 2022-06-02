from project.utils import ArithmeticModule as am


class FirstModule:

    @staticmethod
    def get_base_distribution(data_obj, params, typology):
        # returns an array of base_distribution_ROOF && base_distribution_LAND
        if typology == 0:  # get ROOF
            return am.base_distribution(data_obj.built_surface, am.sum_array(data_obj.built_surface))
        elif typology == 1:  # get LAND
            return am.base_distribution(data_obj.arable_land_area, am.sum_array(data_obj.arable_land_area))
        else:  # TODO: return ERROR
            print("Error")
