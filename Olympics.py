import turtle

turtle.shape('turtle')

x=['blue','black','red','yellow','green']

for y in range(3):
    turtle.width(3)
    turtle.pd()
    turtle.pencolor(x[y])
    turtle.circle(50)
    turtle.pu()
    turtle.fd(110)

turtle.home()
turtle.rt(90)
turtle.fd(50)
turtle.lt(90)
turtle.fd(50)
for z in range(3,5):
    turtle.width(3)
    turtle.pd()
    turtle.color(x[z])
    turtle.circle(50)
    turtle.pu()
    turtle.fd(110)
    