from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.high_score_reader("score.txt")
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score:{self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_sc(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.high_score_writer("score.txt", self.high_score)
        self.score = 0
        self.update_scoreboard()

    def high_score_reader(self, file:str):
        with open(file, "r") as f:
            return int(f.read())
    
    def high_score_writer(self, file:str, inpt):
        with open(file, "w") as f:
            f.write(str(inpt))
    
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
