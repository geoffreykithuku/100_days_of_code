from turtle import Turtle, Screen 


timmy = Turtle()

timmy.shape("turtle")
timmy.color("red")



def draw_square():
    for i in range(4):
        timmy.forward(100)
        timmy.right(90)
    


draw_square()

timmy.hideturtle()

screen = Screen()

screen.exitonclick()