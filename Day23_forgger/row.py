# each row object creates a row of turtles that moves across the screen from right to left or other way round
# a row is initialised by giving a y coordinate


# each row can have the following attributes:
# How many there are (random range according to difficulty)
# use to calculate distance between each turtle knowing turtle length
# their speed
# their color

# a row spawns out of bounds and spawns another when it hits the left of the screen
# no matter the number, the turtles must fill the full width of the screen
#  when row1 hits the left of the screen, spawn row2. When row2 does, spawn row1 (in main)

from turtle import Turtle
import random

SCREEN_WIDTH = 600

# coefficients multiply the standard 20x20 size
WIDTH_COEFFICIENT = 1.5
LENGTH_COEFFICIENT = 3


class Row:
    def __init__(self, ycor, speed, objects_per_screen):
        self.ycor = ycor
        self.speed = speed
        self.objects_per_screen = objects_per_screen

        self.row1_list = self.create_row()
        self.row2_list = self.create_row()
        self.car_length = LENGTH_COEFFICIENT * 20
        self.car_width = WIDTH_COEFFICIENT * 20
        self.out_of_bounds = SCREEN_WIDTH/2 + self.car_length/2


        # The two rows move together at first, then they split

        self.spawn_row(self.row1_list)
        self.spawn_row(self.row2_list)

    def create_row(self):
        row_list = []
        for i in range(self.objects_per_screen):
            car = Turtle("square")
            car.color("white")
            car.penup()
            car.shapesize(stretch_len=LENGTH_COEFFICIENT, stretch_wid=WIDTH_COEFFICIENT)
            car.setheading(180)
            row_list.append(car)
        return row_list



    def spawn_row(self, object_list):
        number_of_cars = len(object_list)
        gap_length = ( SCREEN_WIDTH - (self.car_length*number_of_cars) )/number_of_cars
        gap_and_car_length = gap_length + self.car_length

        # print(number_of_cars, gap_length, gap_and_car_length, self.out_of_bounds)

        i = 0
        for car in object_list:
            car.goto((self.out_of_bounds + gap_and_car_length * i), self.ycor)
            print(car.position())
            i += 1

    def move_row(self):
        for car in self.row1_list:
            car.forward(self.speed)

        for car in self.row2_list:
            car.forward(self.speed)
