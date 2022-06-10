from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
DIRECTIONS = {"right": 0, "up": 90, "left":  180, "down": 270}
SHAPE = "square"
COLOR = "white"


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def clear(self):
        for segment in self.segments:
            segment.reset()
        self.__init__()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle(SHAPE)
        segment.color(COLOR)
        segment.pu()
        segment.goto(position)
        self.segments.append(segment)

    def move(self):
        snake_length = len(self.segments) - 1
        for i in range(snake_length, 0, -1):
            prev_pos = self.segments[i - 1].pos()
            self.segments[i].goto(prev_pos)
        self.head.forward(MOVE_DISTANCE)

    def grow(self):
        self.add_segment(self.segments[-1].pos())

    # snake head dictates turning
    def up(self):
        if self.head.heading() != DIRECTIONS["down"]:
            self.head.setheading(DIRECTIONS["up"])

    def down(self):
        if self.head.heading() != DIRECTIONS["up"]:
            self.head.setheading(DIRECTIONS["down"])

    def left(self):
        if self.head.heading() != DIRECTIONS["right"]:
            self.head.setheading(DIRECTIONS["left"])

    def right(self):
        if self.head.heading() != DIRECTIONS["left"]:
            self.head.setheading(DIRECTIONS["right"])
