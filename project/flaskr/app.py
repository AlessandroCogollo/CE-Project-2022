from flask import Flask, render_template, request, url_for, redirect

from project.flaskr import plotter

app = Flask(__name__)
app.config['SECRET_KEY'] = 'df0331cefc6c2b9a5d0208a726a5d1c0fd37324feba25506'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        p1 = request.form['ScenarioPVpower']
        p2 = request.form['PercentagePVtargetROOF']
        p3 = request.form['PVtargetROOF']
        p4 = request.form['PVbaseROOF']
        p5 = request.form['PVtargetLAND']
        p6 = request.form['WeightEquivalentHoursPV']
        p7 = request.form['WeightDomesticConsumptionPerCapita']
        p8 = request.form['WeightTaxableIncomePerCapita']
        p9 = request.form['WeightAgriculturalAddedValue']

        parameters = Parameters(p1, p2, p3, p4, p5, p6, p7, p8, p9)
        plotter.set_param(plotter, parameters)
        # return redirect(url_for('create'))
        plotter.plot()

    return render_template('create.html')


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
