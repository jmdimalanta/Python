from flask_app.models.recipe import Recipe
from flask.helpers import flash
from flask_app.models.user import User
from flask_app import app
from flask_app.models.user import User
from flask import render_template, redirect, session, request, flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def login_and_reg():
    return render_template('index.html')

@app.route('/users/register', methods=['POST'])
def register():
    if not User.validate_registration(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"],
        "password" : pw_hash
    }
    user_id = User.create(data)
    session["user_id"] = user_id
    return redirect('/welcome')

@app.route('/users/login', methods=['POST'])
def login():
    if not User.validate_login(request.form):
        return redirect('/')
    data = {
        "email" : request.form["email"]
    }
    user_in_db = User.get_user_by_email(data)
    if not user_in_db:
        flash ("User cannot be found")
        return redirect("/")
    print(user_in_db.password)
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash ("Invalid Email or Password")
        return redirect("/")
    session["user_id"] = user_in_db.id
    return redirect('/welcome')

@app.route('/welcome')
def dashboard():
    if "user_id" not in session:
        return redirect('/')
    data = {
        "id" : session["user_id"]
    }
    user = User.get_user(data)
    recipes = Recipe.get_all()
    return render_template('dashboard.html', user= user, recipes = recipes)

@app.route('/users/<int:user_id>/recipe', methods=["POST"])
def post_recipe(user_id):
    if not Recipe.validate_recipe(request.form):
        return redirect('/add_recipe')
    data = {
        "recipe_name" : request.form["recipe_name"],
        "description" : request.form["description"],
        "instructions" : request.form["instructions"],
        "user_id" : session["user_id"]
    }
    Recipe.add_recipe(data)
    return redirect("/welcome")

@app.route('/recipes/update/<int:recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    data = {
        "id" : recipe_id,
        "recipe_name" : request.form["recipe_name"],
        "description" : request.form["description"],
        "instructions" : request.form["instructions"],
        "user_id" : session["user_id"]
    }
    print(data)
    Recipe.update_recipe(data)
    return redirect("/welcome")

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')