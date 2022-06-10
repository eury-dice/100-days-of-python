from turtle import Turtle
SHAPE = "square"

STRETCH_WID = 5
STRETCH_LEN = 1
COLOR = "white"
STEP = 20


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__(SHAPE)
        self.shapesize(stretch_wid=STRETCH_WID, stretch_len=STRETCH_LEN)
        self.pu()
        self.color(COLOR)
        self.goto(pos)

    def up(self):
        new_y = self.ycor() + STEP
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - STEP
        self.goto(self.xcor(), new_y)
