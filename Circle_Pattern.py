from turtle import *
a=['white','yellow','light blue','pink']
speed(0)
bgcolor('black')
for b in range(0,4):
    for z in range(0,10):
        color(a[b])
        y=150-10*b
        for x in range(0,10):
            circle(y)
            y=y-4
        rt(36)
    rt(2*(b+1))