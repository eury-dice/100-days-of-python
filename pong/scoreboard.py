from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 50, "normal")
SCORE_1_POS = (-100, 200)
SCORE_2_POS = (100, 200)
DEFAULT_COLOR = "white"
WIN_COLOR = "yellow"
WIN_SCORE = 3


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.pu()
        self.color(DEFAULT_COLOR)
        self.l_score = 0
        self.r_score = 0
        self.win_score = WIN_SCORE
        self.update_scores()

    def update_scores(self):
        # For Player 1
        self.goto(SCORE_1_POS)
        if self.l_score == self.win_score:
            self.color(WIN_COLOR)
        self.write(self.l_score, align=ALIGN, font=FONT)
        self.color(DEFAULT_COLOR)

        # For Player 2
        self.goto(SCORE_2_POS)
        if self.r_score == self.win_score:
            self.color(WIN_COLOR)
        self.write(self.r_score, align=ALIGN, font=FONT)
        self.color(DEFAULT_COLOR)

    def add_point(self, player):
        if player == "l":
            self.l_score += 1
        else:
            self.r_score += 1
        self.clear()
        self.update_scores()
