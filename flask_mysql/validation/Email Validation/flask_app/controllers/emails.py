from flask_app.models.email import Email
from flask_app import app
from flask import render_template, request, redirect

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/create/email', methods = ['POST'])
def create_email():
    if not Email.validate_email(request.form):
        return redirect('/')
    Email.create(request.form)
    return redirect('/success')

@app.route('/success')
def results():
    email = Email.get_all()
    return render_template('success.html', email = email)

@app.route('/destroy/<int:id>')
def destroy_email(id):
    data = {
        'id' : id
    }
    Email.destroy(data)
    return redirect ('/success')