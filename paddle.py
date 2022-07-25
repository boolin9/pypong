# Imports
from turtle import Turtle, width


# Paddle class
class Paddle(Turtle):
    
    
    # Initialize paddle
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(4, 1)
        self.pu()
        self.goto(position)
        
        
    # Paddle functions
    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
                
                
    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)