#Tina und Tom
# Schildkrötentanz

import turtle

wn = turtle.Screen()
wn.bgcolor("green")
wn.title("Tess & Alex")

tina = turtle.Turtle()
tina.shape("turtle")
tina.color("red")
tina.pensize(5)

tom = turtle.Turtle()
tom.shape("turtle")
tom.color("blue")
tom.pensize(5)

for i in range(3):
    tina.forward(80)
    tina.left(120)
    tom.forward(80)
    tom.left(90)

tina.right(180)
tina.forward(80)
tom.forward(160)
tom.left(90)

wn.mainloop()