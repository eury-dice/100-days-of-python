# For getting color scheme
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
#
# print(rgb_colors)

from turtle import Turtle, Screen, colormode
from random import choice

# colors extracted using colorgram
color_list = [
    (245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50),
    (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73),
    (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158),
    (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129),
    (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)
]

SIZE = 20
STEP = 50

x_pos = -250
y_pos = -220

tim = Turtle()
tim.hideturtle()
tim.speed("fast")
colormode(255)
tim.pu()

for _ in range(10):
    tim.setpos(x_pos, y_pos)
    for _ in range(10):
        tim.pd()
        tim.dot(SIZE, choice(color_list))
        tim.pu()
        tim.fd(STEP)
    y_pos += STEP

screen = Screen()
screen.exitonclick()
