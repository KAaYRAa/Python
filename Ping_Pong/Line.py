from turtle import Turtle, Screen

class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 300)  # Початок по центру екрану (x=0), верх
        self.setheading(270)  # Повернути вниз

    def line(self):
        for _ in range(30):
            self.pendown()
            self.forward(10)  # Малюємо штрих
            self.penup()
            self.forward(10)  # Пропуск



