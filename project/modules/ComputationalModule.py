import math
import array as arr
import project.utils.ArithmeticModule as am


class ComputationalModule:

    @staticmethod
    def get_base_distribution(data_obj, params, typology):
        # returns an array of base_distribution_ROOF && base_distribution_LAND
        if typology == 0:  # get ROOF
            return am.base_distribution(data_obj.built_surface, am.sum_array(data_obj.built_surface))
        elif typology == 1:  # get LAND
            return am.base_distribution(data_obj.arable_land_area, am.sum_array(data_obj.arable_land_area))
        else:  # TODO: return ERROR
            print("Error")

    @staticmethod
    def get_synthetical_indicator(data_obj, params, typology):
        synthetical_indicator = arr.array('d', [])
        indicator_equivalent_hours_pv = am.base_distribution(data_obj.hourly_producibility,
                                                             am.mean(data_obj.hourly_producibility))
        if typology == 0:  # get ROOF
            domestic_consumption_per_capita = am.array_division(data_obj.domestic_consumption,
                                                                data_obj.province_population)
            indicator_domestic_consumption_per_capita = am.base_distribution(domestic_consumption_per_capita,
                                                                             am.mean(domestic_consumption_per_capita))
            for i in range(0, len(indicator_domestic_consumption_per_capita)):
                synthetical_indicator.append(
                    math.exp(params.WeightEquivalentHoursPV * math.log(indicator_equivalent_hours_pv[i])
                             + params.WeightDomesticConsumptionPerCapita * math.log(
                        indicator_domestic_consumption_per_capita[i])
                             + params.WeightTaxableIncomePerCapita * math.log((data_obj.taxable_income_per_capita[i]))))
            return synthetical_indicator
        elif typology == 1:  # get LAND
            indicator_agricultural_added_value = am.base_distribution(data_obj.agricultural_added_value,
                                                                      am.mean(data_obj.agricultural_added_value))
            for i in range(0, len(indicator_agricultural_added_value)):
                synthetical_indicator.append(
                    math.exp(params.WeightEquivalentHoursPV * math.log(indicator_equivalent_hours_pv[i])
                             - params.WeightAgriculturalAddedValue * math.log(indicator_agricultural_added_value[i])))
            return synthetical_indicator
        else:  # TODO: return ERROR
            print("Error")

    @staticmethod
    def get_final_distribution(data_obj, params, typology):
        synthetical_coefficient = am.array_product(
            ComputationalModule.get_synthetical_indicator(data_obj, params, typology),
            ComputationalModule.get_base_distribution(data_obj, params, typology))
        return am.base_distribution(synthetical_coefficient, am.sum_array(synthetical_coefficient))

    @staticmethod
    def get_percentage_additional_power(data_obj, params, typology):
        if typology == 0:  # get ROOF
            percentage_pv_additional_roof = am.sum_array(data_obj.other_areas_ROOF) / params.ScenarioPVpower
            percentage_pv_installed_roof = am.sum_array(data_obj.installed_power_ROOF) / params.ScenarioPVpower
            percentage_additional_roof = params.PercentagePVtargetROOF - percentage_pv_installed_roof - percentage_pv_additional_roof
            return params.ScenarioPVpower * percentage_additional_roof
        elif typology == 1:  # get LAND
            percentage_pv_additional_land = am.sum_array(data_obj.other_areas_LAND) / params.ScenarioPVpower
            percentage_pv_installed_land = am.sum_array(data_obj.installed_power_LAND) / params.ScenarioPVpower
            percentage_pv_target_land = 1 - params.PercentagePVtargetROOF
            percentage_additional_land = percentage_pv_target_land - percentage_pv_installed_land - percentage_pv_additional_land
            return params.ScenarioPVpower * percentage_additional_land
        else:  # TODO: return ERROR
            print("Error")

    @staticmethod
    def get_additional_power_distribution(data_obj, params, typology):
        return am.base_distribution(ComputationalModule.get_final_distribution(data_obj, params, typology),
                                    (1 / ComputationalModule.get_percentage_additional_power(data_obj, params,
                                                                                             typology)))
