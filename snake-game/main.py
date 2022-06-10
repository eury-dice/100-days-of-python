from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


COLL_DIST = 15
MAX_X = 290
MAX_Y = 290
MIN_X = -290
MIN_Y = -290
SCREEN_COLOR = "black"
DEFAULT_SPEED = 0.1
MIN_SPEED = 0.03

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor(SCREEN_COLOR)
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
sb = ScoreBoard()


def show_pause_menu():
    global game_is_on
    game_is_on = False
    choice = screen.numinput("Play Again?", "[1] Resume Game\n[2] New Game\n[3] Exit Game", 1, 1, 3)
    if choice == 1:
        game_is_on = True
        enable_keypress(screen)
    elif choice == 2:
        reset_game()
        game_is_on = True


def show_end_menu():
    choice = screen.numinput("Play Again?", "[1] Play Snake\n[2] Exit Game", 1, 1, 2)
    if choice == 1:
        reset_game()
        return True
    else:
        return False


def enable_keypress(sc):
    sc.listen()
    sc.onkey(snake.up, "Up")
    sc.onkey(snake.down, "Down")
    sc.onkey(snake.left, "Left")
    sc.onkey(snake.right, "Right")
    sc.onkey(show_pause_menu, "m")


enable_keypress(screen)

game_is_on = True
snake_speed = DEFAULT_SPEED


def reset_game():
    snake.clear()
    food.clear()
    sb.zero()
    enable_keypress(screen)
    global snake_speed
    snake_speed = DEFAULT_SPEED


while game_is_on:
    screen.update()
    time.sleep(snake_speed)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < COLL_DIST:
        food.refresh()
        snake.grow()
        sb.add_point()
        if sb.score % 5 == 0 and snake_speed > MIN_SPEED:
            snake_speed -= 0.01

    # Detect collision with wall
    if snake.head.xcor() > MAX_X or snake.head.xcor() < MIN_X or snake.head.ycor() > MAX_Y or snake.head.ycor() < MIN_Y:
        sb.game_over()
        game_is_on = show_end_menu()

    # Detection collision with actual snake
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            sb.game_over()
            game_is_on = show_end_menu()
            break
