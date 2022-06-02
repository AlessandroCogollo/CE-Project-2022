from project.modules.OutputValuesModule import OutputValues
from project.utils.DatasModule import DatasModule
from project.utils.Parameters import Parameters

class Orchestrator:


    def __init__(self):
        self.data_obj = DatasModule()
        self.params = Parameters(1, 1, 1, 1, 1, 1, 1, 1, 1)
        self.output_obj = OutputValues(self.data_obj, self.params)
