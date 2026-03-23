import turtle

t = turtle.Turtle()

t.speed(0)


t.pu()
t.goto(-450,300)
t.pd()





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