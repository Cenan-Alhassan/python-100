from turtle import Turtle, Screen
from threading import Thread
counter = 0
complete_function_runs = 0
list = [0, 0, 0, 0]


screen = Screen()

def fun(dictionary_index):
    global counter
    global complete_function_runs
    global list
    index = (counter + dictionary_index)%len(list)
    list[index] += 1
    print(list)
    counter += 1
    if counter == len(list):
        counter = 0
        complete_function_runs += 1


dic_of_functions = {

    1: fun,
}


def the_function():
    i = 0
    for element in dic_of_functions.values():
        i = i % 2
        element(i)
        print(i)
        i += 1



number_of_functions = 1
def add_function():
    global number_of_functions
    number_of_functions += 1
    dic_of_functions.update({number_of_functions: fun})

screen.listen()
screen.onkeypress(the_function, "q")
screen.onkeypress(add_function, "e")

screen.exitonclick()
