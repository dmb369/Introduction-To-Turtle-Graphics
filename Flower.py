import turtle

a=0
z=['red','orange','yellow','green','blue','violet','red','green','pink']

for x in range (8):
    turtle.rt(45)
    a=a+1
    for y in range(2):
        turtle.width(3)
        turtle.pencolor(z[a])
        turtle.rt(120)
        turtle.fd(100)
        turtle.rt(60)
        turtle.fd(100)
