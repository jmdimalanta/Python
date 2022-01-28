from flask_app.models.user import User
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Post:
    def __init__(self, data):
        self.id = data ['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.poster = None

    @classmethod
    def create_thought(cls,data):
        query = "INSERT INTO posts(content, user_id) VALUES(%(content)s, %(user_id)s)"
        print(query)
        return connectToMySQL('thoughts').query_db(query, data)


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM posts JOIN users ON user_id = users.id;"
        posts = connectToMySQL('thoughts').query_db(query)
        results = []
        for post in posts:
            print(post)
            a_post = cls(post)
            poster_data = {
                'id' : post['users.id'],
                'first_name' :post['first_name'],
                'last_name' : post['last_name'],
                'email' : post['email'],
                'password' : post['password'],
                'created_at' : post['created_at'],
                'updated_at' : post['updated_at']
            }
            a_post.poster = User(poster_data)
            results.append(cls(post))
        print(results)
        return results

    @classmethod
    def get_user_post(cls,data):
        query = "SELECT * FROM posts WHERE user_id = %(user_id)s"
        posts = connectToMySQL('thoughts').query_db(query,data)
        results = []
        for post in posts:
            results.append(cls(post))
        return results

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM posts WHERE id = %(id)s"
        return connectToMySQL('thoughts').query_db(query, data)

    @staticmethod
    def validate_post(post):
        is_valid = True
        if len(post['content']) < 5:
            flash ("Thought must be at least 5 characters.")
            is_valid = False
        return is_valid
