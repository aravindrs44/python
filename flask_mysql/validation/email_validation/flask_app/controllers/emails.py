from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.email import Email

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/valid_check', methods = ["POST"])
def check_valid():
    data = {"email": request.form["email"]}
    if not Email.validate_email(data["email"]):
        return redirect('/')
    current_email = Email.create_email(data)
    return redirect('/success')

@app.route('/success')
def success_page():
    display = get_all_emails()
    return render_template('success.html')