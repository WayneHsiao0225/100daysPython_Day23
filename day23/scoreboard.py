from turtle import Turtle
FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.hideturtle()
        self.penup()
        self.goto(180,250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write("Level:" + str(self.level) + "", align="left", font=FONT)

    def score_up(self):
        self.level+=1
        self.update_scoreboard()
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over !!!",align="center", font=FONT)



