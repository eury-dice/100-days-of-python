from turtle import Turtle
import time
SHAPE = "circle"
COLOR = "white"
DELAY = 0.3
STEP = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__(SHAPE)
        self.color(COLOR)
        self.pu()
        self.x_step = STEP
        self.y_step = STEP

    def move(self):
        new_x = self.xcor() + self.x_step
        new_y = self.ycor() + self.y_step
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_step *= -1

    def bounce_y(self):
        self.y_step *= -1

    def reset_position(self):
        self.x_step = STEP
        self.y_step = STEP
        time.sleep(DELAY)
        self.goto(0, 0)
        time.sleep(DELAY)
        self.bounce_x()
