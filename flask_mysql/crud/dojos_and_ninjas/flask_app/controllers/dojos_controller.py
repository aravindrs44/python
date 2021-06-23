from flask import render_template, redirect, request, session, flash
from flask_app import app
from ..models.dojo import Dojo
from  ..models.ninja import Ninja

# -----------  REDIRECT TO DOJOS PAGE FROM HOME  --------------#
@app.route('/')
def home_to_dojo():
    return redirect('/dojos')

# -----------  GET ALL DOJOS PAGE  --------------#
@app.route('/dojos')
def initialize_dojo_page():
    dojos = Dojo.get_all_dojos()
    return render_template('dojos.html', dojos_list = dojos)

# ----------------  NEW DOJO PAGE  -------------------#
@app.route('/newdojo', methods = ["POST"])
def add_dojo_to_page():
    data = {
        'name': request.form['name']
    }
    Dojo.add_dojo(data)
    return redirect('/dojos')

# ------------  SHOW ONE DOJO PAGE  -------------------#
@app.route('/dojos/<int:id>')
def initialize_show_one_dojo_page(id):
    data = {
        'id': id
    }
    return render_template('show_dojos.html', dn_joined = Dojo.get_dojo_and_ninjas_info(data))
