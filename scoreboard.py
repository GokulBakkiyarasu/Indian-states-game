from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("red")
        self.hideturtle()
        self.goto(200, 250)
        self.current_score = 0
        self.write(f"Score: {self.current_score}", align="center", font=("Arial", 14, "bold"))

    def inc_score(self):
        self.current_score += 1
        self.clear()
        self.write(f"Score: {self.current_score}", align="center", font=("Arial", 14, "bold"))

    def game_over(self):
        self.color("white")
        self.goto(0, 0)
        self.write(f"Score: {self.current_score} Game Over!", align="center", font=("Arial", 14, "bold"))
