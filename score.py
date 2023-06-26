from turtle import Turtle, textinput

FONT = ('Courier', 15, 'normal')
class Score (Turtle):

    def __init__(self):
        """counts the score of foods eaten by the snake"""
        super().__init__()
        self.points = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.write(f"score: {self.points}", move = False, align = "center", font = FONT)

    def increase_score(self):
        """increases the score by one"""
        self.points += 1
        self.clear()
        self.write(f"score: {self.points}", move = False, align = "center", font = FONT)

    def game_over(self):
        """set the game over sequence. Writes game over and asks for option to play another game"""
        self.goto(0, 150)
        self.write("GAME OVER", move = False, align = "center", font = FONT)
        answer = textinput("Play Again", "Type 'y' for yes:")
        if answer == 'y':
            return True
        else:
            return False

    def win(self):
        """set the wining sequence. Writes you win and asks if you want to play another game"""
        self.goto(0, 150)
        self.write("YOU WIN!!!", move=False, align="center", font=FONT)
        answer = textinput("Play Again", "Type 'y' for yes:")
        if answer == 'y':
            return True
        else:
            return False





