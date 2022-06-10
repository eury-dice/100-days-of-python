from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.pu()
        self.color("yellow")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.refresh()

    def clear(self):
        self.reset()
        self.__init__()

    def refresh(self):
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 260)
        self.goto(rand_x, rand_y)
