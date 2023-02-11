import turtle

x=0
turtle.begin_fill()
turtle.color('black','yellow')
y=200
for x in range(90):
    turtle.fd(y)
    turtle.rt(144)
    y=y-3
turtle.end_fill()

