import math

from ..utils import ArithmeticModule as am


# block 1 & 2
class FirstModule:
    @staticmethod
    def get_final_distribution(data_obj, typology, weight_equivalent_hours_pv, weight_agricultural_added_value,
                               weight_domestic_consumption_per_capita, weight_taxable_income_per_capita):
        surface = []
        synthetical_indicator = []
        agricultural_added_value = []
        domestic_consumption = []
        domestic_consumption_per_capita = []
        province_population = []
        taxable_income_per_capita = []

        if typology == 0:  # get ROOF
            surface = data_obj.built_surface
            agricultural_added_value = data_obj.agricultural_added_value
        elif typology == 1:  # get LAND
            surface = data_obj.arable_land_area
            domestic_consumption = data_obj.domestic_consumption
            province_population = data_obj.province_population
            taxable_income_per_capita = data_obj.taxable_income_per_capita
        else:  # return ERROR
            print("ERROR")
        annual_sum_equivalent_hours_pv = data_obj.hourly_producibility
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
            indicator_domestic_consumption_per_capita = am.base_distribution(domestic_consumption_per_capita,
                                                                             am.mean(domestic_consumption_per_capita))
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
