from flask import Flask, request, render_template, redirect, url_for, flash
import requests
from flask_pymongo import PyMongo
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import uuid

class ReusableForm(Form):
    commit = TextField('commit:', [validators.Length(min=5, max=40), validators.Regexp("^[0-9a-f]{5,40}$")])
    cmessage = TextField('cmessage:', [validators.Length(min=3, max=40)])


app = Flask(__name__)
app.config.from_object('settings')
app.config.from_object('version')
app.config["SECRET_KEY"] = "changeTracing4ever"
from flask_bootstrap import Bootstrap
Bootstrap(app)

mongo = PyMongo(app)

@app.route('/healthz')
def healthz():
    return 'Healthy'

@app.route('/version')
def version():
    return app.config['VERSION']

@app.route('/')
def hello_world():
    return 'Welcome! See changes here: <a href="/changes"> here </a>'

@app.route('/change', methods=['POST', 'GET'])
def add_change():

    form = ReusableForm(request.form)
    placeholder = uuid.uuid1().hex
    if request.method == 'POST':
        commit=request.form['commit']
        cmessage=request.form['cmessage']
        app.logger.info ("commit : %s, mesage: %s", commit, cmessage )
        if form.validate():
          app.logger.info ("form validated" )
          change = mongo.db.changes
          change_id = change.insert({'commit': commit, 'cmessage': cmessage})
          new_change = change.find_one({'_id': change_id })
          output = {'commit' : new_change['commit'], 'cmessage' : new_change['cmessage']}
          return redirect(url_for('get_all_changes'))
        else:
          app.logger.error (form.errors )
          flash('Error: ' + str(form.errors))

    return render_template('form.html', form=form, placeholder=placeholder)

@app.route('/changes', methods=['GET'])
def get_all_changes():
  change = mongo.db.changes
  output = []
  changes = change.find()
  return render_template(
        'front.html',
        changes=changes
    )

app.run(host='0.0.0.0', port='5000', debug=True)
