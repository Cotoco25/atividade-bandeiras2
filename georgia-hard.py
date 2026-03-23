import turtle

t = turtle.Turtle()

t.speed(0)

t.pu()
t.goto(-50,300)
t.pd()

t.rt(90)

t.color("red")
t.begin_fill()


for i in range(2):
    t.fd(600)
    t.lt(90)
    t.fd(100)
    t.lt(90)
    
t.end_fill()

t.up()
t.goto(-450,-50)
t.lt(90)
t.pd()

t.color("red")
t.begin_fill()
for i in range(2):
    t.fd(900)
    t.lt(90)
    t.fd(100)
    t.lt(90)
    
t.end_fill()

t.up()
t.goto(-330,170)
t.lt(90)
t.pd()

t.pensize(5)
t.color("red")
t.begin_fill()

for i in range(4):
    t.fd(20)
    t.rt(90)
    t.fd(40)
    t.lt(90)
    t.fd(40)
    t.rt(90)

t.rt(90)
t.end_fill()

t.up()
t.goto(-330,-200)
t.lt(90)
t.pd()

t.color("red")
t.begin_fill()

for i in range(4):
    t.fd(20)
    t.rt(90)
    t.fd(40)
    t.lt(90)
    t.fd(40)
    t.rt(90)

t.rt(90)
t.end_fill()

t.up()
t.goto(180,140)
t.lt(90)
t.pd()

t.color("red")
t.begin_fill()

for i in range(4):
    t.fd(20)
    t.rt(90)
    t.fd(40)
    t.lt(90)
    t.fd(40)
    t.rt(90)

t.rt(90)
t.end_fill()

t.up()
t.goto(180,-170)
t.lt(90)
t.pd()

t.color("red")
t.begin_fill()

for i in range(4):
    t.fd(20)
    t.rt(90)
    t.fd(40)
    t.lt(90)
    t.fd(40)
    t.rt(90)

t.lt(90)
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