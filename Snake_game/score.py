from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score =0
        with open("/Users/admin/PycharmProjects/Snake_game/data") as data:
            content = data.read()
            self.high_score = int(content) if content.strip().isdigit() else 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"score is {self.score} ; The high score is {self.high_score}", align='center', font=("Arial", 20, "bold"))

    def reset(self):
        if self.score>self.high_score:
            self.high_score = self.score
            with open("/Users/admin/PycharmProjects/Snake_game/data" , mode="w") as data:
                data.write(f"{self.high_score}")

        self.score=0
        self.update_scoreboard()


    def increase_score(self):
        self.score+=1
        self.update_scoreboard()

