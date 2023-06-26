from turtle import Turtle
import random


class Food (Turtle):

    def __init__(self):
        """sets the food for the snake"""
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("gray")
        self.speed("fastest")
        random_x = 20*random.randint(-14, 14)
        random_y = 20*random.randint(-14, 14)
        self.goto(random_x, random_y)


    def refresh(self):
        """adds new food"""
        random_x = 20 * random.randint(-14, 14)
        random_y = 20 * random.randint(-14, 14)
        self.goto(random_x, random_y)
