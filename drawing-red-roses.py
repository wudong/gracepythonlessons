import turtle

goldiloks = turtle.Pen()
goldiloks.color("red")
goldiloks.shape("turtle")
goldiloks.speed(0)
goldiloks.width(4)
for i in range(100):
    goldiloks.circle(i*3, 180)
    goldiloks.right(45)

turtle.done()
