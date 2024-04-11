from turtle import Turtle, Screen

jimbo = Turtle()
window = Screen()
jimbo.shape("turtle")
jimbo.color("coral")
print(window.screensize())
window.title("hello")
window.bgcolor("aqua")

jimbo.forward(100)
window.exitonclick()
