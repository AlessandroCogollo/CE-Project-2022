class IllegalDatasRequired(Exception):
    def __init__(self):
        super().__init__("IllegalDatasRequired: code of datas required doesn't refer to any available datas")
