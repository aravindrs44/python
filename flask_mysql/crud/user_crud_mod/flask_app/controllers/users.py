from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User

@app.route('/')
def index():
    return redirect("/users")

# ------ SHOW PAGE ----------
@app.route('/users')
def users():
    display = User.get_all_users()
    return render_template("users.html", all_users = display)

@app.route('/users/new')
def users_new():
    return render_template("new.html")

# ---------CREATE USER PAGE-------------
@app.route('/users/create', methods = ["POST"])
def create_user():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    user_id = User.add_user(data)
    return redirect(f"/users/{user_id}")


# -------- SHOW ONE USER PAGE -----------
@app.route("/users/<int:id>")
def show_page(id):
    display = User.get_one_user({"id": id})
    return render_template('show.html', one_user = display)


# ---- EDIT PAGE -------
@app.route("/users/<int:id>/edit")
def edit_page(id):
    return render_template("edit.html", id = id)

@app.route("/edit/<int:id>", methods = ["POST"])
def edit_user(id):
    data = {
        'id': id,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.edit_query(data)
    return redirect(f"/users/{id}")


# ---------DELETE USER------------
@app.route("/users/delete/<int:id>")
def delete(id):
    print(id)
    User.delete_user({"id": id})
    return redirect("/users")