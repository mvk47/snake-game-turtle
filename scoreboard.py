from turtle import Turtle



class scoreBoard (Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt",mode="r") as data:
            self.high_score = int(data.read())
            #print(data.read())
        #self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(f"score : {self.score} High score {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score = self.score+1
        self.clear()
        self.update_scoreboard()
    
    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center",font=("Arial", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.clear()
        self.update_scoreboard()

