from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class Email:
    def __init__(self, data):
        self.id =  data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM email;"
        results = connectToMySQL('email').query_db(query)
        emails = []
        for row in results:
            emails.append(cls(row))
        return emails

    @classmethod
    def create(cls, data):
        query = "INSERT INTO email (email) VALUES (%(email)s);"
        results = connectToMySQL('email').query_db(query, data)
        return results

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM email WHERE id = %(id)s;"
        return connectToMySQL('email').query_db(query,data)
    
    @staticmethod
    def validate_email(email):
        is_valid = True
        query = "SELECT * FROM email WHERE email = %(email)s;"
        print(email)
        results = connectToMySQL('email').query_db(query, email)
        if not EMAIL_REGEX.match(email['email']):
            flash("Invalid email address!")
            is_valid = False
        return is_valid