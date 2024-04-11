import random
import time
from turtle import Turtle, Screen
from row import Row
from frog import Frog
from level_count import LevelCount

screen = Screen()
screen.bgcolor("black")
screen.tracer(0)
screen.setup(width=600, height=600)

# we have easy, medium and hard difficulties
# we can have a dictionary for each difficulty containing keys for speed and n of objects
# we then have a list of these dictionaries
# make a function that chooses a random difficulty for speed, but then chooses from the other two for n of objects

HARD = {
    "speed": 15,
    "objects_per_screen": 5
}

MEDIUM = {
    "speed": 12,
    "objects_per_screen": 4
}

EASY = {
    "speed": 10,
    "objects_per_screen": 3
}

DIFFICULTY = [HARD, MEDIUM, EASY]


def choose_difficulty():
    speed_difficulty = random.choice(DIFFICULTY)
    object_difficulty = random.choice(DIFFICULTY)

    same = True
    while same:
        if object_difficulty == speed_difficulty:
            object_difficulty = random.choice(DIFFICULTY)
        else:
            same = False

    return speed_difficulty["speed"], object_difficulty["objects_per_screen"]


def clear_screen(row_list):
    for row in row_list:
        for object in row.row1_list:
            object.color(screen.bgcolor())
            del object
        for object in row.row2_list:
            object.color(screen.bgcolor())
            del object


def level_creator(ycor_first_row, ycor_last_row):
    """Create a number of rows by giving the y coordinate of the first and last row. Must be multiples of 40"""
    list_of_rows = []

    for i in range(ycor_first_row, ycor_last_row-1, -40):
        speed, object_number = choose_difficulty()
        row1 = Row(ycor=i, speed=speed, objects_per_screen=object_number)

        list_of_rows.append(row1)

    return list_of_rows


def move_forward():
    global frog_can_move
    if frog_can_move:
        frog.move_forward()


# list of levels starting at level 1 at index 0
level_list = [level_creator(ycor_first_row=40, ycor_last_row=-40), level_creator(80, -40),
              level_creator(80, -80), level_creator(120, -80), level_creator(120, -120), level_creator(160, -120)]

counter = LevelCount()
frog = Frog()
screen.listen()

screen.onkey(move_forward, "w")
screen.onkey(frog.move_backward, "s")
screen.onkeypress(frog.shimmy_right, "d")
screen.onkeypress(frog.shimmy_left, "a")

for level in level_list:
    frog_can_move = False
    row_list = level

    counter.update_level(level=level_list.index(level)+1, final_level=len(level_list))

    still_playing = True
    while still_playing:
        screen.update()
        time.sleep(0.1)

        for row in row_list:
            row.move_row()

        if frog.ycor() > row_list[0].row1_list[0].ycor() + 50: # win level
            frog.goto(0, -280)
            still_playing = False

        for row in row_list:
            for object in row.row1_list:
                if frog.distance(object) < 30:
                    time.sleep(0.5)
                    frog.goto(0, -280)

            for object in row.row2_list:
                if frog.distance(object) < 30:
                    time.sleep(0.5)
                    frog.goto(0, -280)

            if -299 > row.row1_list[0].xcor() > -309:  # accounts for when the row's speed won't equal 300 exactly
                row.spawn_row(row.row2_list)
            if -299 > row.row2_list[0].xcor() > -309:
                row.spawn_row(row.row1_list)

        if -299 > row_list[-1].row1_list[0].xcor() > -309:
            frog_can_move = True

    clear_screen(row_list)
