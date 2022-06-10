from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
SHAPE = "square"
CAR_COUNT = 25
CAR_WIDTH = 1
CAR_LENGTH = 2
X_MIN = -280
X_MAX = 600
Y_MIN = -250
Y_MAX = 250
X_LOOP_POINT = -340
X_UPPER_LOOP = 500
X_LOWER_LOOP = 320


class CarManager:
    def __init__(self):
        self.car_speed = STARTING_MOVE_DISTANCE
        self.cars = []
        self.car_number = CAR_COUNT
        self.generate_cars()

    def generate_cars(self):
        for _ in range(self.car_number):
            car = Turtle(SHAPE)
            car.pu()
            car.shapesize(stretch_wid=CAR_WIDTH, stretch_len=CAR_LENGTH)
            car.color(random.choice(COLORS))
            x_cor = random.randint(X_MIN, X_MAX)
            y_cor = random.randint(Y_MIN, Y_MAX)
            car.goto(x_cor, y_cor)
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            new_x = car.xcor() - self.car_speed
            new_y = car.ycor()
            if new_x < X_LOOP_POINT:
                new_x = random.randint(X_LOWER_LOOP, X_UPPER_LOOP)
                new_y = random.randint(Y_MIN, Y_MAX)
            car.goto(new_x, new_y)

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT
