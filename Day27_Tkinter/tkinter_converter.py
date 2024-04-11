from tkinter import *


def miles_to_km():
    number = int(text_box.get())
    converted_number = str(round(number * 1.60934, 2))
    text_converted_number.config(text=converted_number)

window = Tk()
window.minsize(height=100, width=200)
window.config(pady=15, padx=15)

text_is_equal_to = Label(text="is equal to")
text_is_equal_to.grid(column=0, row=1, padx=10)

text_converted_number = Label(text="0")
text_converted_number.grid(column=1, row=1, padx=20)

text_miles = Label(text="Miles")
text_miles.grid(column=2, row=0, padx=10)

text_km = Label(text="Km")
text_km.grid(column=2, row=1, padx=10)

text_box = Entry(width=10)
text_box.grid(column=1, row=0, pady=10)

button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2, pady=1)

window.mainloop()