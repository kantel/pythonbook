import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Hallo, Türtel!")

tess = turtle.Turtle()
tess.color("darkgreen")
tess.pensize(3)

tess.forward(50)
tess.left(120)
tess.forward(50)

wn.mainloop()