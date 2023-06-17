# Day 27 - Mile to Km Converter

from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=50, pady=30)

def convert(event=None):
    try:
        miles = float(miles_input.get())
        km = round(miles * 1.609, 2)
        km_result_label.config(text=f"{km}")

    except ValueError:
        print("Please enter a value")

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)
miles_input.bind("<Return>", convert)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=convert)
calculate_button.grid(column=1, row=2)

window.mainloop()