import random
import turtle

goldiloks = turtle.Pen()
goldiloks.shape("turtle")
goldiloks.width(3)
goldiloks.speed(0)
colorlist = ["yellow","red","blue","purple","pink","turquoise","aqua"]
def square(size):
    for i in range(4):
        goldiloks.forward(size)
        goldiloks.left(90)

for i in range(100):
    x = random.randrange(-200, 250)
    y = random.randrange(-200, 250)
    goldiloks.up()
    goldiloks.goto(x, y)
    goldiloks.down()


    color = random.choice(colorlist)
    goldiloks.color(color)
    square(random.randrange(10, 250))
























turtle.done()
