# initialising the class creates two score (Turtle) objects on the left and right hand sides of the dotted line
# The objects are invisible, and they write their own score attributes
# if ball hits the right side of the screen, player_2_score += 1 and score_2 writes the number
from turtle import Turtle

POSITION = 80
class Scoreboard(Turtle):
    def __init__(self, player):
        super().__init__()
        self.dotted_line()

        if player == 1:
            self.position = POSITION
        else:
            self.position = -POSITION

        self.player_score = 0

        self.hideturtle()
        self.goto(self.position, 180)
        self.color("white")
        self.write(f"{self.player_score}", align="center",  font=("Arial", 40, 'bold'))

    def update_score(self):
        self.player_score += 1
        self.clear()
        self.write(f"{self.player_score}", align="center",  font=("Arial", 40, 'bold'))
    def dotted_line(self):
        line = Turtle()
        line.penup()
        line.goto(0, -400)
        line.setheading(90)
        line.pencolor("white")
        line.pensize(width=3)
        for i in range(30):
            line.pendown()
            line.forward(15)
            line.penup()
            line.forward(15)