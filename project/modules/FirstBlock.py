import math

from ..utils import ArithmeticModule as am
from ..utils import DatasModule as dm

# block 1 & 2
class FirstModule:
    @staticmethod
    def get_final_distribution(typology, weight_equivalent_hours_pv, weight_agricultural_added_value,
                               weight_domestic_consumption_per_capita=None, weight_taxable_income_per_capita=None):
        surface = []
        synthetical_indicator = []
        agricultural_added_value = []
        domestic_consumption = []
        domestic_consumption_per_capita = []
        province_population = []
        taxable_income_per_capita = []

        if typology == 0:  # get ROOF
            surface = dm.get_datas(4)
            agricultural_added_value = dm.get_datas(9)
        elif typology == 1:  # get LAND
            surface = dm.get_datas(0)
            domestic_consumption = dm.get_datas(5)
            province_population = dm.get_datas(6)
            taxable_income_per_capita = dm.get_datas(7)
        else:  # return ERROR
            print("ERROR")
        annual_sum_equivalent_hours_pv = dm.get_datas(10)
        base_distribution = am.base_distribution(surface, am.sum_array(surface))
        indicator_equivalent_hours_pv = am.base_distribution(annual_sum_equivalent_hours_pv,
                                                             am.mean(annual_sum_equivalent_hours_pv))
        if typology == 0:  # get syntheticalIndicatorLAND
            indicator_agricultural_added_value = am.base_distribution(agricultural_added_value,
                                                                      am.mean(agricultural_added_value))
            for i in range(len(indicator_equivalent_hours_pv)):
                synthetical_indicator.append(math.exp(weight_equivalent_hours_pv
                                                      * math.log(indicator_equivalent_hours_pv[i])
                                                      - weight_agricultural_added_value
                                                      * math.log(indicator_agricultural_added_value[i]))
                                             )
        elif typology == 1:  # get syntheticalIndicatorROOF
            for i in range(len(domestic_consumption)):
                domestic_consumption_per_capita.append(domestic_consumption[i] / province_population[i])
            indicator_domestic_consumption_per_capita = am.base_distribution(domestic_consumption_per_capita, am.mean(domestic_consumption_per_capita))
            for i in range(len(indicator_equivalent_hours_pv)):
                synthetical_indicator.append(math.exp(weight_equivalent_hours_pv
                                                      * math.log(indicator_equivalent_hours_pv[i])
                                                      + weight_domestic_consumption_per_capita
                                                      * math.log(indicator_domestic_consumption_per_capita[i])
                                                      + weight_taxable_income_per_capita
                                                      * math.log(taxable_income_per_capita))
                                             )
        else:  # get ERROR
            print("ERROR")
        synthetical_coefficient = am.array_product(synthetical_indicator, base_distribution)
        return am.base_distribution(synthetical_coefficient, am.sum_array(synthetical_coefficient))
