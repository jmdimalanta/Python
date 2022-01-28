import re
from flask import flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask import render_template, redirect, session, request, flash

@app.route('/add_recipe')
def create_recipe():
    data = {
        "id" : session["user_id"]
    }
    user = User.get_user(data)
    return render_template('create.html', user = user)

@app.route('/recipes/edit/<int:user_id>')
def edit(user_id):
    data ={
        'id' : user_id
    }
    one_recipe = Recipe.get_one(data)
    user = User.get_user(data)
    return render_template('edit_recipe.html', recipe = user_id, user = user)

@app.route('/recipes/show/<int:recipe_id>')
def show(recipe_id):
    data ={
        'id' : recipe_id
    }
    one_recipe = Recipe.get_one(data)
    user = User.get_user(data)
    return render_template('view.html', recipe = one_recipe, user =user)

@app.route('/recipes/destroy/<int:recipe_id>')
def delete(recipe_id):
    data = {
        'id' : recipe_id
    }
    Recipe.delete(data)
    return redirect('/welcome')