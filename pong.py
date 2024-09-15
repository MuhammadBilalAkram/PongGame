from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

sc = Screen()

sc.bgcolor("black")
sc.setup(width=800, height=600)
sc.title("Pong Game")
sc.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
scoreboard = Scoreboard()

ball = Ball()
sc.listen()
sc.onkey(r_paddle.up,"Up")
sc.onkey(r_paddle.down,"Down")
sc.onkey(l_paddle.up,"w")
sc.onkey(l_paddle.down,"s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    sc.update()
    ball.move()

    #detect the colision with top and bottum walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    #detect colision with the Both paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() >320 or ball.distance(l_paddle) < 50 and ball.xcor() > -320:
       ball.bounce_x()

    #Detect Right Paddle Miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    
    #detect left paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


sc.exitonclick()