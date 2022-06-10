from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper


def make_italic(function):
    def wrapper():
        return "<i>" + function() + "</i>"
    return wrapper


def make_underline(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper


@app.route("/", endpoint="hello")
@make_bold
def hello():
    return "Hello!"


@app.route("/username/<name>/<int:age>", endpoint="greet")
@make_italic
def greet(name, age):
    return f"Hello, {name}! You're {age} years old, right?"


@app.route("/bye", endpoint="bye")
@make_bold
@make_italic
@make_underline
def bye():
    return "Bye!"


if __name__ == "__main__":
    app.run(debug=True)
