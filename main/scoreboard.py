from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self,pos):
        super().__init__()
        self.pu()
        self.ht()
        self.goto(pos)
        self.color("white")
        self.score = 0
        self.write(f"{self.score}", move=False, align="center", font=("Courier",50,"normal"))

    def shooter(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", move=False, align="center", font=("Courier",50,"normal"))

        