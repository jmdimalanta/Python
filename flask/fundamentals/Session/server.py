from flask import Flask, render_template, request,redirect, session
app = Flask(__name__)
app.secret_key = "counting counter" #set secret key for security purposes.

@app.route("/")
def index():
    if "count" not in session:
        session["count"] = 1
    else:
        session["count"] += 1
    return render_template("index.html")

@app.route("/counter", methods = ["POST"])
def sessionCounter():
    if request.form["click"] == "add":
        session["count"] += 1
    elif request.form["delete"] == "reset":
        session["count"] = 0
    return redirect("/")

@app.route("/destroy")
def sessionDestroy():
    session.clear()
    return redirect("/")

if __name__== "__main__":
    app.run(debug=True)