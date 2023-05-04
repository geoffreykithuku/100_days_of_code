from turtle import Turtle, Screen 
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Python Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard= Scoreboard()

screen.listen()

screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")
game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()
    
    #Detect food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()
        
    
    
for part in snake.snake_body:
    
    if part == snake.head:
        pass
    elif snake.head.distance(part) < 10:
            game_on = False
            scoreboard.game_over()
    
    
        

screen.exitonclick()