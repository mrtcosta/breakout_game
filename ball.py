from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.goto(random.randint(-290, 290), -240)
        self.color("white")

    def move(self, dir_x, dir_y):
        new_x = self.xcor() + (10 * dir_x)
        new_y = self.ycor() + (10 * dir_y)
        self.goto(new_x, new_y)
