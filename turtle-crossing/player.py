from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
SHAPE = "turtle"
UP = 90


class Player(Turtle):
    def __init__(self):
        super().__init__(SHAPE)
        self.pu()
        self.seth(UP)
        self.go_to_start()

    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def at_finish(self):
        return self.ycor() >= FINISH_LINE_Y

    def go_to_start(self):
        self.goto(STARTING_POSITION)