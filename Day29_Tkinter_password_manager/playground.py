from tkinter import *
import pandas

# window = Tk()
#
# b = Label(bg="blue", width=20, height=5)
# b.grid(row=0, column=0, columnspan=1)
#
# g = Label(bg="green", width=20, height=5)
# g.grid(row=1, column=1)
#
# r = Label(bg="blue", width=40, height=5)
# r.grid(row=2, column=0, columnspan=2)
#
# window.mainloop()

dictionary = {
    "website": [1, 2, 3],
    "email": [4, 5, 6],
    "password": [7, 8, 9]
}

frame = pandas.DataFrame(dictionary)
print(frame)