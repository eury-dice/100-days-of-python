# Etch-A-Sketch

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
ANG = 10
STEP = 10


def go_backward():
    tim.backward(STEP)


def go_forward():
    tim.forward(STEP)


def go_right():
    tim.right(ANG)


def go_left():
    tim.left(ANG)


screen.listen()
screen.onkey(go_forward, "w")
screen.onkey(go_left, "a")
screen.onkey(go_backward, "s")
screen.onkey(go_right, "d")
screen.onkey(tim.reset, "c")
screen.exitonclick()
