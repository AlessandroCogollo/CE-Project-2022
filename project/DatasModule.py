import pandas as pd
import Exceptions as ex


class DatasModule:

    @staticmethod
    def get_datas(data_required):
        if data_required < 2:
            sheet = pd.read_csv('../docs/input/installed.csv')
            if data_required == 0:
                return sheet['Land']
            elif data_required == 1:
                return sheet['Roof']
            elif data_required == 2:
                return sheet['Other Land']
            else:
                return sheet['Other Roof']
        elif 4 <= data_required <= 9:
            sheet = pd.read_csv('../docs/input/variables.csv')
            if data_required == 4:
                return sheet['Built surface [km2]']
            elif data_required == 5:
                return sheet['Domestic consumption [GWh]']
            elif data_required == 6:
                return sheet['Population']
            elif data_required == 7:
                return sheet['Taxable income per capita']
            elif data_required == 8:
                return sheet['Arable land area [km2]']
            else:
                return sheet['Agricultural added value']
        elif data_required == 10:
            sheet = pd.read_csv('../docs/input/hourly_producibility.csv')
            # return whole sheet
            return sheet
        else:
            raise ex.IllegalDatasRequired
