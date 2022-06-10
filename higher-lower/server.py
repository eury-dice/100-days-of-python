from flask import Flask
from random import randint

LOW = 0
HIGH = 9
NUMBERS_GIF = "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"
HIGH_GIF = "https://media.giphy.com/media/wHB67Zkr63UP7RWJsj/giphy.gif"
LOW_GIF = "https://media.giphy.com/media/IevhwxTcTgNlaaim73/giphy.gif"
CORRECT_GIF = "https://media.giphy.com/media/l2YWykMPCmCb9lLWM/giphy.gif"
GIFS = [HIGH_GIF, LOW_GIF, CORRECT_GIF]

app = Flask(__name__)
correct_guess = randint(LOW, HIGH)


# def show_result(function):
#     def wrapper(number):
#         result = function(number)
#         if result == 0:
#             response = "<h1>Too high, try again!</h1>"
#         elif result == 1:
#             response = "<h1>Too low, try again!</h1>"
#         else:
#             response = "<h1>You got it!</h1>"
#
#         return response + f"<img src={GIFS[result]} alt='result.gif'/>"
#     return wrapper


@app.route("/")
def start():
    return f"<h1>Guess a number between {LOW} and {HIGH}</h1>" \
           f"<img src={NUMBERS_GIF} alt='numbers.gif'/>"


@app.route("/<int:number>")
# @show_result
def guess(number):
    if number > correct_guess:
        return f"<h1>Too high, try again!</h1>" \
               f"<img src={HIGH_GIF} alt='result.gif'/>"
    elif number < correct_guess:
        return f"<h1>Too low, try again!</h1>" \
               f"<img src={LOW_GIF} alt='result.gif'/>"
    else:
        return f"<h1>You got it!</h1>" \
               f"<img src={CORRECT_GIF} alt='result.gif'/>"


if __name__ == "__main__":
    app.run(debug=True)
