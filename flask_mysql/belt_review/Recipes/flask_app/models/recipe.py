from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.recipe_name = data['recipe_name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def add_recipe(cls, data):
        query = "INSERT INTO recipes (recipe_name, description, instructions, user_id) VALUES (%(recipe_name)s, %(description)s, %(instructions)s, %(user_id)s);"
        return connectToMySQL ('recipes').query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes JOIN users ON user_id = users.id"
        recipes = connectToMySQL('recipes').query_db(query)
        results = []
        for recipe in recipes:
            results.append(cls(recipe))
        print(results)
        return results

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        results = connectToMySQL('recipes').query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def update_recipe(cls, data):
        query = "UPDATE recipes SET recipe_name = %(recipe_name)s, description = %(description)s, instructions = %(instructions)s, user_id = %(user_id)s WHERE id = %(id)s;"
        print (query)
        return connectToMySQL('recipes').query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s"
        return connectToMySQL('recipes').query_db(query,data)
    
    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        if len(recipe['recipe_name']) < 3:
            flash ('Name must be at least 3 characters.')
            is_valid = False
        if len(recipe['description']) < 3:
            flash ('Description must be at least 3 characters')
            is_valid = False
        if len(recipe['instructions']) < 3:
            flash ('Instructions must be at least 3 characters')
            is_valid = False
        return is_valid

