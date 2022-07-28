from turtle import Turtle
FONT = ("Arial",10, "normal")
class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self._score = 0
        self.highscore = 0
        self.hideturtle()
        self.penup()
        self.goto(0,280)
        self.speed("fastest")
        self.write(f"Score:{self._score}",align="center",font=FONT)
        
        
    def update_sc(self):
        self.clear()
        self.write(f"Score:{self._score}",align="center",font=FONT)
    
    def high_score_reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
    
    def yemYuttu(self):
        self._score+=1
        self.update_sc()
        
    def gameOver(self):
        self.goto(0,0)
        self.write(f"GAME OVER!",align="center",font=FONT)
        