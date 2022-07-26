# Imports
from turtle import Turtle
import random


# Ball class
class Ball(Turtle):
    
    
    # Initialize class
    def __init__(self):
        super().__init__()
        self.pu()
        self.shape('square')
        self.shapesize(0.7, 0.7)
        self.color('white')
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.08

    
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    
    
    def bounce_y(self):
        self.y_move *= -1
        
        
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9
        
    
    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.08
        self.bounce_x()