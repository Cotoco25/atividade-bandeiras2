import turtle

t = turtle.Turtle()

t.speed(0)

t.pu()
t.goto(-450,300)
t.pd()

t.color("seagreen")
t.begin_fill()
t.goto(-150,300)
t.goto(-150,-300)
t.goto(-450,-300)
t.goto(-450,300)
t.goto(-150,300)
t.end_fill()


t.color("firebrick")
t.begin_fill()
t.goto(150,300)
t.goto(150,-300)
t.goto(-150,-300)
t.goto(-150,300)
t.goto(150,300)
t.end_fill()

t.color("yellow")
t.begin_fill()
t.goto(450,300)
t.goto(450,-300)
t.goto(450,-300)
t.goto(150,-300)
t.goto(150,300)
t.goto(450,300)
t.end_fill()

t.pu()
t.goto(-39,50)
t.pd()

t.color("yellow")
t.begin_fill()

for i in range(5):
    t.fd(30)
    t.lt(72)
    t.fd(30)
    t.rt(144)

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