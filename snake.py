from turtle import Screen,Turtle
import time

starting_position = [(0, 0), (-20, 0), (-40, 0)]
MOVE = 20

class Snake:
    def __init__(self):
      self.body = []
      self.create_snake()
      self.head = self.body[0]
        
    def create_snake(self):
      for position in starting_position:
        self.add_segment(position)

    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.body.append(new_segment)

    def extend(self):
        self.add_segment(self.body[-1].position())

    def move(self):
        for seg_num in range(len(self.body) - 1, 0, -1):
            new_x = self.body[seg_num - 1].xcor()
            new_y = self.body[seg_num - 1].ycor()
            self.body[seg_num].goto(new_x, new_y)
        self.body[0].forward(MOVE)
    def up(self):
        if self.body[0].heading() != 270:
            self.body[0].setheading(90)
            #time.sleep(0.3)
    def down(self):
        if self.body[0].heading() != 90:
            self.body[0].setheading(270)
            #time.sleep(0.3)
    def left(self):
        if self.body[0].heading() != 0:
            self.body[0].setheading(180)
            #time.sleep(0.3)
    def right(self):
        if self.body[0].heading() != 180:
            self.body[0].setheading(0)

    def reset(self):
        for seg in self.body:
            seg.goto(1000,1000)
        self.body.clear()
        self.create_snake()
        self.head = self.body[0]
