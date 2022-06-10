from turtle import Turtle, Screen, colormode
from random import randrange

STEP = 20
DIRECTIONS = (0, 90, 180, 270)

tim = Turtle()
tim.shape("classic")
tim.speed(0)  # "fastest"


def random_color():
    colormode(255)
    r = randrange(0, 256)
    g = randrange(0, 256)
    b = randrange(0, 256)
    color = (r, g, b)
    return color


RAD = 100
ANG = 10


def draw_spirograph(angle, radius):
    for _ in range(0, 360, round(angle)):
        tim.color(random_color())
        tim.circle(radius)
        tim.seth(tim.heading() + angle)


draw_spirograph(ANG, RAD)

screen = Screen()
screen.exitonclick()
