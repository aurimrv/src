import turtle
from math import sqrt

L = input("Tamanho do lado: ");
N = input("Quantidade de quadrados: ");

L = int(L)
N = int(N)

pen = turtle.Pen()

A = L*L

soma = A

cont = 2

# desenhando quadrado
pen.forward(L)
pen.left(90)
pen.forward(L)
pen.left(90)
pen.forward(L)
pen.left(90)
pen.forward(L)

while cont <= N:
   D = sqrt(L)
   A = A/2
   soma = soma+A
   cont = cont + 1
   pen.left(90)
   pen.forward(L/2)
   pen.left(45)
   pen.forward(D)
   pen.left(90)
   pen.forward(D)
   pen.left(90)
   pen.forward(D)
   pen.left(90)
   pen.forward(D)
   L = D

print("Soma das areas: ", soma)

   

   
