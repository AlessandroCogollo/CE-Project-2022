from .SecondModule import SecondModule
from .ThirdModule import ThirdModule
from project.utils import ArithmeticModule as am


class FourthModule:

    # return additional_power_distribution_land (mod5) && additional_power_distribution_roof (mod6)
    @staticmethod
    def get_additional_power_distribution(data_obj, params, typology):
        return am.base_distribution(SecondModule.get_final_distribution(data_obj, params, typology),
                                    (1 / ThirdModule.get_percentage_additional_power(data_obj, params, typology)))
