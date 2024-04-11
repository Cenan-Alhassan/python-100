from turtle import Turtle

class LevelCount(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-260, 250)
        self.color("white")

    def update_level(self, level, final_level):
        self.clear()
        self.write(f"Level {level}/{final_level}", align="left",  font=("Arial", 15, 'bold'))