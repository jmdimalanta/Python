from logging import debug
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", vertical = 8, horizontal = 8)

@app.route("/<num>")
def smaller(num):
    return render_template("index.html", vertical = 8, horizontal = int(num))

@app.route("/<num1>/<num2>")
def verticalDown(num1,num2):
    return render_template("index.html", vertical = int(num1), horizontal = int(num2))

@app.route("/<num1>/<num2>/<col1>/<col2>")
def alternatingColors(num1, num2, col1, col2):
    return render_template("index.html", vertical = int(num1), horizontal = int(num2), col1 =col1, col2 = col2)

if __name__ == "__main__":
    app.run(debug = True)