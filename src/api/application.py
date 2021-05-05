from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm, Form
import sklearn
from wtforms import widgets, SelectMultipleField, SubmitField, SelectField
import os
from pickle import load
import pathlib
from platform import system

SECRET_KEY = 'development'
if system() == "Windows":
    model_path = '..\\..\\..\\model\\model'
else:
    model_path = '../../../model/model'
model_file = os.path.join(pathlib.Path(__file__), model_path)
model = load(open(model_file, 'rb'))

if system() == "Windows":
    symptons_path = '..\\..\\..\\data\\datasets\\transformed\\dummy_dataset_pt_translation'
    diseases_pt_br_path = '..\\..\\..\\data\\datasets\\transformed\\dummy_class_pt_translation'
    diseases_en_us_path = '..\\..\\..\\data\\datasets\\transformed\\class_dummy'
else:
    symptons_path = '../../../data/datasets/transformed/dummy_dataset_pt_translation'
    diseases_pt_br_path = '../../../data/datasets/transformed/dummy_class_pt_translation'
    diseases_en_us_path = '../../../data/datasets/transformed/class_dummy'

symptons_file = os.path.join(pathlib.Path(__file__), symptons_path)
symptons = list(load(open(symptons_file, 'rb')).items())
translate_symptons_dict = {int(i): s for i, s in symptons if int(i) != 0}

diseases_file = os.path.join(pathlib.Path(__file__), diseases_en_us_path)
diseases_en_us = list(load(open(diseases_file, 'rb')).keys())
diseases_file = os.path.join(pathlib.Path(__file__), diseases_pt_br_path)
diseases_pt_br = list(load(open(diseases_file, 'rb')).values())
translate_disease_dict = {k: v for k, v in zip(diseases_en_us, diseases_pt_br)}

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
    input_list = symptons + [0] * (17 - len(symptons))
    print(input_list)
    prediction = model.predict([input_list])[0]
    return prediction


def translate_disease(disease_in_english):
    return translate_disease_dict[disease_in_english]


@application.route('/', methods=['post', 'get'])
def hello_world():
    form = SimpleForm()
    form.symptons.choices = [(int(i), s) for i, s in symptons if int(i) != 0]

    return render_template('home.html', form=form)


@application.route('/predict', methods=['post'])
def predict():
    sintomas = [translate_symptons_dict[int(x)] for x in request.form.getlist('symptons')]
    doenca = translate_disease(predict_disease(request.form.getlist('symptons')))
    frase = 'Seus sintomas são ' + ', '.join(sintomas) + '.\n\nNosso sistema acredita que você esteja com ' + doenca + '.'

    return frase
