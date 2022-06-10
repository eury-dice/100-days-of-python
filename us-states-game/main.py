import pandas as pd
import turtle

IMG_PATH = "blank_states_img.gif"
STATES_CSV_PATH = "50_states.csv"
FONT = ("Arial", 10, "normal")
WIDTH = 725
HEIGHT = 500

screen = turtle.Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.title("U.S. States Game")

screen.addshape(IMG_PATH)
turtle.shape(IMG_PATH)

df_states = pd.read_csv(STATES_CSV_PATH)
correct_state = turtle.Turtle()
correct_state.pu()
correct_state.ht()


def write_state(guessed_state, df, state_obj):
    state_details = df[df["state"] == guessed_state]
    position = (int(state_details.x), int(state_details.y))
    state_obj.goto(position)
    state_obj.write(guessed_state, align="center", font=FONT)


def write_remaining_states(df, state_obj, states, sc):
    state_obj.color("red")
    state_details = df[~df.state.isin(states)]
    for remaining_state in state_details.state:
        write_state(remaining_state, df, state_obj)
    sc.update()


states_guessed = []
game_on = True
while game_on:
    if len(states_guessed) < 50:
        answer_state = screen.textinput(title=f"{len(states_guessed)}/50 States Correct",
                                        prompt="What's another state's name?")
    if answer_state is None:
        game_on = False
        screen.tracer(0)
        write_remaining_states(df_states, correct_state, states_guessed, screen)
    elif (answer_state.title() in df_states.values) and (answer_state.title() not in states_guessed):
        states_guessed.append(answer_state.title())
        write_state(answer_state.title(), df_states, correct_state)

screen.exitonclick()
