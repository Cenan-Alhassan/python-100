from tkinter import *
from playsound import *
import winsound
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25 * 60
SHORT_BREAK_MIN = 25 * 60
LONG_BREAK_MIN = 20 * 60
timer_functional = None
reps = 0
SPEED = 1000
FREQ = 2000
DUR = 200


def set_checkmarks(reps_p):
    checkmarks = ["✔" for number in range(0, reps_p, 2)]  # adds a ✔ every 2 reps
    checkmarks = "".join(element for element in checkmarks)  # joins into a string

    checkmark_label.config(text=checkmarks)

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    window.after_cancel(timer_functional)
    canvas.itemconfig(timer, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    reps = 0
    set_checkmarks(reps)

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_countdown():
    """calls the function that reduces the second by 1, passes different seconds depending on number of repetitions"""
    global reps
    reps += 1

    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)
    winsound.Beep(FREQ, DUR)


    if reps in (1, 3, 5, 7):
        timer_label.config(text="Work", fg=GREEN)
        countdown(WORK_MIN)
    elif reps in (2, 4, 6):
        timer_label.config(text="Break", fg=PINK)
        countdown(SHORT_BREAK_MIN)
    elif reps == 8:
        timer_label.config(text="Break", fg=RED)
        reps = 0
        countdown(LONG_BREAK_MIN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(seconds):
    """takes a number of seconds, subtracts one, and displays it on canvas text object in 0:00 format"""
    global reps
    global timer_functional
    get_minutes = int(seconds / 60)
    remaining_seconds = seconds % 60

    canvas.itemconfig(timer, text=f"{get_minutes}:{'0' if remaining_seconds < 10 else ''}{remaining_seconds}")

    if seconds > 0:  # call itself if seconds still > 0
        timer_functional = window.after(SPEED, countdown, seconds-1)

    else:  # starts countdown again if equals zero

        set_checkmarks(reps)

        start_countdown()

# ---------------------------- UI SETUP ------------------------------- #


def printt():
    print("hello")
    # pady = window.winfo_height() - 224
    # padx = window.winfo_width() - 200
    # print(pady, padx)
    # window.config(pady=pady/2, padx=padx/2, bg=YELLOW)


window = Tk()
window.title("Pomodoro")
window.config(pady=50, padx=100, bg=YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=2, row=1)

start_button = Button(text="Start", command=start_countdown)
start_button.grid(column=1, row=3)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=3, row=3)

tomato_png = PhotoImage(file="tomato.png")
canvas = Canvas(height=250, width=224, bg=YELLOW, highlightbackground=YELLOW)

checkmark_label = Label(text="", font=(FONT_NAME, 25), fg=GREEN, bg=YELLOW)
checkmark_label.grid(column=2, row=4)

# tomato image
canvas.create_image((112, 120), image=tomato_png)
# countdown text
timer = canvas.create_text((112, 145), text="00:00", fill="white", font=(FONT_NAME, 24, "bold"))


canvas.grid(column=2, row=2)


window.mainloop()