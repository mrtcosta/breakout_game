from turtle import Turtle

score = 0

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()


    def scores(self):
        global score

        score += 1

        self.clear()
        self.penup()
        self.color("white")
        self.goto(250, 260)
        self.write(f"Points: {score}", False, "center", font=("Courier", 20, "normal"))
        self.hideturtle()

    def game_over(self):
        self.goto(0, 100)
        self.write("GAME OVER", False, "center", font=("Courier", 24, "bold"))