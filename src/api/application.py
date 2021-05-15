from flask_sqlalchemy import SQLAlchemy
from flask_select2 import Select2
from flask_select2.model.fields import AjaxSelectMultipleField
from flask_select2.contrib.sqla.ajax import QueryAjaxModelLoader
from flask import Flask, render_template, request, flash, Markup
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
import sklearn
import os
from pickle import load
import pathlib
from platform import system


application = Flask(__name__)
bootstrap = Bootstrap(application)
select2 = Select2()

# Create dummy secrey key so we can use sessions
application.config['SECRET_KEY'] = '123456790'

# Create in-memory database
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'

db = SQLAlchemy(application)


if system() == "Windows":
    model_path = '..\\..\\..\\model\\model'
else:
    model_path = '../../../model/model'
model_file = os.path.join(pathlib.Path(__file__), model_path)
model = load(open(model_file, 'rb'))

if system() == "Windows":
    symptons_path = '..\\..\\..\\data\\datasets\\transformed\\dummy_dataset_pt_translation'
    professional_path = '..\\..\\data\\datasets\\transformed\\professionals_pt'
    diseases_pt_br_path = '..\\..\\..\\data\\datasets\\transformed\\dummy_class_pt_translation'
    diseases_en_us_path = '..\\..\\..\\data\\datasets\\transformed\\class_dummy'
else:
    symptons_path = '../../../data/datasets/transformed/dummy_dataset_pt_translation'
    diseases_pt_br_path = '../../../data/datasets/transformed/dummy_class_pt_translation'
    professional_path = '../../../data/datasets/transformed/professionals_pt'
    diseases_en_us_path = '../../../data/datasets/transformed/class_dummy'

symptons_file = os.path.join(pathlib.Path(__file__), symptons_path)
symptons = list(load(open(symptons_file, 'rb')).items())
translate_symptons_dict = {int(i): s for i, s in symptons if int(i) != 0}

professional_dict = load(open(professional_path,'rb'))
diseases_file = os.path.join(pathlib.Path(__file__), diseases_en_us_path)
diseases_en_us = list(load(open(diseases_file, 'rb')).keys())
diseases_file = os.path.join(pathlib.Path(__file__), diseases_pt_br_path)
diseases_pt_br = list(load(open(diseases_file, 'rb')).values())
translate_disease_dict = {k: v for k, v in zip(diseases_en_us, diseases_pt_br)}


class Sympton(db.Model):
    __tablename__ = 'sympton'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(255), nullable=False)
    sympton_id = db.Column(db.Integer, nullable=False)

    def __str__(self):
        return str(self.name)


sympton_loader = QueryAjaxModelLoader(
    name='sympton',
    session=db.session,
    model=Sympton,
    fields=['name'],
    order_by=[Sympton.name.asc()],
    page_size=50,
    placeholder="Clique para ver os sintomas"
)

select2.init_app(application)
select2.add_loader(loader=sympton_loader)


class SymptonForm(FlaskForm):

    multiple_sympton = AjaxSelectMultipleField(
        loader=sympton_loader,
        label='Selecione seus sintomas',
        allow_blank=False
    )


def predict_disease(symptons):
    input_list = symptons + [0] * (17 - len(symptons))
    print('vetor_entrada_modelo', input_list)
    print('saída_do_modelo', model.predict([input_list]))
    prediction = model.predict([input_list])[0]
    return prediction


def translate_disease(disease_in_english):
    return translate_disease_dict[disease_in_english]


# Flask views
@application.route('/', methods=['GET', 'POST'])
def index():
    _form = SymptonForm()

    if _form.validate_on_submit():

        sintomas = [translate_symptons_dict[int(x.sympton_id)] for x in _form.multiple_sympton.data]
        doenca = translate_disease(predict_disease([c.sympton_id for c in _form.multiple_sympton.data]))
        profissional = professional_dict[str(doenca)]
        print('sintomas', sintomas)
        print('doenca', doenca)
        print('profissional', profissional)

        flash("Seus sintomas são: {names}.".format(names=', '.join(c.name for c in _form.multiple_sympton.data)), category='success')
        flash(f"Nosso sistema acredita que você esteja com: {doenca}", category='success')
        flash(Markup(f'<a href =\"https://www.google.com/maps/search/{profissional}\">Clique aqui</a> e consulte um especialista próximo à sua localização atual.'), category='success')

    return render_template('index.html', form=_form)


@application.before_first_request
def build_sample_db():

    db.drop_all()
    db.create_all()

    d = [{'name': s, 'sympton_id': i} for i, s in symptons if int(i) != 0]

    db.session.bulk_insert_mappings(
        Sympton,
        d
    )

    db.session.commit()


@application.route('/predict', methods=['post'])
def predict():
    sintomas = [translate_symptons_dict[int(x)] for x in request.form.getlist('symptons')]
    doenca = translate_disease(predict_disease(request.form.getlist('symptons')))
    profissional = professional_dict[str(doenca)]
    frase = 'Seus sintomas são ' + ', '.join(sintomas) + '.<br><br>Nosso sistema acredita que você esteja com <b>' + doenca + '</b>. <br><br><a href=\"https://www.google.com/maps/search/'+profissional+'\">Clique aqui</a> e consulte um especialista próximo à sua localização atual.'
    return frase


if __name__ == '__main__':
    application.run(port=5000, debug=True)