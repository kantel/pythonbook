# Turtlespirale

import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tina = turtle.Turtle()
tina.shape("turtle")
tina.color("darkgreen")

tina.penup()
size = 20

for i in range(30):
    tina.stamp()
    size += 3
    tina.forward(size)
    tina.right(24)

wn.mainloop()