
from turtle import Turtle, Screen 

t = Turtle()
t.color("green")
def draw_polygon(sides, angle):
    for i in range(sides):
        t.forward(30)
        t.right(angle)

#triangle 
draw_polygon(3,120)

#square 
draw_polygon(4, 90)

#pentagon
draw_polygon(5, 72)

#hexagon 
draw_polygon(6, 60)

#heptagon
draw_polygon(7, 51.42857)

#octagon 
draw_polygon(8, 45)

#nonagon 
draw_polygon(9, 40)

#decagon
draw_polygon(10, 36)



screen = Screen()

screen.exitonclick()