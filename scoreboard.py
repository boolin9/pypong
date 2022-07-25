# Imports
from turtle import Turtle


# Scoreboard class
class Scoreboard(Turtle):
    
    
    # Initalize scoreboard
    def __init__(self):
            super().__init__()
            self.draw_line()


    # Scoreboard functions
    def draw_line(self):
            self.goto(0, 300)
            self.setheading(270)
            self.color('white')
            for _ in range(30):
                self.pd()
                self.fd(10)
                self.pu()
                self.fd(10)