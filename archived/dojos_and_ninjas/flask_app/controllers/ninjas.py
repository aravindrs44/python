from flask import render_template, request, session, redirect

from flask_app import app
from ..models.dojo import Dojo
from ..models.ninja import Ninja

@app.route('/ninjas')
def ninja_page():
    return render_template('ninjas.html', dojos = Dojo.get_all_dojos())

@app.route('/createninja/', methods = ["POST"])
def add_ninja():
    haha = request.form['dojo_name']
    print(haha)
    return redirect('/dojos/<int:dojo_id>')