from unicodedata import decimal

from flask import Flask, render_template, request, url_for, redirect

from project.flaskr import bokeh_plotter
from project.flaskr import leaflet_plotter

app = Flask(__name__)
app.config['SECRET_KEY'] = 'df0331cefc6c2b9a5d0208a726a5d1c0fd37324feba25506'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        p1 = request.form.get('ScenarioPVpower', type=float)
        p2 = request.form.get('PercentagePVtargetROOF', type=float)
        p3 = request.form.get('PVtargetROOF', type=float)
        p4 = request.form.get('PVbaseROOF', type=float)
        p5 = request.form.get('PVtargetLAND', type=float)
        p6 = request.form.get('WeightEquivalentHoursPV', type=float)
        p7 = request.form.get('WeightDomesticConsumptionPerCapita', type=float)
        p8 = request.form.get('WeightTaxableIncomePerCapita', type=float)
        p9 = request.form.get('WeightAgriculturalAddedValue', type=float)

        parameters = Parameters(p1, p2, p3, p4, p5, p6, p7, p8, p9)
        leaflet_plotter.plot()
        # bokeh_plotter.set_param(bokeh_plotter, parameters)
        # bokeh_plotter.plot()

    return render_template('map.html')


class Parameters:

    def __init__(self, p1, p2, p3, p4, p5, p6, p7, p8, p9):
        self.ScenarioPVpower = p1
        self.PercentagePVtargetROOF = p2
        self.PVtargetROOF = p3
        self.PVbaseROOF = p4
        self.PVtargetLAND = p5
        self.WeightEquivalentHoursPV = p6
        self.WeightDomesticConsumptionPerCapita = p7
        self.WeightTaxableIncomePerCapita = p8
        self.WeightAgriculturalAddedValue = p9
