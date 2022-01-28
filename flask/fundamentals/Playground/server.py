from flask import Flask, render_template

app = Flask(__name__)

@app.route("/play")
def home():
    return render_template("index.html")

@app.route("/play/<number_of_boxes>")
def block_repeat(number_of_boxes):
    repeat = (int(number_of_boxes))
    return render_template("index2.html", repeat = repeat)

@app.route("/play/<number_of_boxes>/<color_change>")
def box_change(number_of_boxes, color_change):
    repeat = (int(number_of_boxes))
    color_change = color_change
    return render_template("index3.html",repeat = repeat, colorChange= color_change)


if __name__=="__main__":
    app.run(debug=True)