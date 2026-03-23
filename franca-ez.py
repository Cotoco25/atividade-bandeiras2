import turtle

t = turtle.Turtle()

t.speed(0)

t.pu()
t.goto(-450,300)
t.pd()

t.color("blue")
t.begin_fill()
t.goto(-150,300)
t.goto(-150,-300)
t.goto(-450,-300)
t.goto(-450,300)
t.goto(-150,300)
t.end_fill()


t.color("white")
t.begin_fill()
t.goto(150,300)
t.goto(150,-300)
t.goto(-150,-300)
t.goto(-150,300)
t.goto(150,300)
t.end_fill()


t.color("red")
t.begin_fill()
t.goto(450,300)
t.goto(450,-300)
t.goto(450,-300)
t.goto(150,-300)
t.goto(150,300)
t.goto(450,300)
t.end_fill()



t.pensize(5)
t.color("black")
t.pu()
t.goto(-450,300)
t.pd()
t.goto(450,300)
t.goto(450,-300)
t.goto(-450,-300)
t.goto(-450,300)

t.hideturtle()

turtle.mainloop()