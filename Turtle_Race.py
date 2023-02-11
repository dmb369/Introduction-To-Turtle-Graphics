from turtle import *
from random import *

speed(20)
pu()

for i in range(1,20):
    fd(16*i)
    lt(90)
    pd()
    fd(160)
    write(i)
    pu()
    home()
pu()    

#First Turtle
t1=Turtle()
t1.shape("turtle")
t1.color('purple')
t1.pu()
t1.setpos(-10,140)
t1.pd()

#Second Turtle
t2=Turtle()
t2.shape("turtle")
t2.color('blue')
t2.pu()
t2.setpos(-10,110)
t2.pd()

#Third Turtle
t3=Turtle()
t3.shape("turtle")
t3.color('green')
t3.pu()
t3.setpos(-10,80)
t3.pd()

#Fourth Turtle
t4=Turtle()
t4.shape("turtle")
t4.color('orange')
t4.pu()
t4.setpos(-10,50)
t4.pd()

#Fifth Turtle
t5=Turtle()
t5.shape("turtle")
t5.color('red')
t5.pu()
t5.setpos(-10,20)
t5.pd()

for x in range(100):
    t1.fd(randint(1,5))
    t2.fd(randint(1,5))
    t3.fd(randint(1,5))
    t4.fd(randint(1,5))
    t5.fd(randint(1,5))