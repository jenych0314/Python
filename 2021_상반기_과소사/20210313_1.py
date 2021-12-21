import turtle

s = turtle.Screen()
t = turtle.Turtle()
# t = turtle.Turtle(shape='turtle')
t.pensize(3) #펜 진하게

x = -100
y = 100
t.goto(x, y)#좌표로 선 그리면서 이동
t.undo()#취소

t.penup()#그리지 않고 좌표 이동
t.goto(x, y)
t.pendown()#그릴 준비

t.dot()
t.circle(100)#반지금 100짜리 원 그리기
#거북이가 바라보는 방향의 왼쪽이 원중심
s._bgcolor('white')