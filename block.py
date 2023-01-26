from turtle import Turtle


class Blocks():

    def __init__(self):
        self.blocks = []

    def create_blocks(self, X, Y):
        new_block = Turtle('square')
        new_block.shapesize(stretch_wid=1, stretch_len=2)
        new_block.penup()
        new_block.color("white")
        new_block.goto(X, Y)
        self.blocks.append(new_block)