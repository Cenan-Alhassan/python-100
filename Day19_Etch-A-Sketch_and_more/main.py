from turtle import Turtle, Screen
import keyboard

jimm = Turtle(shape="square")
screen = Screen()


def forw():
    jimm.forward(10)
    print(jimm.heading())


def back():
    jimm.back(10)

def rotate_right():
    jimm.right(5)


def rotate_left():
    jimm.left(5)


def clear_screen():
    screen.resetscreen()


def circle_anti_clockwise():
    for _ in range(36):
        jimm.circle(100, 10)
        if keyboard.is_pressed('w'):
            return


def circle_clockwise():
    jimm.setheading(180)
    for _ in range(36):
        jimm.circle(100, -10)
        if keyboard.is_pressed('w'):
            return


screen.listen()
screen.onkeypress(fun=forw, key="w")
screen.onkeypress(rotate_right, "d")
screen.onkeypress(back, "s")
screen.onkeypress(rotate_left, "a")
screen.onkeypress(clear_screen, "c")
screen.onkeypress(circle_anti_clockwise, "Right")
screen.onkeypress(circle_clockwise, "Left")


screen.exitonclick()