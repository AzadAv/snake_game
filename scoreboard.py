from turtle import Turtle
from turtle import Screen
from tkinter import *
ALIGMENT = "center"
FONT = ("Courier", 24, "normal")
screen= Screen()
def close_the_screen():

    screen.bye()

def restart_game():

    screen.clearscreen()
    # screen.reset()
    # screen.update()


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.hideturtle()

        self.score = 0
        self.update_scoreboard()

        self.exit_btn = self.exit_button()
        #self.restart_button()
       
        
    def update_scoreboard(self):
        self.write(f"Score : {self.score}", align=ALIGMENT,
                   font=FONT)
        
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", align=ALIGMENT,
                   font=FONT)
    
    def increase_score(self):
        
        self.score+=1
        self.clear()
        self.update_scoreboard()        
        
    def exit_button(self):

        canvas = screen.getcanvas()
        exit_button = Button(canvas.master, text="Exit", command=close_the_screen)
        exit_button.pack()
        exit_button.place(x=100, y=10) 

    def restart_button(self):

        canvas = screen.getcanvas()
        restart_button = Button(canvas.master, text="Restart", command=restart_game)
        restart_button.pack()
        restart_button.place(x=300, y=10) 
