# The ball object is a turtle object with a specific size. it bounces when a collision condition is met.
# The bounce functions calculate different headings for a vertical and horizontal bounce


from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(0.7, 0.7)

        self.spawn_ball()
        self.current_heading = self.heading()

    def spawn_ball(self):
        self.goto(0, 0)
        random_heading = [random.randint(-45, 45), random.randint(135, 225)]

        self.setheading(random.choice(random_heading))

    def horizontal_bounce(self):
        new_heading = 360 - self.heading()
        self.setheading(new_heading)

    def vertical_bounce(self):
        new_heading = 180 - self.heading()
        self.setheading(new_heading)