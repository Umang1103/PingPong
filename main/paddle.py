from turtle import Turtle


class Paddle(Turtle):

    def __init__(self,pos):
        super().__init__()
        self.pu()
        self.speed("fastest")
        self.goto(pos)
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=6,stretch_len=1)
    
    def up(self):
        if self.ycor() < 230:
            self.goto(self.xcor(),self.ycor()+30)

    def down(self):
        if self.ycor() > -230:
            self.goto(self.xcor(),self.ycor()-30)

            
    