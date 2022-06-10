from turtle import Turtle

FONT = ("Courier", 20, "normal")
SCORE_POS = (-280, 260)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.pu()
        self.level = 0
        self.game_over = False
        self.goto(SCORE_POS)
        self.update_level()

    def update_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def show_end_screen(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
