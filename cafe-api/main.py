from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import BadRequestKeyError
import random

API_KEY = "TopSecretAPIKey"

app = Flask(__name__)

# # Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# # Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


# TODO: HTTP GET - Read Record
@app.route("/random")
def get_random_cafe():
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)

    return jsonify(cafe=random_cafe.to_dict()), 200


@app.route("/all")
def get_all_cafes():
    cafes = db.session.query(Cafe).all()
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes]), 200


@app.route("/search")
def search_cafes():
    loc = request.args["loc"]
    cafes = db.session.query(Cafe).filter(Cafe.location.ilike(f"%{loc}%")).all()

    if cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in cafes])
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe in that location."}), 404


# TODO: HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_cafe():
    try:
        name = request.form["name"]
        map_url = request.form["mapUrl"]
        img_url = request.form["imgUrl"]
        location = request.form["loc"]
        seats = request.form["seats"]
        has_toilet = bool(request.form["hasToilet"])
        has_wifi = bool(request.form["hasWifi"])
        has_sockets = bool(request.form["hasSockets"])
        can_take_calls = bool(request.form["canTakeCalls"])
    except BadRequestKeyError:
        return jsonify(error={"Missing Key": "Key/s needed by request is/are missing."}), 404
    else:
        try:
            coffee_price = request.form["coffeePrice"]
        except BadRequestKeyError:
            coffee_price = ""
        finally:
            new_cafe = Cafe(
                name=name,
                map_url=map_url,
                img_url=img_url,
                location=location,
                seats=seats,
                has_toilet=has_toilet,
                has_wifi=has_wifi,
                has_sockets=has_sockets,
                can_take_calls=can_take_calls,
                coffee_price=coffee_price,
            )
            db.session.add(new_cafe)
            db.session.commit()

            return jsonify({"success": "Successfully added the new cafe."}), 200


# TODO: HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    cafe = Cafe.query.get(cafe_id)
    if cafe:
        cafe.coffee_price = request.args["coffeePrice"]
        db.session.commit()
        return jsonify({"success": "Successfully updated the price."}), 200
    else:
        return jsonify(error={"Not Found": "Sorry, a cafe with that id was not found in the database."}), 404


# TODO: HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    if request.args["api_key"] != API_KEY:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403
    else:
        cafe = Cafe.query.get(cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted cafe from the database."}), 200
        else:
            return jsonify(error={"Not Found": "Sorry, a cafe with that id was not found in the database."}), 404


if __name__ == '__main__':
    app.run(debug=True)
