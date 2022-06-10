import turtle
from random import randint
screen = turtle.Screen()
t1 = turtle.Turtle("turtle")
x = randint(-450,400)
y = randint(-400,300)
t1.penup()
t1.goto(x,y)
t1.pendown()
t1.stamp()
x = x * (-1)
y = y * (-1)
t1.penup()
t1.goto(x,y)
t1.pendown()
for i in range(3):
    k = (180 / 3) * 2
    t1.forward(100)
    t1.left(k)
turtle.done()


 #losowanie pozycji żólwia
 # na tej pozycji pieczątka stamp
 # na odbicu lustrzanym rysujemy trójkąt

