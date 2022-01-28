import re
from flask import flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.post import Post
from flask import render_template, redirect, session, request, flash

@app.route('/add_thought')
def create():
    data = {
        'id' : session['user_id']
    }
    user = User.get_user(data)
    return render_template('create.html', user = user)

@app.route('/users/<int:user_id>/thought', methods = ['POST'])
def add_thought(user_id):
    if not Post.validate_post(request.form):
        return redirect('/add_thought')
    data = {
        'content' : request.form['content'],
        'user_id' : user_id
    }
    Post.create_thought(data)
    return redirect('/add_thought')

@app.route('/user/<int:user_id>')
def user(user_id):
    if "user_id" not in session:
        return redirect('/')
    user_data = {
        "id" : session["user_id"]
    }
    user = User.get_user(user_data)
    data = {
        'user_id' : user_id
    }
    user_posts = Post.get_user_post(data)
    return render_template('view.html', user = user, user_posts = user_posts)

@app.route ('/delete/<int:user_posts_id>')
def delete(user_posts_id):
    data = {
        'id' : user_posts_id
    }
    Post.destroy(data)
    return redirect('/welcome')

@app.route ('/like')
def like():
    session['count'] += 1
    return redirect('/welcome')

@app.route ('/unlike')
def unlike():
    session['count'] -=1
    return redirect('/welcome')