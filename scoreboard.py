from turtle import Turtle

class ScoreBoard(Turtle):

    #creating scoreboard
    score = -1
    def __init__(self):
        super().__init__()
        self.color("Red")
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        self.new_score()
    
    #updating scoreboard
    def new_score(self):    
        self.score += 1
        self.clear()
        self.write(f"Level = {self.score}",align = "Center",font = ("Arial",24,"bold"))
    
    #displaying gameover
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("GAME OVER!!",align = "Center",font = ("Arial",50,"bold"))
        self.goto(0,-50)
        self.write(f"Max Level = {self.score}",align = "Center",font = ("Arial",25,"bold"))
        