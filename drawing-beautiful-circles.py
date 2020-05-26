import turtle

goldiloks = turtle.Pen()
goldiloks.color("aqua")
goldiloks.shape("turtle")
goldiloks.speed(0)
colorlist = ["yellow","red","blue","green","orange","purple","pink","aqua"]


for i in range(150):
    color = colorlist[i%7]
    goldiloks.color(color)
    goldiloks.circle(i * 3)
    goldiloks.left(10)

turtle.done()
