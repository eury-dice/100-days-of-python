from flask import Flask, render_template
from datetime import datetime
import requests
import random

GENDERIZE_API = "https://api.genderize.io"
AGIFY_API = "https://api.agify.io"
BLOGS_API = "https://api.npoint.io/5abcca6f4e39b4955965"

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    year = datetime.now().year
    return render_template("index.html", num=random_number, year=year)


@app.route("/guess/<name>")
def guess(name):
    params = {
        "name": name,
    }

    gender = requests.get(url=GENDERIZE_API, params=params).json()["gender"]
    age = requests.get(url=AGIFY_API, params=params).json()["age"]
    name_title = name.title()

    return render_template("guess.html", name=name_title, gender=gender, age=age)


@app.route("/blog")
def get_blog():
    all_blogs = requests.get(BLOGS_API).json()
    return render_template("blog.html", blogs=all_blogs)


if __name__ == "__main__":
    app.run(debug=True)
