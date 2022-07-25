# Imports
from turtle import Turtle


# Scoreboard class
class Scoreboard(Turtle):
    
    
    # Initalize scoreboard
    def __init__(self):
            super().__init__()
            # self.draw_line()
            self.color('white')
            self.pu()
            self.hideturtle()
            self.l_score = 0
            self.r_score = 0
            self.update_scoreboard()
                
    
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=('Bit5x3', 80, 'normal'))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=('Bit5x3', 80, 'normal'))
        self.draw_line()
        
                
    def l_point(self):
        self.l_score += 1
        
        
    def r_point(self):
        self.r_score += 1
        
        
    def draw_line(self):
        self.goto(0, 300)
        self.setheading(270)
        for _ in range(30):
            self.pd()
            self.fd(10)
            self.pu()
            self.fd(10)