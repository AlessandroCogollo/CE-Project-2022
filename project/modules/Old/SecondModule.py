import math
import array as arr

from .FirstModule import FirstModule
from project.utils import ArithmeticModule as am


class SecondModule:

    @staticmethod
    def get_synthetical_indicator(data_obj, params, typology):
        synthetical_indicator = []
        indicator_equivalent_hours_pv = am.base_distribution(data_obj.hourly_producibility,
                                                             am.mean(data_obj.hourly_producibility))
        if typology == 0:  # get ROOF
            domestic_consumption_per_capita = am.array_division(data_obj.domestic_consumption,
                                                                data_obj.province_population)
            indicator_domestic_consumption_per_capita = am.base_distribution(domestic_consumption_per_capita,
                                                                             am.mean(domestic_consumption_per_capita))
            for i in range(len(data_obj.taxable_income_per_capita)):
                synthetical_indicator.append(
                    math.exp(params.WeightEquivalentHoursPV * math.log(indicator_equivalent_hours_pv[i])
                             + params.WeightDomesticConsumptionPerCapita * math.log(
                        indicator_domestic_consumption_per_capita[i])
                             + params.WeightTaxableIncomePerCapita * math.log((data_obj.taxable_income_per_capita[i]))))
            return synthetical_indicator
        elif typology == 1:  # get LAND
            indicator_agricultural_added_value = am.base_distribution(data_obj.agricultural_added_value,
                                                                      am.mean(data_obj.agricultural_added_value))
            for i in range(0, len(indicator_equivalent_hours_pv)):
                synthetical_indicator.append(
                    math.exp(params.WeightEquivalentHoursPV * math.log(indicator_equivalent_hours_pv[i])
                             - params.WeightAgriculturalAddedValue * math.log(indicator_agricultural_added_value[i])))
            return synthetical_indicator
        else:  # TODO: return ERROR
            print("Error")

    @staticmethod
    def get_final_distribution(data_obj, params, typology):
        synthetical_coefficient = am.array_product(SecondModule.get_synthetical_indicator(data_obj, params, typology),
                                                   FirstModule.get_base_distribution(data_obj, params, typology))
        return am.base_distribution(synthetical_coefficient, am.sum_array(synthetical_coefficient))
