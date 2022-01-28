from flask_app.models.user import User
from flask import render_template, request, redirect
from flask_app import app

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    return render_template("users.html", users = User.get_all())

@app.route('/user/new')
def new():
    return render_template('users.html')

@app.route('user/create', methods = ['post'])
def create():
    print(request.form)
    User.create_users(request.form)
    return redirect('/users')

