import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Labyrinthe")
wn.setup(700,700)

class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

#Creer liste niveau
levels = [""]

level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX X",
"X      XXXXXX             X",
"XXXXX               XXXXXXX",
"XXXXXXXXXXXXXXXX    XXXXXXX",
"XXXXXXXXXXXXXXXXX  XXXXXXXX",
"XXXXXXXXXXXXXXX     XXXXXXX",
"XXX  XXXXXXXXXX     XXXXXXX",
"XXX                 XXXXXXX",
"XXX  XX    XXXXXXX XXXXXXXX",
"XXX  XXXXXXXXXXXXX XXXXXXXX",
"XXX  XXXXXXXXXXXXX XXXXXXXX",
"XXX  XXXXXXXXXXXXX XXXXXXXX",
"XXX  XXXXXXXXXXXXX XXXXXXXX",
"XXX  XXXXXXXXXXXXX XXXXXXXX",
"XXX  XXXXXXXXXXXXX XXXXXXXX",
"XXX  XXXXXXXXXXXXX XXXXXXXX",
"XXX  XXXXXXXXXXXXX XXXXXXXX",
"XXX  XXXXXXXXXXXXX XXXXXXXX",
"XXX  XXXXXXXXXXXXX XXXXXXXX",
"XXX  XXXXXXXXXXXXX XXXXXXXX",
"XXX  XXXXXXXXXXXXX XXXXXXXX",
"XXX  XXXXXXXXXXXXX XXXXXXXX",
"XXX  XXXXXXXXXXXXX XXXXXXXX",
"XXX  XXXXXXXXXXXXX XXXXXXXX",
"XXX                  XXXXXX",
"XXX  XXXXXXXXXXXXXXXXXXXXXX",
]

levels.append(level_1)
def  setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
pen = Pen()

setup_maze(levels[1])

while True:
    pass