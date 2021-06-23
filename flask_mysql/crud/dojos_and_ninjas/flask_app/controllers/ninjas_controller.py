from flask import render_template, redirect, request, session
from flask_app import app
from ..models.dojo import Dojo
from  ..models.ninja import Ninja

@app.route('/ninjas')
def initialize_ninja_page():
    return render_template('ninjas.html', dojos_list = Dojo.get_all_dojos())

@app.route('/createninja', methods  = ["POST"])
def new_ninja():
    data = {
        'dojo_id': request.form['dojo_id'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age']
    }
    id_dojo = data['dojo_id']
    Ninja.add_ninja(data)
    return redirect(f"/dojos/{id_dojo}")
