from flask.helpers import flash
from flask_app.models.user import User
from flask_app.models.post import Post
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
    if 'count' not in session:
        session['count'] = 0
    data = {
        "id" : session["user_id"]
    }
    user = User.get_user(data)
    posts = Post.get_all()
    return render_template('dashboard.html', user= user, posts = posts)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')