import turtle

goldiloks = turtle.Pen()
goldiloks.color("red")
goldiloks.shape("turtle")

for i in range(20):
    goldiloks.forward(10 * i)
    goldiloks.left(90)

turtle.done()
