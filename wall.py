from turtle import Turtle

LEFT_TOP=(-290, 270)
RIGHT_TOP=((290,270))
RIGHT_BOTTOM=(290, -290)
LEFT_BOTTOM=(-290, -290)

LEFT=[LEFT_TOP,LEFT_BOTTOM]
TOP=[LEFT_TOP,RIGHT_TOP]
RIGHT=[RIGHT_TOP,RIGHT_BOTTOM]
BOTTOM = [RIGHT_BOTTOM,LEFT_BOTTOM]

WALLS_COORDINATES = [LEFT,TOP,RIGHT,BOTTOM]

class Wall(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.draw_wall()

    def draw_wall(self):

        for lists in WALLS_COORDINATES:
           
            self.goto(lists[0])
            self.pendown()
            self.goto(lists[1])
            self.hideturtle()