import turtle

t = turtle.Turtle()

t.speed(0)


t.pu()
t.goto(-450,0)
t.pd()


t.color("steelblue")
t.begin_fill()
t.goto(0,0)
t.goto(0,-300)
t.goto(-450,-300)
t.goto(-450,0)
t.end_fill()

t.pu()
t.goto(450,0)
t.pd()

t.color("firebrick")
t.begin_fill()
t.goto(0,0)
t.goto(0,300)
t.goto(450,300)
t.goto(450,0)
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