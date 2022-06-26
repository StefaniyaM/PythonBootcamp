#####Turtle Intro######

import turtle as t

turty = t.Turtle()
turty.shape("turtle")
turty.color("red")
# turty.forward(100)
# turty.backward(200)
# turty.right(90)
# turty.left(180)
# turty.setheading(0)


######## Challenge 1 - Draw a Square ############
for _ in range(4):
    turty.forward(100)
    turty.left(90)


screen = t.Screen()
screen.exitonclick()
print("Bye!")

# =========================



from turtle import Turtle, Screen

tim = Turtle()

########### Challenge 2 - Draw a Dashed Line ########

for _ in range(15):
    tim.pendown()
    tim.forward(10)
    tim.penup()
    tim.forward(10)

screen = Screen()
screen.exitonclick()

# ============================




from turtle import Turtle, Screen

tim = Turtle()

########### Challenge 3 - Draw Shapes ########

colors = ["cornflower blue", "aquamarine", "gold", "dark red",
          "salmon", "indigo", "dark green", "gray", "olive drab", "olive"]


def draw_shapes(n):
    for _ in range(n):
        tim.forward(100)
        tim.right(360//n)


for i in range(3, 11):
    tim.color(colors[i-3])
    draw_shapes(i)


screen = Screen()
screen.exitonclick()

# ==============================

import turtle as t
import random

tim = t.Turtle()

########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed",
           "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

directions = [0, 90, 180, 270]

tim.speed('fastest')

while True:
    tim.color(random.choice(colours))
    tim.pensize(10)
    tim.forward(20)
    tim.setheading(random.choice(directions))
    
# ==============================

import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed('fastest')


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

########### Challenge 5 - Spirograph ########


def draw_spirograph(gap):
    for _ in range(int(360/gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+gap)


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
