import turtle

t = turtle.Turtle()

t.speed(0)


t.pu()
t.goto(-450,300)
t.pd()



t.color("white")
t.begin_fill()
t.goto(450,300)
t.goto(450,-300)
t.goto(-450,-300)
t.goto(-450,300)
t.end_fill()

t.pu()
t.goto(-100,-50)
t.pd()

t.color("steelblue")
t.pensize(10)

for _ in range(3):
    t.fd(200)
    t.lt(120) 

t.pu()
t.goto(100,50)
t.pd()
t.lt(180)
for _ in range(3):
    t.fd(200)
    t.lt(120) 

t.pensize(1)


t.pu()
t.goto(-450,190)
t.pd()
t.color("steelblue")
t.begin_fill()
t.goto(450,190)
t.goto(450,260)
t.goto(-450,260)
t.goto(-450,190)
t.end_fill()

t.pu()
t.goto(-450,-190)
t.pd()
t.color("steelblue")
t.begin_fill()
t.goto(450,-190)
t.goto(450,-260)
t.goto(-450,-260)
t.goto(-450,-190)
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