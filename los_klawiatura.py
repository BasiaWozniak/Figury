import turtle
from random import randint
intro = turtle.Screen()
t2 = turtle.Turtle("turtle")
intro.bgcolor("#189C52")
t2.color("white")

#intro
t2.penup()
t2.goto(0,200)
t2.pendown()
t2.write("GRA FIGURY", align="center", font=("Arial", 24, "bold"))
t2.penup()
t2.goto(0,100)
t2.pendown()
t2.hideturtle()
t2.speed(0)
def intro(t2, iter, dlugosc, skrot, kat):
    if iter == 0:
        t2.forward(dlugosc)
    else:
        iter = iter - 1
        dlugosc = dlugosc / skrot
        intro(t2, iter, dlugosc, skrot, kat)
        t2.left(kat)
        intro(t2, iter, dlugosc, skrot, kat)
        t2.right(kat * 2)
        intro(t2, iter, kat, skrot, kat)
        t2.left(kat)
t2.hideturtle()
 # iteracja - o proces w którym zestaw poleceń/instrukcji
# powtarzane są skończoną ilość razy lub do momentu spełnienia warunku
for i in range(3):
  intro(t2, 3, 100, 3, 60)
  t2.right(120)
t2.clear()

#figury
screen = turtle.Screen()
t1 = turtle.Turtle("turtle")
screen.bgcolor('#8BBCF5')
t1.color("white")
t1.penup()
t1.goto(-100,200)
t1.pendown()

f = randint(1,5)
if f == 1:
    t1.forward(50)
    t1.left(90)
    t1.forward(50)
    t1.left(90)
    t1.forward(50)
    t1.left(90)
    t1.forward(50)
if f == 2:
    t1.forward(50)
    t1.left(90)
    t1.forward(50)
    t1.right(90)
    t1.forward(50)
    t1.right(90)
    t1.forward(50)
    t1.forward(50)
    t1.right(90)
    t1.forward(50)
    t1.forward(50)
    t1.right(90)
    t1.forward(50)
    t1.right(90)
if f == 3:
    t1.forward(50)
    t1.left(90)
    t1.forward(50)
    t1.right(90)
    t1.forward(50)
    t1.right(90)
    t1.forward(50)
    t1.left(90)
    t1.forward(50)
    t1.right(90)
    t1.forward(50)
    t1.right(90)
    t1.forward(50)
    t1.forward(50)
    t1.forward(50)
    t1.right(90)
    t1.forward(50)
if f == 4:
    t1.forward(50)
    t1.forward(50)
    t1.forward(50)
    t1.left(90)
    t1.forward(50)
    t1.right(90)
    t1.forward(50)
    t1.right(90)
    t1.forward(50)
    t1.forward(50)
    t1.forward(50)
    t1.right(90)
    t1.forward(50)
    t1.right(90)
    t1.forward(50)
    t1.left(90)
    t1.forward(50)
    t1.left(90)
    t1.forward(50)
    t1.right(90)
    t1.forward(50)
    t1.forward(50)
    t1.forward(50)
    t1.right(90)
    t1.forward(50)
    t1.right(90)
    t1.forward(50)
    t1.left(90)
    t1.forward(50)
if f == 5:
    t1.forward(50)
    t1.left(90)
    t1.forward(50)
    t1.right(90)
    t1.forward(50)
    t1.right(90)
    t1.forward(50)
    t1.left(90)
    t1.forward(50)
    t1.forward(50)
    t1.right(90)
    t1.forward(50)
    t1.right(90)
    t1.forward(50)
    t1.forward(50)
    t1.left(90)
    t1.forward(50)
    t1.right(90)
    t1.forward(50)
    t1.right(90)
    t1.forward(50)
    t1.left(90)
    t1.forward(50)
    t1.right(90)
    t1.forward(50)

#sterowanie
def prawo():
    t1.setheading(0)
    t1.forward(50)
def lewo():
    t1.setheading(180)
    t1.forward(50)
def gora():
    t1.setheading(90)
    t1.forward(50)
def dol():
    t1.setheading(270)
    t1.forward(50)

t1.penup()
t1.goto(-100,-100)
t1.pendown()
turtle.listen()
turtle.onkey(prawo, "Right")
turtle.onkey(lewo, "Left")
turtle.onkey(gora, "Up")
turtle.onkey(dol, "Down")













turtle.mainloop()










