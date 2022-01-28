from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self, db_data):
        self.id = db_data ['id']
        self.first_name = db_data ['first_name']
        self.last_name = db_data ['last_name']
        self.email = db_data ['email']
        self.created_at = db_data ['created_at']
        self.updated_at = db_data ['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users').query_db(query)
        users = []
        for u in results:
            users.append(cls(u))
        return users

    @classmethod
    def create_users(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        result = connectToMySQL('users').query_db(query, data)
        return result