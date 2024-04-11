import random
from turtle import Turtle as Block
from turtle import Screen
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

screen = Screen()
screen.bgcolor("black")
block_list = []

block = Block(shape="turtle")
block.color("white")
block_list.append(block)
screen.tracer(0)

flag = True
colors = ["white", "red", "blue"]

def create_snake_block():
    global block
    global block_list
    xval, yval = 0, 0
    heading = block.heading()
    print(heading)
    print(block.xcor(), block.ycor())

    if heading == 90.00:
        yval = block.ycor()-20
        xval = block.xcor()

    elif heading == 0.00:
        xval = block.xcor()-20
        yval = block.ycor()

    elif heading == 180.00:
        xval = block.xcor()+20
        yval = block.ycor()

    elif heading == 270.00:
        yval = block.ycor()+20
        xval = block.xcor()

    block = Block("turtle")
    block.color(random.choice(colors))
    block.setheading(heading)
    block.goto(xval, yval)
    block_list.append(block)
    screen.update()


def move_forwards():
    global flag
    block_list[0].forward(20)
    for i in range(1, len(block_list)):
        block_list[i].forward(20)
    check_rotation()


    screen.update()
    # time.sleep(0.1)




def manual_rotate():
    global flag
    block_list[0].right(90)

    screen.update()


def check_rotation():
    already_rotated = False
    for i in range(1, len(block_list)):
        if not already_rotated:
            current_heading = block_list[i].heading()
            previous_heading = block_list[i-1].heading()

            if current_heading != previous_heading:
                block_list[i].setheading(previous_heading)
                print(i)
                already_rotated = True


    screen.update()




for _ in range(4):
    create_snake_block()


screen.listen()
screen.onkeypress(move_forwards, "w")
screen.onkeypress(manual_rotate, "d")
screen.onkeypress(create_snake_block, "q")



screen.exitonclick()