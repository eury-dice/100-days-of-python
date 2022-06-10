from flask import Flask
from flask import render_template
from flask import redirect

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/images/<img>")
def images(img):
    return redirect(f"/static/images/{img}")


@app.route("/css/<style>")
def css(style):
    return redirect(f"/static/css/{style}")


if __name__ == "__main__":
    app.run(debug=True)
