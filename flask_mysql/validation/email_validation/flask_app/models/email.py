from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Email:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_email(data):
        query = "INSERT INTO users (email, created_at, updated_at) VALUES(%{email}s, NOW(), NOW();)"
        results = connectToMySQL("email_validation_schema").query_db(query, data)

    @classmethod
    def get_all_emails():
        query = "SELECT * FROM emails ORDER BY id DESC;"
        results = connectToMySQL("email_validation_schema").query_db(query)
        return cls(results)

    @staticmethod
    def validate_email(thisispain):
        is_valid = True
        print(email)
        if not EMAIL_REGEX.match(thisispain['email']):
            flash("Invalid email address!")
            is_valid = False
        return is_valid