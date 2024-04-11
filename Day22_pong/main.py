# CREATED IN ~3:30 HOURS

from turtle import Turtle, Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
import time

ball_speed = 1
screen = Screen()
screen.bgcolor("black")
screen.setup(width=700, height=500)
screen.tracer(0)

def increase_ball_speed():
    global ball_speed
    ball_speed += 1
    text = Turtle()
    text.hideturtle()
    text.color("white")
    text.goto(50, -220)
    text.write(f"Ball speed set to {round(ball_speed, 1)}x", align="left", font=("Arial", 12, 'bold'))
    time.sleep(0.2)
    text.clear()

def introduction():
    text = Turtle()
    text.hideturtle()
    text.color("white")
    text.goto(0, 30)
    text.write(f"Welcome to Pong!\n\nPlayer 1 controls with w/s\nPlayer 2 controls with up/down"
               f"\n\nTip: press 'E' to increase ball speed",
               align="center", font=("Pixel", 20, 'normal'))
    time.sleep(3)
    text.clear()

def countdown():
    count = Turtle()
    count.hideturtle()
    count.color("white")
    for i in range(3, -1, -1):
        if i == 0:
            count.write(f"GO!", align="center", font=("Arial", 40, 'bold'))
        else:
            count.write(f"{i}", align="center", font=("Arial", 40, 'bold'))
        time.sleep(0.5)
        count.clear()

# chose difficulty and make countdown with controls displayed
def main():
    global ball_speed
    countdown()

    ball = Ball()
    player1 = Paddle(player=1)
    player2 = Paddle(player=2)
    scoreboard1 = Scoreboard(player=1)
    scoreboard2 = Scoreboard(player=2)

    screen.listen()

    screen.onkeypress(player1.move_up, "w")
    screen.onkeypress(player1.move_down, "s")

    screen.onkeypress(player2.move_up, "Up")
    screen.onkeypress(player2.move_down, "Down")

    screen.onkeypress(increase_ball_speed, "q")


    while True:
        print(ball_speed)

        ball.forward(ball_speed)

        if ball.ycor() < -240 or ball.ycor() > 235:
            ball.horizontal_bounce()

        for section in player1.paddle_sections:
            if ball.distance(section["object"]) <= 10:
                ball.setheading(section["angle"])
                ball_speed = round(ball_speed * 1.05, 2)

        for section in player2.paddle_sections:
            if ball.distance(section["object"]) <= 10:
                ball.setheading(180-section["angle"])
                ball_speed = round(ball_speed * 1.05, 2)

        if ball.xcor() > 340:
            time.sleep(0.5)
            ball_speed = 1
            ball.spawn_ball()
            scoreboard2.update_score()
            # ball.spawn_ball()
            # time.sleep(0.3)

        if ball.xcor() < -340:
            time.sleep(0.5)
            ball_speed = 1
            ball.spawn_ball()
            scoreboard1.update_score()
            # ball.spawn_ball()
            # time.sleep(0.3)

        screen.update()


introduction()
main()
