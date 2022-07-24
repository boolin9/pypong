# Imports
from turtle import Turtle, Screen
from paddle import Paddle

# Screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("PyPong")
screen.tracer(0)


# Objects
r_paddle = Paddle((360, 0))
l_paddle = Paddle((-360, 0))
# ball = Ball()
# scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


# Game initializer
game_on = True

# Run game
while game_on:
    screen.update()
## Collisions


screen.exitonclick()