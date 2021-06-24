from flask import render_template, redirect, request, session, flash
from flask_app import app
from ..models.user import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def initialize_entry():
    if 'uuid' in session:
        return redirect('/loggedin')
    return render_template('index.html')

@app.route('/success')
def initialize_success_page():
    return render_template('success.html')

@app.route('/loggedin')
def initialize_loggedin_page():
    if 'uuid' not in session:
        return redirect('/')
    print(session['uuid'])
    data = {
        'id': session['uuid']
    }
    user = User.get_one_user(data)
    return render_template('welcome.html', user = user)

@app.route('/register', methods = ["POST"])
def register():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': request.form['password'],
        'confirm_password': request.form['confirm_password']
    }
    print(data)
    if not User.validate_user(data):
        return redirect('/')
    data['password'] = bcrypt.generate_password_hash(data['password'])
    data.pop('confirm_password')
    User.register_user(data)
    return redirect('/success')


@app.route('/welcome', methods = ["POST"])
def logged_in():
    data = {
        'email': request.form['log_in_email'],
        'password': request.form['log_in_password']
    }

    if not User.login_validation(data):
        return redirect('/')
    user = User.get_user_from_email(data)
    session['uuid'] = user.id
    return redirect('/loggedin')

@app.route('/logout')
def logout():
    session.pop('uuid')
    return redirect('/')
