import turtle
from random import randint
screen = turtle.Screen()
t1 = turtle.Turtle("turtle")
t1.speed(1) # zmienia prędkość
t1.color("green") #zmienia kolor
t1.dot(60,"blue") # stawia kropkę
t1.pencolor("red") # kolor ołówka
t1.pensize(20) #rozmiar ołowka
t1.penup() # podniesienie żółwika
t1.goto(-200,-200) # ustawienie żółwika w danym miejscu
t1.pendown() #opuszczenie żółwika
print("Podaj liczbę boków:")
n = int(input())
for i in range(n):
    k = (180 / n) * 2
    t1.forward(100)
    t1.left(k)
turtle.done()
