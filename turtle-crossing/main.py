import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

COLLISION_RANGE = 15

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
turtle = Player()
scoreboard = Scoreboard()
car_man = CarManager()
screen.listen()
screen.onkeypress(turtle.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_man.move_cars()

    for car in car_man.cars:
        if turtle.distance(car) < COLLISION_RANGE:
            scoreboard.show_end_screen()
            game_is_on = False
            break

    if turtle.at_finish():
        turtle.go_to_start()
        scoreboard.update_level()
        car_man.speed_up()

screen.exitonclick()
