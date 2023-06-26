from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        """sets snake class"""
        self.speed = 0.1
        self.full_snake = []
        self.start()
        self.head = self.full_snake[0]





    def add_seg(self,x , y):
        """adds a segment to the snake"""

        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(x, y)
        self.full_snake.append(new_segment)


    def start (self):
        """initiated the starting 3 segment snake at 0,0"""
        x = 0
        y = 0
        for n in range(3):
            self.add_seg(x, y)
            x = x - 20



    def hit (self):
        """Detects collision with wall or snake and return a false if there is a collision or true if not"""
        x, y = self.head.position()
        if x > 290 or x < -290 or y > 290 or y < -290:
            return False
        for seg in self.full_snake[1:]:
            if self.head.distance(seg) < 10:
                return False
        return True

    def extend(self):
        """extends snake by one segment at the end"""
        x, y = self.full_snake[-1].pos()
        self.add_seg(x, y)

    def move(self):
        """moves the snake one step MOVE_DISTANCE and returns True if there is no collision (from hit method) or False if there is"""
        for seg_num in range(len(self.full_snake) - 1, 0, -1):
            (x, y) = self.full_snake[seg_num - 1].pos()
            self.full_snake[seg_num].goto(x, y)
        self.head.forward(MOVE_DISTANCE)
        return self.hit()


    #sets the moving direction from the key input
    def up (self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def right (self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left (self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down (self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


