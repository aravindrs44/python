from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from flask_app import app
import re
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']



    @classmethod
    def register_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"
        results = connectToMySQL('login_and_registration').query_db(query, data)

    @classmethod
    def get_user_from_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('login_and_registration').query_db(query, data)
        print(results)
        if results == False:
            return results
        if results == ():
            return False
        return cls(results[0])

    @classmethod
    def get_one_user(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL('login_and_registration').query_db(query, data)
        return cls(results[0])

    @staticmethod
    def validate_user(user):
        is_valid = True
        validate_candidate = User.get_user_from_email(user)
        if validate_candidate != False:
            flash("Account already exists!")
            is_valid = False
            return is_valid
        if user['password'] != user['confirm_password'] or len(user['password']) < 8:
            flash("Passwords do not match!")
            is_valid = False
        if len(user['first_name']) < 2:
            flash("First name must be longer than 2 characters!")
            is_valid = False
        if len(user['last_name']) < 2:
            flash("Last name must be longer than 2 characters!")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address!")
            is_valid = False
        return is_valid

    @staticmethod
    def login_validation(user):
        is_valid = True
        print(user)
        user_info = User.get_user_from_email(user)
        if user_info == False:
            flash("Login failed")
            is_valid = False
            return is_valid
        if not bcrypt.check_password_hash(user_info.password, user['password']):
            flash("Login failed")
            is_valid = False
        return is_valid
