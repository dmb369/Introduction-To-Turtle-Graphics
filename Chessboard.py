import turtle

turtle.shape('classic')
turtle.speed(0)
b=0
list=['black','white']
for w in range(4):
    turtle.fd(240)
    turtle.lt(90)
turtle.lt(90)
for z in range(8):
  for x in range(8):
    turtle.begin_fill()  
    for y in range(4):
     turtle.fd(30)
     turtle.rt(90)
    turtle.color('black',list[(z+x)%2]) 
    turtle.end_fill()
    turtle.fd(30)
  turtle.pu()
  turtle.home()
  b=b+30
  turtle.fd(b)
  turtle.lt(90)
  turtle.pd()