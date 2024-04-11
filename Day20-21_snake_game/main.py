from turtle import Turtle as Block
from turtle import Screen
from snake import Snake
from food import Food
import time
from scoreboard import Scoreboard

game = True
# we have 0 written in the file. High score is that.
# if the scoreboard.score is bigger than the score in the file, write that score

def main():
    global game

    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Za Snake")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()


    def high_scores():

        with open("./high_score.text", mode="r") as file:
            current_high_score = int(file.read())
            if scoreboard.score > current_high_score:
                print("yay")

                with open("high_score.text", mode="w") as file:
                    file.write(str(scoreboard.score))

        score = Block()
        score.hideturtle()
        score.penup()
        score.sety(252)
        score.setx(-280)
        score.color("white")
        score.write(f"High score: {current_high_score}", font=('Times_new_roman', 12, 'bold'))

    high_scores()

    def food_safe_spawn():  # spawns outside the snake's body
        food.hideturtle()
        food.spawn_food()
        for segments in snake.block_list:
            if food.distance(segments) < 10:
                food_safe_spawn()
        food.showturtle()

    def game_is_lost():
        time.sleep(1)
        screen.clear()
        main()




    screen.listen()

    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.create_snake_block, "e")

    while game:
        screen.update()
        time.sleep(0.05)
        snake.move_forwards()

        if snake.head.distance(food) < 15:
            food_safe_spawn()
            snake.create_snake_block()
            scoreboard.update_score()

        bound = snake.head.position()

        # check to see if snake.head is out of bounds (collision with wall)
        if -300 > bound[0] or 280 < bound[0] or -300 > bound[1] or 280 < bound[1]:
            high_scores()
            scoreboard.game_over()
            game_is_lost()

        # loop through snake segments to see if the distance between it and snake.head is < 10 (collision with self)
        for segment in snake.block_list[1:]:
            if snake.head.distance(segment) < 10:
                game_is_lost()

    screen.exitonclick()


main()
