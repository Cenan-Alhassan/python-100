from tkinter import *
window = Tk()

def button_click():
    label.config(text=input_field.get())

window.minsize(width=600, height=500)
label = Label(text="hello world", font=("Arial", 24))
label.grid(column=0, row=0)

button = Button(text="niceuu", command=button_click)
button.grid(column=1, row=2, pady=20)

new_button = Button(text="newwwwwwwwww")
new_button.grid(column=3, row=0)

input_field = Entry(width=10)
input_field.grid(column=4, row=3)


window.mainloop()