
from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake game")

my_snake = Snake()
food = Food()
heading = Score(-40, 280)

# tracer is used to switch off the screen
screen.tracer(0)

screen.listen()
screen.onkey(my_snake.up, "Up")
screen.onkey(my_snake.down, "Down")
screen.onkey(my_snake.right, "Right")
screen.onkey(my_snake.left, "Left")



my_score = 0
speed = 0.5
is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(speed)
    my_snake.move()

    # detect collission with food
    heading.printing(my_score)

    if my_snake.head.distance(food) < 15:
        my_score += 1
        food.new_position()
        my_snake.add_snake()
        speed -= 0.02

    # if u touch boundary, it will reset the game
    if my_snake.head.xcor() > 280 or my_snake.head.xcor() < -280 or my_snake.head.ycor() > 280 or my_snake.head.ycor() <- 280:
        heading.reset(my_score)
        my_snake.snake_reset()
        my_score = 0

    # highscore mod for touching the body
    result = my_snake.touching_body()
    if result == True:
        heading.reset(my_score)
        my_snake.snake_reset()
        my_score = 0


screen.exitonclick()
