import turtle

t = turtle.Turtle()

t.speed(0)
t.color("royalblue")

t.pu()
t.goto(-450,300)
t.pd()

t.begin_fill()
t.goto(450,300)
t.rt(90)
t.goto(450,-300)
t.rt(90)
t.goto(-450,-300)
t.rt(90)
t.goto(-450,300)
t.rt(90)
t.end_fill()

t.pu()
t.goto(-450,0)
t.pd()

t.color("darkred")
t.begin_fill()
t.goto(450,0)
t.goto(450,-300)
t.goto(-450,-300)
t.goto(-450,0)
t.end_fill()

t.pu()
t.goto(-150,0)
t.pd()

t.color("white")
t.begin_fill()
t.goto(450,0)
t.goto(450,300)
t.goto(-150,300)
t.goto(-150,0)
t.end_fill()

t.pu()
t.goto(-400,185)
t.pd()

t.color("white")
t.begin_fill()

for i in range(5):
    t.fd(70)
    t.lt(72)
    t.fd(70)
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

turtle.mainloop()