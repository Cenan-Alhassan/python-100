from turtle import Turtle, Screen


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.score = 0
        self.hideturtle()
        self.penup()
        self.sety(250)
        self.color("white")
        self.write(f"Score: {self.score}", align="center", font=('Times_new_roman', 20, 'bold'))



    def update_score(self):

        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=('Times_new_roman', 20, 'bold'))

    def game_over(self):
        self.goto(0, 75)
        self.write(f"GAME OVER", align="center", font=('Times_new_roman', 20, 'bold'))