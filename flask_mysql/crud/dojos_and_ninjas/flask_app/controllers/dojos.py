from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo

@app.route('/')
def redirectToHome():
    return redirect('/dojos')

# -----------  CREATE GET ALL USER PAGE  --------------#
@app.route('/dojos')
def all_dojo_page():
    dojos_display = Dojo.get_all_dojos()
    return render_template("dojos.html", dojos = dojos_display)

# ------------  SHOW ONE USER PAGE  -------------------#
@app.route('/dojos/<int:id>')
def one_dojo_page(id):
    
    return render_template("dojo_show.html", dojo_id = id)

# ----------------  NEW NINJA PAGE  -------------------#