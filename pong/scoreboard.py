from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 50, "normal")
SCORE_1_POS = (-100, 200)
SCORE_2_POS = (100, 200)
COLOR = "white"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.pu()
        self.color(COLOR)
        self.l_score = 0
        self.r_score = 0
        self.update_scores()

    def update_scores(self):
        self.goto(SCORE_1_POS)
        self.write(self.l_score, align=ALIGN, font=FONT)
        self.goto(SCORE_2_POS)
        self.write(self.r_score, align=ALIGN, font=FONT)

    def add_point(self, player):
        if player == "l":
            self.l_score += 1
        else:
            self.r_score += 1
        self.clear()
        self.update_scores()
