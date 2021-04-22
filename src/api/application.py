from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import widgets, RadioField, SelectMultipleField, SubmitField, SelectField

SECRET_KEY = 'development'

bootstrap = Bootstrap()
application = Flask(__name__)
application.config.from_object(__name__)

bootstrap.init_app(application)


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class SimpleForm(FlaskForm):
    symptons = MultiCheckboxField('Label')
    # example = RadioField('Label')


@application.route('/', methods=['post', 'get'])
def hello_world():
    form = SimpleForm()
    symptons = ["febre", "dor_de_cabeca", "coriza", "tosse"]
    form.symptons.choices = [(s, s) for s in symptons]

    return render_template('home.html', form=form)


@application.route('/predict', methods=['post'])
def predict():
    return str(request.form.getlist('symptons'))

