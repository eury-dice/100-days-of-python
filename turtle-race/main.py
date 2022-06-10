from turtle import Turtle, Screen
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

is_race_on = True
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color: ")

while user_bet not in COLORS:
    user_bet = screen.textinput(title="Make your bet!",
                                prompt="Choose only among red, orange, yellow, green, blue, purple: ").lower()


x_pos = -230
y_pos = -80
gap = 30

turtles = []

for ind in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.pu()
    new_turtle.color(COLORS[ind])
    new_turtle.goto(x_pos, y_pos)
    turtles.append(new_turtle)
    y_pos += gap

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle was the winner.")
            else:
                print(f"You've lost! The {winning_color} turtle was the winner.")

        rand_distance = randint(0, 10)
        turtle.forward(rand_distance)
