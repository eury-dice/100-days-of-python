# ---------------------------- Imports ----------------------------
from tkinter import *
from tkinter import messagebox
import pandas
import random

# ---------------------------- Constants ----------------------------
PAD = 50
BACKGROUND_COLOR = "#B1DDC6"
LANG_FILE = "./data/french_words.csv"
SAVE_FILE = "./data/words_to_learn.csv"
CARD_BACK = "./images/card_back.png"
CARD_FRONT = "./images/card_front.png"
RIGHT_IMG = "./images/right.png"
WRONG_IMG = "./images/wrong.png"
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 526
ORIG_TEXT_COLOR = "black"
FLIP_TEXT_COLOR = "white"
LANG_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")
LANG_POS = (400, 150)
WORD_POS = (400, 263)
CARD_POS = (400, 263)
LANG1 = "French"
LANG2 = "English"

# ---------------------------- Extract .csv  ----------------------------
try:
    df_words = pandas.read_csv(SAVE_FILE)
    print("Loading saved words.")
except FileNotFoundError:
    df_words = pandas.read_csv(LANG_FILE)
finally:
    to_learn = df_words.to_dict(orient="records")


# ---------------------------- Flip card  ----------------------------
def flip_card():
    right_button["state"] = "normal"
    wrong_button["state"] = "normal"
    canvas.itemconfig(card_img, image=card_back_img)
    canvas.itemconfig(lang_text, text=LANG2, fill=FLIP_TEXT_COLOR)
    canvas.itemconfig(word_text, text=current_card[LANG2], fill=FLIP_TEXT_COLOR)


# ---------------------------- Get next word  ----------------------------
def next_card():
    global current_card

    right_button["state"] = "disabled"
    wrong_button["state"] = "disabled"
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_img, image=card_front_img)
    canvas.itemconfig(lang_text, text=LANG1, fill=ORIG_TEXT_COLOR)
    canvas.itemconfig(word_text, text=current_card[LANG1], fill=ORIG_TEXT_COLOR)
    window.after(3000, flip_card)


# ---------------------------- Remove card  ----------------------------
def remove_card():
    global to_learn
    to_learn.remove(current_card)
    if len(to_learn) == 0:
        messagebox.showinfo(title="Well Done",
                            message="You have gone through all the words, congratulations! "
                                    "The words will now be reset.")
        df = pandas.read_csv(LANG_FILE)
        to_learn = df.to_dict(orient="records")
    pandas.DataFrame(to_learn).to_csv(SAVE_FILE, index=False)
    next_card()


# ---------------------------- UI ----------------------------
current_card = {}

window = Tk()
window.config(padx=PAD, pady=PAD)
window.config(bg=BACKGROUND_COLOR)
window.title("Flashy")

card_front_img = PhotoImage(file=CARD_FRONT)
card_back_img = PhotoImage(file=CARD_BACK)

canvas = Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=BACKGROUND_COLOR, highlightthickness=0)
card_img = canvas.create_image(CARD_POS, image=card_front_img)
lang_text = canvas.create_text(LANG_POS, text="Language", font=LANG_FONT)
word_text = canvas.create_text(WORD_POS, text="Word", font=WORD_FONT)
canvas.grid(column=0, row=0, columnspan=2)


# Buttons
right_img = PhotoImage(file=RIGHT_IMG)
wrong_img = PhotoImage(file=WRONG_IMG)

right_button = Button(image=right_img, highlightthickness=0, bd=0, command=remove_card)
right_button.grid(column=1, row=1)

wrong_button = Button(image=wrong_img, highlightthickness=0, bd=0, command=next_card)
wrong_button.grid(column=0, row=1)

next_card()

# Loop
window.mainloop()
