import turtle
x=0
turtle.begin_fill()
for x in range (4):
    turtle.shape('square')
    turtle.color('red')
    turtle.forward(100)
    turtle.lt(90)
turtle.end_fill()