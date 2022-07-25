# Imports
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("PyPong")
screen.tracer(0)

# Objects
r_paddle = Paddle((360, 0))
l_paddle = Paddle((-360, 0))
ball = Ball()
scoreboard = Scoreboard()

# Controls
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


# Game initializer
game_on = True

# Run game
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    scoreboard.draw_line()
    
    # Collision parameters
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()
        
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.l_point()
        scoreboard.update_scoreboard()
        
    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.r_point()
        scoreboard.update_scoreboard()


screen.exitonclick()