from turtle import Turtle

# create a simple turtle that moves forward by 20 onkey and shimmies to the side onkeypress

class Frog(Turtle):
    def __init__(self):
        super().__init__()

        self.setheading(90)
        self.shape("turtle")
        self.color("white")
        self.shapesize(1.5, 1.5)
        self.penup()
        self.goto(0, -280)

    def move_forward(self):

        print("hello")
        self.forward(40)

    def move_backward(self):
        if self.ycor() <= -280:
            return
        print("hello")
        self.back(40)

    def shimmy_right(self):
        if self.xcor() >= 300:
            return
        self.goto(self.xcor() + 20, self.ycor())

    def shimmy_left(self):
        if self.xcor() <= -300:
            return
        self.goto(self.xcor() - 20, self.ycor())
