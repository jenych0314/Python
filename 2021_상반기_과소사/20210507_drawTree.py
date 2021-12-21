import turtle

s = turtle.Screen()
t = turtle.Turtle()

def drawTree(t, lineLength, *angle):
    if lineLength <= 5:
        return 0
    t.forward(lineLength)
    t.left(30)
    drawTree(t, lineLength * (2/3))
    t.right(60)
    drawTree(t, lineLength * (2/3))
    t.left(30)
    t.back(lineLength)

lineLength = int(input())
t.left(90)

drawTree(t, lineLength)