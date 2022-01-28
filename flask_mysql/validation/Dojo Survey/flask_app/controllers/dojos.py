from flask_app.models.dojo import Dojo
from flask_app import app
from flask import render_template, request, redirect, session

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/create/survey', methods = ['POST'])
def create_survey():
    if Dojo.is_valid(request.form):
        Dojo.save (request.form)
        return redirect('/results')
    return redirect('/')

@app.route('/results')
def results():
    return render_template('results.html', dojo = Dojo.get_last_survey)