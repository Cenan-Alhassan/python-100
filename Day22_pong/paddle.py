# The racket will be a set of 5 turtle objects in a list
# They can be initialised either on the left or right side of the screen

# when calling the move function, all 5 objects will move in unison up or down within the y bounds of the screen

# each of the 5 will be assigned a bounce angle through a list of dictionaries system

# in the main file, when the ball detects collision with any of the 5 objects (as keys of the dictionary of that index),
# the ball's heading will be updated with the value of the object it collided with
# by calling the ball.paddle_bounce(arg) function



from turtle import Turtle

BOUNCE_ANGLES = [45, 20, 0, -20, -45]
SPEED = 20
UPPER_BOUND = 235
LOWER_BOUND = -220

class Paddle:
    def __init__(self, player):
        self.paddle_sections = []
        self.create_paddle_sections()

        if player == 1:
            self.player_position(1)
        else:
            self.player_position(2)

        self.head = self.paddle_sections[0]["object"]
        self.bottom = self.paddle_sections[4]["object"]

    def create_paddle_sections(self):
        for angle in BOUNCE_ANGLES:
            section = Turtle("square")
            section.color("white")
            section.penup()
            section.right(90)
            section.shapesize(0.5, 0.7)  # square with dimension of 14x10 pixels
            print(section.shapesize())
            self.paddle_sections.append({"object": section, "angle": angle})

    def player_position(self, player):
        if player == 1:  # change x coordinate if player 1 or 2
            xcor = -330
        else:
            xcor = 325
        i = 0
        for dictionary in self.paddle_sections:
            dictionary["object"].goto(xcor, 28-i)  # loops through objects of dictionary and sets x coordinates
            i += 14

    def move_up(self):
        if self.head.ycor() >= UPPER_BOUND:
            return

        for dictionary in self.paddle_sections:
            dictionary["object"].setheading(90)

        self.move()

    def move_down(self):
        if self.bottom.ycor() <= LOWER_BOUND:
            return

        for dictionary in self.paddle_sections:
            dictionary["object"].setheading(270)  # sets all headings down

        self.move()

    def move(self):
        for dictionary in self.paddle_sections:
            dictionary["object"].forward(SPEED)

