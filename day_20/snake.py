from turtle import Turtle

#startng positions 

START_POSITIONS = [(0,0), (-20, 0), (-40,0)] 
DISTANCE = 20

RIGHT = 0
LEFT  = 180
UP = 90
DOWN = 270

class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]
        
    def create_snake(self):
        for pos in START_POSITIONS:
            self.add_part(pos)
        
           
            
    def add_part(self, pos):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(pos)
        self.snake_body.append(snake)
        
    def extend(self):     
         self.add_part(self.snake_body[-1].position())
         
         
         
            
    def move(self):
        self.snake_body[0].forward(DISTANCE)
        for part_num in range(len(self.snake_body) - 1 , 0, -1):
            new_x = self.snake_body[part_num - 1].xcor()
            new_y = self.snake_body[part_num - 1].ycor()
            self.snake_body[part_num].goto(new_x, new_y)
    def up(self):
        if self.head.heading() != DOWN:
            
            self.head.setheading(UP)
    def down(self):
          if self.head.heading() != UP:
             self.head.setheading(DOWN)
    def left(self):
          if self.head.heading() != RIGHT:
             self.head.setheading(LEFT)
        
    def right(self):
          if self.head.heading() != LEFT:
             self.head.setheading(RIGHT)
                                
  