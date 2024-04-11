from turtle import Turtle
import random
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
WIDTH_OF_SNAKE = 20

class Food(Turtle):

    def __init__(self):
        super().__init__()

        self.spawn_food()
        print(self.position())

    def spawn_food(self):
        self.shape("circle")
        self.color("blue")
        self.shapesize(0.5, 0.5)
        self.penup()
        current_y_position = random.randint(-280, 240)
        current_x_position = random.randint(-280, 280)

        self.goto(current_x_position, current_y_position)
