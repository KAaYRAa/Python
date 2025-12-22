from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score import Score

import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
snake=Snake()
food =Food()
score = Score()
level = screen.textinput("Difficulty Level","Which level do you want(easy , medium or hard)?").lower()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
if level == "easy":
    speed=(0.2)
elif level == "medium":
    speed =(0.1)
else:
    speed=(0.05)
while is_game_on:
    time.sleep(speed)
    screen.update()
    snake.move()

    if snake.head.distance(food)<15:
        food.refresh()
        score.increase_score()
        score.update_scoreboard()
        snake.extend()
    if snake.head.xcor()>300 or snake.head.xcor()<-300 or snake.head.ycor()>280 or snake.head.ycor()<-300:
        snake.reset()
        score.reset()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            segment.reset()
            score.reset()






screen.exitonclick()







