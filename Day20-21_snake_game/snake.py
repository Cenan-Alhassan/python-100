import random
from turtle import Turtle as Block
import time


# TODO 1. make an initial function that creates the next turtle object of 20x20, each turtle is positioned exactly at
#  the end of the turtle in front of it
# a square turtle is 20x20 and the line starts 10 pixels in

# we need to know which direction turtle1 is, set turtle2 at the beginning of its rear end (if turtle1 faces north,
# turtle2 is placed 10 pixels south of it)

# TODO 2.1 set the rotation delay of the next turtle
# You rotate the first block in block_list, and move the whole snake. The first movement will look correct, but then
# they will be set off course.

# The sequence needs to be: rotate block1, move all when move(), rotate block 2, move all when move(), etc

# what we could do is set a rotate_flag that is activated when the first block is rotated.
# when the flag is on, it rotates subsequent blocks every time the move() is called, until it runs through the list

# TODO BUG1. if a rotation happens, and the rotation runs through the whole block list, adding a new block will place
#  the new block in the position before the rotation happened, but only after the rotation finishes
# which means, after the whole rotation finishes, the xcor and ycor of the last block of the list equals its state
# before the rotation happened
# ACTUAL SOLUTION: the issue was that setting xval and yval to 0 at function call did not account for when the snake
# goes off of the origin lines

# TODO 2.2 what to do if rotate again before first rotation runs through all the blocks?
# once a block is out of the list of the original rotation, then it joins the list of the new rotation

# TODO 3. Remake the movement style:
# if we want to move the first segment, segment 2 moves to segment 1, segment 1 moves to 0, and zero does whatever
# it wants
# TODO MEGA. This idea could've been easily realised had you redefined what the word "follow" means. If a problem seems
#  like it won't budge, it's better to re-analise the basics instead going into increasingly convoluted solutions

MOVEMENT_DISTANCE = 20

class Snake:

    def __init__(self):
        self.block_list = []
        self.block = Block("square")
        self.block.color("white")
        self.block.penup()
        self.block_list.append(self.block)

        for _ in range(2):
            self.create_snake_block()

        self.head = self.block_list[0]
        self.head_position = ()

    def create_snake_block(self):

        # DUE TO THE METHOD OF UPDATING POSITIONS, THE NEW BLOCK AUTOMATICALLY GOES TO THE OLD POSITION OF ITS PARENT
        # BLOCK, NO MATTER WHAT THAT POSITION IS. THE SCREEN.UPDATE() HIDES ITS INITIAL POSITION
        # THIS IS A BENEFIT OF ANGELA'S METHOD

        self.block = Block("square")
        self.block.hideturtle()
        self.block.color("white")
        self.block.penup()
        self.block_list.append(self.block)

    def move_forwards(self):

        for i in range(1, len(self.block_list)):
            self.block_list[i].showturtle()
            position_of_block_in_front = self.block_list[-i - 1].position()
            self.block_list[-i].goto(position_of_block_in_front)
        self.head.forward(MOVEMENT_DISTANCE)
        self.head_position = self.head.position()

        # time.sleep(0.1)

    def up(self):
        if self.head.heading() == 270:
            return
        self.head.setheading(90)

    def down(self):
        if self.head.heading() == 90:
            return
        self.head.setheading(270)

    def left(self):
        if self.head.heading() == 0:
            return
        self.head.setheading(180)

    def right(self):
        if self.head.heading() == 180:
            return
        self.head.setheading(0)

