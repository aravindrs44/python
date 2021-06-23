from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo

@app.route('/')
def redirectToHome():
    return redirect('/dojos')

# -----------  GET ALL DOJOS PAGE  --------------#
@app.route('/dojos')
def all_dojo_page():
    dojos_display = Dojo.get_all_dojos()
    return render_template("dojos.html", dojos = dojos_display)

# ------------  SHOW ONE DOJO PAGE  -------------------#
@app.route('/dojos/<int:dojo_id>')
def one_dojo_page(dojo_id):
    print(dojo_id)

    return render_template("dojo_show.html")

# ----------------  NEW DOJO PAGE  -------------------#
@app.route('/new/dojo', methods = ["POST"])
def new_dojo():
    data = {
        'name': request.form['name']
    }
    Dojo.create_dojo(data)
    return redirect('/dojos')