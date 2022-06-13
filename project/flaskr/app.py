from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Optional

from project.graphs import leaflet_plotter
from project.utils.GarbageCleaner import GarbageCleaner
from project.utils.Parameters import Parameters

app = Flask(__name__)

app.config['SECRET_KEY'] = 'df0331cefc6c2b9a5d0208a726a5d1c0fd37324feba25506'

garbage_sonar = GarbageCleaner()


class ParamsForm(FlaskForm):
    ScenarioPVpower = FloatField("Scenario PV Power [MV]", validators=[DataRequired(), NumberRange(min=0)],
                                 default="52000")
    PercentagePVtargetROOF = FloatField("Percentage PV target ROOF [%]",
                                        validators=[DataRequired(), NumberRange(min=0)], default="40")
    PVtargetROOF = FloatField("PV target ROOF [km2/MW]", validators=[DataRequired(), NumberRange(min=0)],
                              default="0.005")
    PVbaseROOF = FloatField("PV base ROOF [km2/MW]", validators=[DataRequired(), NumberRange(min=0)], default="0.008")
    PVtargetLAND = FloatField("PV target LAND [MW/km2]", validators=[DataRequired(), NumberRange(min=0)],
                              default="90.9")
    WeightEquivalentHoursPV = FloatField("Weight Equivalent Hours PV", validators=[Optional()])
    WeightDomesticConsumptionPerCapita = FloatField("Weight Domestic Consumption Per Capita", validators=[Optional()])
    WeightTaxableIncomePerCapita = FloatField("Weight Taxable Income Per Capita", validators=[Optional()])
    WeightAgriculturalAddedValue = FloatField("Weight Agricultural Added Value", validators=[Optional()])

    # -------------- OPTIONALS ---------------
    ScenarioPVpowerOpt = FloatField("Scenario PV Power [MV]", validators=[DataRequired(), NumberRange(min=0)],
                                    default="52000")
    PercentagePVtargetROOFOpt = FloatField("Percentage PV target ROOF [%]",
                                           validators=[DataRequired(), NumberRange(min=0)], default="40")
    PVtargetROOFOpt = FloatField("PV target ROOF [km2/MW]", validators=[DataRequired(), NumberRange(min=0)],
                                 default="0.005")
    PVbaseROOFOpt = FloatField("PV base ROOF [km2/MW]", validators=[DataRequired(), NumberRange(min=0)],
                               default="0.008")
    PVtargetLANDOpt = FloatField("PV target LAND [MW/km2]", validators=[DataRequired(), NumberRange(min=0)],
                                 default="90.9")
    WeightEquivalentHoursPVOpt = FloatField("Weight Equivalent Hours PV", validators=[Optional()])
    WeightDomesticConsumptionPerCapitaOpt = FloatField("Weight Domestic Consumption Per Capita",
                                                       validators=[Optional()])
    WeightTaxableIncomePerCapitaOpt = FloatField("Weight Taxable Income Per Capita", validators=[Optional()])
    WeightAgriculturalAddedValueOpt = FloatField("Weight Agricultural Added Value", validators=[Optional()])

    submitBtn = SubmitField("Submit")

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('error.html', msg="Page not found")

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create/', methods=('GET', 'POST'))
def create():
    form = ParamsForm()
    return render_template('create.html', form=form)


@app.route("/mapplot/", methods=('GET', 'POST'))
def mapplot():
    form = request.form
    paramarray = []
    for elem in form:
        if form[elem] != '' and elem != "submit" and elem != "csrf_token":
            paramarray.append(form[elem])

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
        print("---- plotting one map ----")
        token = leaflet_plotter.plot(parameters)
        return redirect("/showmap/" + token)

    elif len(paramarray) == 18:

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
        print("---- plotting two maps ----")
        token = leaflet_plotter.plot(parameters1, parameters2)
        return redirect("/showmap/" + token)
    else:
        print("---- ERROR! Invalid request ----")
        return render_template('error.html', msg="Server didn't receive enough parameters to perform a plot")


@app.route("/showmap/<token>")
def showmap(token):
    garbage_sonar.main()
    return render_template("/plots/" + token + ".html")

if __name__ == '__main__':
    app.run()
