from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.speed("fastest")
        self.new_position()

    def new_position(self):
        self.randomx = random.randint(-280, 280)
        self.randomy = random.randint(-280, 280)
        self.goto(self.randomx, self.randomy)
