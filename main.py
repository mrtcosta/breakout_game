import time
from turtle import Screen
from racket import Racket
from ball import Ball
from block import Blocks
from scoreboard import Scoreboard



# creating screen
screen = Screen()
screen.bgcolor('black')
screen.setup(height=600, width=700)
screen.title("Breakout Game")
screen.tracer(0)

# variables
racket = Racket()
ball = Ball()
blocks = Blocks()
score = Scoreboard()

# waiting for arrows' click
screen.listen()
screen.onkeypress(racket.left, "Left")
screen.onkeypress(racket.right, "Right")

is_on = True

# import setting to be used during the game
x_ball = 1
y_ball = 1
time_speed = 0.1
lines_of_blocks = {'first': (310, 0),
                   "second": (320, 22),
                   "third": (310, 44),
                   "fourth": (320, 66),
                   "fifth": (310, 88)}

# creating the blocks
for line in lines_of_blocks:
    x_block = lines_of_blocks[line][0]
    y_block = lines_of_blocks[line][1]
    for block in range(0, 16):
        blocks.create_blocks(x_block, y_block)
        x_block -= 42

while is_on:
    screen.update()
    time.sleep(time_speed)
    ball.move(x_ball, y_ball)

    # setting the area where the ball is able to go around
    if ball.xcor() > 330 or ball.xcor() < -340:
        x_ball *= -1
        ball.move(x_ball, y_ball)

    if ball.ycor() > 290:
        y_ball *= -1
        ball.move(x_ball, y_ball)

    # making the ball turn around when touching the racket
    if racket.racket1.ycor() + 5 <= ball.ycor() <= racket.racket1.ycor() + 10 and racket.racket1.xcor() - 50 <= ball.xcor() <= racket.racket1.xcor() + 50:
        y_ball *= -1
        time_speed *= 0.75
        ball.move(x_ball, y_ball)

    elif ball.ycor() < racket.racket1.ycor() - 20:
        score.game_over()
        is_on = False

    # check if the ball hits any block and then delete it
    for block in blocks.blocks:
        if block.distance(ball) < 20:
            y_ball *= -1
            ball.move(x_ball, y_ball)
            blocks.blocks.remove(block)
            block.reset()
            time_speed *= 0.9
            score.scores()


        # tried to do something more accurate
        # if block.xcor() + 5 <= ball.xcor() <= block.xcor() + 10 and block.ycor() - 10 <= ball.ycor() <= block.ycor() + 10:
        #     x_ball *= -1
        #     ball.move(x_ball, y_ball)
        #     blocks.blocks.remove(block)
        #     block.reset()
        #     # time_speed *= 0.9
        #
        # if block.xcor() - 20 <= ball.xcor() <= block.xcor() + 20 and block.ycor() - 10 <= ball.ycor() <= block.ycor() - 8 \
        #         or block.ycor() + 8 <= ball.ycor() <= block.ycor() + 10:
        #     y_ball *= -1
        #     ball.move(x_ball, y_ball)
        #     blocks.blocks.remove(block)
        #     block.reset()
        #     # time_speed *= 0.9



screen.exitonclick()
