from flask import Flask, render_template, redirect, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from forms import RatingForm, MovieForm
from os import environ
import requests

API_KEY = environ["MOVIE_API_KEY"]
SEARCH_API = environ["SEARCH_MOVIE_API_ENDPOINT"]
FIND_API = environ["FIND_MOVIE_API_ENDPOINT"]
IMAGE_URL = environ["MOVIE_IMAGE_URL"]

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///top-movies-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)
db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String(500))
    img_url = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f'<Movie {self.title}>'


db.create_all()


@app.route("/")
def home():
    movies = db.session.query(Movie).order_by(Movie.rating).all()
    for i in range(len(movies)):
        movies[i].ranking = len(movies) - i
    db.session.commit()

    movies = db.session.query(Movie).filter(Movie.ranking < 11).order_by(Movie.ranking.desc()).all()
    return render_template("index.html", movies=movies)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    form = RatingForm()

    if form.validate_on_submit():
        movie.rating = request.form['rating']
        movie.review = request.form['review']
        db.session.commit()
        return redirect('/')
    else:
        return render_template("edit.html", form=form, movie=movie)


@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()

    return redirect("/")


@app.route("/add", methods=["GET", "POST"])
def add():
    form = MovieForm()
    if form.validate_on_submit():
        params = {
            "api_key": API_KEY,
            "query": request.form['title'],
        }
        response = requests.get(url=SEARCH_API, params=params)
        response.raise_for_status()
        movie_results = response.json()["results"]
        return render_template("select.html", movies=movie_results)
    else:
        return render_template("add.html", form=form)


@app.route("/find")
def find():
    movie_id = request.args.get("id")
    find_endpoint = FIND_API + movie_id
    params = {
        "api_key": API_KEY
    }
    response = requests.get(url=find_endpoint, params=params)
    response.raise_for_status()
    movie = response.json()
    year = movie['release_date'].split("-")[0]
    img_url = IMAGE_URL + movie["poster_path"]
    new_movie = Movie(title=movie["title"],
                      year=year,
                      description=movie["overview"],
                      img_url=img_url,
                      )
    db.session.add(new_movie)
    db.session.commit()
    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)
