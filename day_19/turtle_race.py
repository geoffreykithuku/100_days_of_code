from turtle import Turtle, Screen 
import random 

screen = Screen()
colors = ["blue", "green", "red", "purple", "yellow", "orange"]

screen.setup(width=500, height=400)



tim = Turtle(shape="turtle")
tim.penup()
tim.color(colors[0])
tim.goto(x=-230,y=-100)
toki = Turtle(shape="turtle")
toki.penup()
toki.color(colors[1])
toki.goto(x=-230,y=0)
lex = Turtle(shape="turtle") 
lex.penup()
lex.color(colors[2])
lex.goto(x=-230,y=100)


user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
race_on = False
turtles = [tim, lex, toki]
if user_bet:
    race_on = True
    
while race_on:
    for t in turtles:
        if t.xcor() > 230:
            race_on = False
            winning_color = t.pencolor()
            
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} turtle is the winner.")
            else:
                print(f"You lost! The {winning_color} turtle is the winner")
            
        rad_distance = random.randint(0,10)
        t.forward(rad_distance)
        
    
screen.exitonclick()