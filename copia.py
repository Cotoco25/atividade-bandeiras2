import turtle

t = turtle.Turtle()

t.speed(0)

t.pu()
t.goto(-450,300)
t.pd()




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


#simetria
t.color("black")
t.goto(450,-300)
t.goto(0,0)
t.goto(450,300)
t.goto(-450,-300)
t.goto(0,0)
t.goto(0,700)
t.goto(0,-700)
t.goto(0,0)
t.goto(700,0)
t.goto(-700,0)




t.hideturtle()
turtle.mainloop()