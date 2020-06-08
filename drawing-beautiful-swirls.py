import turtle

goldiloks = turtle.Pen()
goldiloks.color("red")
goldiloks.shape("turtle")
goldiloks.speed(0)
goldiloks.width(5)
for i in range(100):
    goldiloks.forward(i*2)
    goldiloks.circle(i*2, 90)
    goldiloks.right(20)
turtle.done()
