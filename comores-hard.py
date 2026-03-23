import turtle

t = turtle.Turtle()

t.speed(0)

t.pu()
t.goto(-450,300)
t.pd()

t.color("yellow")
t.begin_fill()
t.goto(450,300)
t.goto(450,150)
t.goto(-450,150)
t.goto(-450,300)
t.end_fill()

t.pu()
t.goto(-450,0)
t.pd()

t.color("red")
t.begin_fill()
t.goto(450,0)
t.goto(450,-150)
t.goto(-450,-150)
t.goto(-450,0)
t.end_fill()

t.pu()
t.goto(-450,-150)
t.pd()

t.color("blue")
t.begin_fill()
t.goto(450,-150)
t.goto(450,-300)
t.goto(-450,-300)
t.goto(-450,-150)
t.end_fill()

t.pu()
t.goto(-450,300)
t.pd()
t.color("seagreen")
t.begin_fill()
t.goto(0,0)
t.goto(-450,-300)
t.goto(-450,300)
t.end_fill()




t.up()
t.goto(-320,-100)
t.begin_fill()
t.color("white")
t.circle(100)
t.end_fill()

t.up()
t.goto(-280,-100)
t.begin_fill()
t.color("seagreen")
t.circle(100)
t.end_fill()

t.pu()
t.goto(-317,70)
t.pd()

t.color("white")
t.begin_fill()

for i in range(5):
    t.fd(13)
    t.lt(72)
    t.fd(13)
    t.rt(144)

t.end_fill()



t.pu()
t.goto(-317,30)
t.pd()

t.color("white")
t.begin_fill()

for i in range(5):
    t.fd(13)
    t.lt(72)
    t.fd(13)
    t.rt(144)

t.end_fill()



t.pu()
t.goto(-317,-15)
t.pd()

t.color("white")
t.begin_fill()

for i in range(5):
    t.fd(13)
    t.lt(72)
    t.fd(13)
    t.rt(144)

t.end_fill()


t.pu()
t.goto(-317,-60)
t.pd()

t.color("white")
t.begin_fill()

for i in range(5):
    t.fd(13)
    t.lt(72)
    t.fd(13)
    t.rt(144)

t.end_fill()




#destaque
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