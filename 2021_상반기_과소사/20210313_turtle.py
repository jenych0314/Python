import turtle

s = turtle.Screen()
t = turtle.Turtle()

t.pensize(5) #펜 진하게
t.speed(1000000)
x = 0
y = 0

t.circle(150)#반지름 100짜리 원 그리기

t.penup()#그리지 않고 좌표 이동
t.goto(x - 60.62, y + 65)
t.pendown()#그릴 준비

t.setheading(-60)
t.circle(70, 120)

t.setheading(180)
t.forward(120)

x = -100
y = 100

t.penup()#그리지 않고 좌표 이동
t.goto(x, y)
t.pendown()#그릴 준비

t.setheading(-60)
t.circle(30)

x = 49
y = 100

t.penup()#그리지 않고 좌표 이동
t.goto(x, y)
t.pendown()#그릴 준비

t.setheading(-60)
t.circle(30)