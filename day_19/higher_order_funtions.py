from turtle import Turtle, Screen


t = Turtle()

def move_forwards():
    t.forward(10)

def move_backwards():
    t.backward(10)

def move_clockwise():
    t.right(10)

def move_counter():
    t.left(10)

def clear_screen():
    t.clear()
    t.reset()
def lift_pen():
    t.penup()
    
def pen_down():
    t.pendown()
screen = Screen()
screen.listen()

screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="a", fun=move_counter)
screen.onkey(key="c", fun=clear_screen)
screen.onkey(key="x", fun=lift_pen)
screen.onkey(key="z", fun=pen_down)

screen.exitonclick()