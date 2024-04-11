import turtle
from turtle import Turtle, Screen
import random


def draw_a_square(self):
    for _ in range(4):
        self.dotted(self, 100)
        self.right(90)


def random_rgb_tuple():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b



# if length is 100, penup for 10 pen down for 10 until 100
def dotted_line(self, length):
    for _ in range(int(length/10)):
        self.forward(5)
        self.penup()
        self.forward(5)
        self.pendown()


def all_shapes(self, n_of_shapes):
    screen.colormode(255)  # needed in order to use rgb values in turtle.color()
    for i in range(3, n_of_shapes+3):
        self.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        for _ in range(i):
            self.forward(100)
            self.right(360 / i)


def random_walk(self):
    """To make a random walk, the turtle rotates right randomly between 0 and 4 times, and moves forwards"""
    self.hideturtle()
    self.speed(12)
    self.width(8)
    colors = ["coral", "tomato", "orange red", "red", "crimson"]
    turtle.colormode(255)
    while True:
        walk_rotation = random.randint(0, 3)
        for _ in range(walk_rotation):
            self.pencolor(random_rgb_tuple())
            self.right(90)
        self.forward(15)


def spirograph(self):
    jimm.hideturtle()
    turtle.colormode(255)
    self.speed("fastest")
    for _ in range(72):
        self.pencolor(random_rgb_tuple())
        self.circle(100)
        self.right(5)


screen = Screen()
jimm = Turtle()
jimm.square = draw_a_square
jimm.dotted = dotted_line
jimm.all_shapes = all_shapes
jimm.random_walk = random_walk
jimm.spirograph = spirograph
jimm.shape("turtle")
jimm.color("blue", "red")
jimm.speed("fastest")
jimm.hideturtle()

import colorgram

turtle.colormode(255)

colors = colorgram.extract('autumn_cat.jpg', 20)
rgb_tuples = []
for color in colors:
    named_tuple = (color.rgb[0], color.rgb[1], color.rgb[2])
    rgb_tuples.append(named_tuple)

screen.setup(570, 550)

for i in range(0, 500, 50):
    jimm.penup()
    jimm.setposition(-280, -230+i)
    for _ in range(10):
        jimm.forward(50)
        jimm.dot(20, random.choice(rgb_tuples))

print(jimm.position())
screen.exitonclick()

