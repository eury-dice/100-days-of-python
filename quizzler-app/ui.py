from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
WIN_PAD = 20
CANVAS_PAD = 50
CANVAS_WIDTH = 300
CANVAS_HEIGHT = 250
QUESTION_LOC = (150, 125)
LABEL_FONT = ("Arial", 12, "normal")
Q_FONT = ("Arial", 20, "italic")
Q_TEXT_WIDTH = 280
TRUE_IMG = "./images/true.png"
FALSE_IMG = "./images/false.png"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=WIN_PAD, pady=WIN_PAD, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {self.quiz.score}",
                                 bg=THEME_COLOR,
                                 fg="white",
                                 font=LABEL_FONT)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
        self.question_text = self.canvas.create_text(QUESTION_LOC,
                                                     width=Q_TEXT_WIDTH,
                                                     text="Some Question Text",
                                                     font=Q_FONT,
                                                     fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=CANVAS_PAD)

        true_img = PhotoImage(file=TRUE_IMG)
        self.true_button = Button(image=true_img,
                                  highlightthickness=0,
                                  command=lambda: self.check_answer("True"))
        self.true_button.grid(column=0, row=2)

        false_img = PhotoImage(file=FALSE_IMG)
        self.false_button = Button(image=false_img,
                                   highlightthickness=0,
                                   command=lambda: self.check_answer("False"))
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.true_button.config(state="normal")
            self.false_button.config(state="normal")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f"You've reached the end of the quiz. "
                                        f"You got {self.quiz.score}/{self.quiz.question_number}!")

    def check_answer(self, answer: str):
        if self.quiz.check_answer(answer):
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
        self.window.after(1000, self.update)

    def update(self):
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.get_next_question()
