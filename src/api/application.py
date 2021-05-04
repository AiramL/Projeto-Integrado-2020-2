from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm, Form
from wtforms.validators import DataRequired
from wtforms import widgets, SelectMultipleField, SubmitField, SelectField
import os
from pickle import load
import pathlib

SECRET_KEY = 'development'
symptons_path = '/Users/vinob/Projeto-Integrado-2020-2/data/datasets/transformed/dataset_dummy'

symptons_file = os.path.join(pathlib.Path(__file__), symptons_path)
symptons = sorted([x.strip() for x in list(load(open(symptons_file, 'rb')).keys()) if
                   type(x) == str])

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


def predict_disease(symptons):
    if "febre" in symptons:
        return "dengue"
    else:
        return "..."


@application.route('/', methods=['post', 'get'])
def hello_world():
    form = SimpleForm()
    file = os.path.join(pathlib.Path(__file__), symptons_path)
    symptons = sorted([x.strip() for x in list(load(open(file, 'rb')).keys()) if
                       type(x) == str])
    form.symptons.choices = [(s, s) for s in symptons]

    return render_template('home.html', form=form)


@application.route('/predict', methods=['post'])
def predict():
    return predict_disease(request.form.getlist('symptons'))
