from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

WIDTH = 800
HEIGHT = 600
COLOR = "black"
TITLE = "pong"
PADDLE1_POS = (350, 0)
PADDLE2_POS = (-350, 0)
Y_MAX = 280
Y_MIN = -280
X_MAX = 380
X_MIN = -380
X_PAD_MAX = 320
X_PAD_MIN = -320
PADDLE_DIST = 50
DEF_DELAY = 0.06
MIN_DELAY = 0.01

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor(COLOR)
screen.title(TITLE)
screen.tracer(0)

r_paddle = Paddle(PADDLE1_POS)
l_paddle = Paddle(PADDLE2_POS)
ball = Ball()
sb = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

game_on = True
delay = 0.07
while game_on:
    time.sleep(delay)
    screen.update()
    ball.move()
    if (ball.ycor() >= Y_MAX) or (ball.ycor() <= Y_MIN):
        ball.bounce_y()

    if ((ball.distance(r_paddle) < PADDLE_DIST) and ball.xcor() > X_PAD_MAX) or \
            ((ball.distance(l_paddle) < PADDLE_DIST) and ball.xcor() < X_PAD_MIN):
        ball.bounce_x()
        if delay > MIN_DELAY:
            delay -= 0.005

    if ball.xcor() > X_MAX:
        ball.reset_position()
        delay = DEF_DELAY
        sb.add_point("l")

    if ball.xcor() < X_MIN:
        ball.reset_position()
        delay = DEF_DELAY
        sb.add_point("r")

screen.exitonclick()
