import turtle
from random import randint
screen = turtle.Screen()
t1 = turtle.Turtle("turtle")
screen.bgcolor("green")
t1.color("white")
def czy_pier(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    return True
#1
x1 = randint(0,390)
y1 = randint(0,390)
t1.penup()
t1.goto(x1,y1)
t1.pendown()
print("Jaką figurę mam narysować?")
k = input()
print("Wpisz wymiary")
for i in range(1):
    if k == "prostokat":
        a = int(input())
        b = int(input())
        t1.forward(a)
        t1.left(90)
        t1.forward(b)
        t1.left(90)
        t1.forward(a)
        t1.left(90)
        t1.forward(b)
    if k == "kolo":
        a = int(input())
        t1.circle(a)
    if k == "trapez":
        a = int(input())
        b = int(input())
        t1.forward(a)
        t1.left(90 - 45)
        t1.forward(b)
        t1.left(90 + 45)
        t1.forward(a)
        t1.left(90 - 45)
        t1.forward(b)
        t1.left(90 + 45)
    if k == "romb":
        a = int(input())
        t1.forward(a)
        t1.left(90 - 45)
        t1.forward(a)
        t1.left(90 + 45)
        t1.forward(a)
        t1.left(90 - 45)
        t1.forward(a)
        t1.left(90 + 45)

#2
x2 = randint(-450,0)
y2 = randint(0,390)
t1.penup()
t1.goto(x2,y2)
t1.pendown()

l = randint(0,400)
while not czy_pier(l):
    t1.write(l,font=("Arial",10,"normal"))
    l = randint(0, 400)
    t1.penup()
    t1.forward(50)
t1.write(l,font=("red",30,"normal"))

#3
x3 = randint(-450,0)
y3 = randint(-370,0)
t1.penup()
t1.goto(x3, y3)
t1.pendown()
t1.circle(50)

#4
x4 = randint(0,400)
y4 = randint(-400,0)
t1.penup()
t1.goto(x4, y4)
t1.pendown()
t1.stamp()

t1.penup()
t1.goto(0,0)
t1.pendown()

turtle.done()

#1 ----> użytkownik wybiera figurę i jej rozmiar. Żółwik to rysuje
#2 Sprawdzanie czy wylosowana liczba jest liczbą pierwszą
#3 Rysowanie koła za pomocą funkcji
#4 Suma cyfr z wylosowanej liczby