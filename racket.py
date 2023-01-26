from turtle import Turtle
import random

class Racket:

    def __init__(self):
        self.segments_racket = []
        self.create_racket()
        self.racket1 = self.segments_racket[0]


    def create_racket(self):

        for racket in range(1):
            racket = Turtle()
            racket.penup()
            racket.shape("square")
            racket.color("white")
            racket.shapesize(1, 5)
            racket.goto(random.randint(-250, 250), -250)
            self.segments_racket.append(racket)

    def left(self):
        new_x = self.racket1.xcor() - 30
        self.racket1.goto(new_x, self.racket1.ycor())

    def right(self):
        new_x = self.racket1.xcor() + 30
        self.racket1.goto(new_x, self.racket1.ycor())

