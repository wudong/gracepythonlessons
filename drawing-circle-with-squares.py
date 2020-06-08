import turtle

goldiloks = turtle.Pen()
goldiloks.color("red")
goldiloks.shape("turtle")
goldiloks.speed(0)
for i in range(360):
    goldiloks.left(1)
    for j in range(4):
        goldiloks.forward(100+5*i)
        goldiloks.left(90)

turtle.done()
