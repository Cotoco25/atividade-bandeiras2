import turtle

t = turtle.Turtle()

t.speed(0)

t.pu()
t.goto(-450,300)
t.pd()
def retangulo(cor1,x1,x11):
    t.color(cor1)
    t.begin_fill()
    t.goto(x1,300)
    t.goto(x1,-300)
    t.goto(x11,-300)
    t.goto(x11,300)
    t.goto(x1,300)
    t.end_fill()

retangulo("blue",-150,-450)

def retangulo2(cor2,x2,x22):
    t.color("white")
    t.begin_fill()
    t.goto(x2,300)
    t.goto(x2,-300)
    t.goto(x22,-300)
    t.goto(x22,300)
    t.goto(x2,300)
    t.end_fill()

retangulo2("white",150,-150)

def retangulo3(cor3,x3,x33):
    t.color(cor3)
    t.begin_fill()
    t.goto(x3,300)
    t.goto(x3,-300)
    t.goto(x3,-300)
    t.goto(x33,-300)
    t.goto(x33,300)
    t.goto(x3,300)
    t.end_fill()

retangulo3("red",450,150)


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
