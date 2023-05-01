from turtle import Turtle, Screen 

t = Turtle()
t.color("blue")
def draw_dashed_line():
    for i in range(10):
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()

draw_dashed_line()

screen = Screen()
screen.exitonclick()