from turtle import Turtle
POSITION = (0, 275)
ALIGN = "center"
FONT = ("Courier", 16, "normal")
COLOR = "white"
CENTER = (0, 0)
HIGH_SCORE_FILE = "high_score.txt"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        with open(HIGH_SCORE_FILE) as file:
            self.high_score = int(file.read())
        self.score = 0
        self.create_scoreboard()

    def zero(self):
        self.clear()
        self.score = 0
        self.create_scoreboard()

    def create_scoreboard(self):
        self.ht()
        self.pu()
        self.color(COLOR)
        self.goto(POSITION)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}\tHigh Score: {self.high_score}", align=ALIGN, font=FONT)

    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(HIGH_SCORE_FILE, "w") as file:
                file.write(f"{self.high_score}")
        self.update_score()
        self.goto(CENTER)
        self.color("red")
        self.write("GAME OVER", align=ALIGN, font=FONT)

    def add_point(self):
        self.score += 1
        self.update_score()
