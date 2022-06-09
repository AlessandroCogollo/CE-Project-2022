from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from psycopg2.extensions import JSON
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Optional

from project.flaskr import leaflet_plotter
from project.utils.Parameters import Parameters

app = Flask(__name__)

app.config['SECRET_KEY'] = 'df0331cefc6c2b9a5d0208a726a5d1c0fd37324feba25506'


class ParamsForm(FlaskForm):
    ScenarioPVpower = FloatField("Scenario PV Power", validators=[DataRequired(), NumberRange(min=0)])
    PercentagePVtargetROOF = FloatField("Percentage PV target ROOF", validators=[DataRequired(), NumberRange(min=0)])
    PVtargetROOF = FloatField("PV target ROOF", validators=[DataRequired(), NumberRange(min=0)])
    PVbaseROOF = FloatField("PV base ROOF", validators=[DataRequired(), NumberRange(min=0)])
    PVtargetLAND = FloatField("PV target LAND", validators=[DataRequired(), NumberRange(min=0)])
    WeightEquivalentHoursPV = FloatField("Weight Equivalent Hours PV", validators=[Optional()], default=1)
    WeightDomesticConsumptionPerCapita = FloatField("Weight Domestic Consumption Per Capita", validators=[Optional()],
                                                    default=1)
    WeightTaxableIncomePerCapita = FloatField("Weight Taxable Income Per Capita", validators=[Optional()], default=1)
    WeightAgriculturalAddedValue = FloatField("Weight Agricultural Added Value", validators=[Optional()], default=1)
    submit = SubmitField("Submit")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create/', methods=('GET', 'POST'))
def create():
    form = ParamsForm()
    content_type = request.headers.get('Content-Type')

    if content_type == 'application/json':

        json = request.json

        paramarray = []
        for elem in json:
            paramarray.append(elem['value'])

        paramarray.pop(0)

        if len(paramarray) == 9:

            paramarray = [float(item) for item in paramarray]
            parameters = Parameters(paramarray[0],
                                    paramarray[1],
                                    paramarray[2],
                                    paramarray[3],
                                    paramarray[4],
                                    paramarray[5],
                                    paramarray[6],
                                    paramarray[7],
                                    paramarray[8],
                                    )
            leaflet_plotter.plot(parameters)
            return render_template('singlemap.html')

        elif len(paramarray) == 19:

            paramarray.pop(9)
            paramarray = [float(item) for item in paramarray]

            parameters1 = Parameters(paramarray[0],
                                     paramarray[1],
                                     paramarray[2],
                                     paramarray[3],
                                     paramarray[4],
                                     paramarray[5],
                                     paramarray[6],
                                     paramarray[7],
                                     paramarray[8],
                                     )
            parameters2 = Parameters(paramarray[9],
                                     paramarray[10],
                                     paramarray[11],
                                     paramarray[12],
                                     paramarray[13],
                                     paramarray[14],
                                     paramarray[15],
                                     paramarray[16],
                                     paramarray[17],
                                     )
            leaflet_plotter.plot(parameters1, parameters2)
            return render_template('doublemap.html')

        else:
            # TODO: raise exception
            print("error")
    else:
        print('Content-Type not supported!')
        # TODO: add error page
    return render_template('create.html', form=form)


@app.route("/map/")
def showmap():
    return render_template('singlemap.html')


@app.route("/base_map/")
def base_map():
    return render_template('base_map.html')


@app.route("/doublemap/")
def comparemap():
    return render_template('doublemap.html')
