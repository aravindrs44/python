from flask import Flask, render_template, redirect, session, request

from user import User
app = Flask(__name__)
app.secret_key = 'Pokemon Colosseum Shadow Pokemon Lab OST. Yes'

@app.route('/')
def index():
    return redirect("/users")

@app.route('/users')
def users():
    display = User.get_all_users()
    return render_template("users.html", all_users = display)

@app.route('/users/new')
def users_new():
    return render_template("new.html")

@app.route('/users/create', methods = ["POST"])
def create_user():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.add_user(data)
    return redirect('/users')

if __name__ == "__main__":
    app.run(debug = True)
