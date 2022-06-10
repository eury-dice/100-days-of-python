from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1#25
SHORT_BREAK_MIN = 1#5
LONG_BREAK_MIN = 1#20

reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps

    work_secs = 60 * WORK_MIN
    short_break_secs = 60 * SHORT_BREAK_MIN
    long_break_secs = 60 * LONG_BREAK_MIN

    if reps % 2 == 0:
        count_down(work_secs)
        timer_label.config(text="Work", fg=GREEN)
    elif reps != 7:
        count_down(short_break_secs)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(long_break_secs)
        timer_label.config(text="Break", fg=RED)
    reps += 1
    window.bell()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = int(count / 60)
    seconds = count % 60
    time_left = f"{minutes:02d}:{seconds:02d}"
    canvas.itemconfig(timer_text, text=time_left)
    global timer
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        if reps % 2 == 0 and reps != 0:
            new_text = check_label.cget("text") + "✔"
            check_label.config(text=new_text)
        if 8 > reps > 0:
            start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=3)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=3)

check_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
check_label.grid(column=1, row=4)

window.mainloop()
