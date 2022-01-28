from logging import debug
from flask import Flask

app = Flask (__name__)

@app.route("/")
def greetings():
    return "Hello World!"

@app.route("/dojo")
def dojo():
    return "Dojo"

@app.route("/say/<name>")
def hello(name):
    return f"Hi {name}!"

@app.route("/<int:num>/<name>")
def repeating(num, name):
    return f"{num * name}"

if __name__=="__main__":
    app.run(debug = True)
