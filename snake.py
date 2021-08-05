from turtle import Turtle, Screen

screen = Screen()


class Snake:

    def __init__(self):
        # a default coordinates is to create 3 objects using the newsnake object
        self.all_body = []
        self.position = [(0, 0), (-20, 0), (-40, 0)]
        self.initiate_snake()
        self.head = self.all_body[0]

    def initiate_snake(self):
        for coord in self.position:
            body = Turtle(shape="square")
            body.color("white")
            body.penup()
            self.all_body.append(body)
            body.goto(coord)

    def move(self):
        # idea is moving the last item in the snake body to the last but previous coordinate, if last os 5,
        # then 5 will go
        # to 4th spot and 4 will go to 3 and so on

        for items in range(len(self.all_body)-1, 0, -1):
            xcor = self.all_body[items - 1].xcor()
            ycor = self.all_body[items - 1].ycor()
            self.all_body[items].showturtle()
            self.all_body[items].goto(xcor, ycor)
        self.head.forward(20)

    def add_snake(self):
        # this function is called when the snake touches the food
        body = Turtle(shape="square")
        body.hideturtle()
        body.color("white")
        body.penup()
        self.all_body.append(body)

    def touching_body(self):

        # if the coordinate of the head is touching the coordinate of any of the body in the list, then game over
        # the loop starts with 1 to avoid counting head
        for items in range(1, len(self.all_body)-1):
            if self.head.distance(self.all_body[items]) < 5:
                return True

    def snake_reset(self):
        for seg in self.all_body:
            seg.goto(1000, -1000)
        self.all_body.clear()
        self.position = [(0, 0), (-20, 0), (-40, 0)]
        self.initiate_snake()
        self.head = self.all_body[0]

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

