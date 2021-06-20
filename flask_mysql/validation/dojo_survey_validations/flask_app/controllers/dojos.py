from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods = ["POST"])
def survey_input():
    data = {
    'name': request.form["name"],
    'location': request.form["location"],
    'language': request.form["language"],
    'comment': request.form["comment"]
    }
    if not Dojo.validate_dojo(request.form):
        return redirect('/')
    survey = Dojo.create_survey(data)
    return redirect('/result')

@app.route('/result')
def show_survey():
    latest_survey = Dojo.retrieve_latest()
    return render_template('result.html', survey = latest_survey)