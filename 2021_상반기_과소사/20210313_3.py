import turtle
import math

pi = math.pi
print(math.radians(2 * pi))
s = turtle.Screen()
t = turtle.Turtle()

t.pensize(3) #펜 진하게

x = -100
y = 100
t.penup()#그리지 않고 좌표 이동
t.goto(x, y)
t.pendown()#그릴 준비

t.circle(100)#반지금 100짜리 원 그리기

t.penup()#그리지 않고 좌표 이동
t.goto(x - 60.62, y + 65)
t.pendown()#그릴 준비

# t.setheading(-60)
# t.left(-60)
t.right(60)
t.circle(70, 120)

t.setheading(180)
t.forward(100)

turtle.mainloop()