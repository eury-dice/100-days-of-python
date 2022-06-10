from tkinter import *

PAD_X = 20
PAD_Y = 10
WIN_PAD = 30
WIDTH = 100
HEIGHT = 70
MILE_TO_KM = 1.60934


def calculate_km():
    km = float(miles_input.get()) * MILE_TO_KM
    converted_label.config(text=f"{km: 0.4f}")


window = Tk()
window.minsize(width=WIDTH, height=HEIGHT)
window.title("Mile to Km Converter")
window.config(padx=WIN_PAD, pady=WIN_PAD)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)
miles_input.insert(END, 0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
miles_label.config(padx=PAD_X, pady=PAD_Y)

equals_label = Label(text="is equal to")
equals_label.grid(column=0, row=1)
equals_label.config(padx=PAD_X, pady=PAD_Y)

converted_label = Label(text="0")
converted_label.grid(column=1, row=1)
converted_label.config(padx=PAD_X, pady=PAD_Y)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)
km_label.config(padx=PAD_X, pady=PAD_Y)

calc_button = Button(text="Calculate", command=calculate_km)
calc_button.grid(column=1, row=2)
calc_button.config(padx=PAD_X, pady=PAD_Y)

window.mainloop()
