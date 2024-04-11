
# create position function:
# if y height is 400: 50 from both sides, left 300
# if 5 turtles, first turtle at height 150, second at 150-300/5, etc
import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
jim = Turtle()
him = Turtle()
gim = Turtle()
fim = Turtle()
screen = Screen()
screen.setup(width=500, height=400)
turtle.colormode(255)


def position(*args):
    i = 0
    turtle_list = []
    for turtle in args:
        turtle.shape("turtle")
        turtle.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        turtle.penup()
        turtle.goto(x=-230, y=100-i)
        i += 200/(len(args)-1)
        turtle_list.append(turtle)
    return turtle_list


bet = screen.textinput("bet", "hello")
turtle_list = position(tim, jim, him, gim, fim)

race = True

while race:

    for turtle in turtle_list:
        turtle.forward(random.randint(0, 10))

        if turtle.xcor() >= 230:
            print(turtle_list.index(turtle))
            exit()
screen.exitonclick()