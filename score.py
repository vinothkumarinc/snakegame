from turtle import Turtle

class Score(Turtle):
    def __init__(self, x , y):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.score = 0
        with open("highscore.txt") as file:
            self.highscore = int(file.read())
        self.goto(x, y)

    def reset(self, score):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", mode="w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.printing(self.score)


    def printing(self, sc):
        self.score = sc
        self.clear()
        self.write(f"score: {self.score} Highscore: {self.highscore}", font=("Arial", 15, "normal"))


