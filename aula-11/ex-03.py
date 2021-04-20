import random
import locale

lin=int(input("linhas"))
col=int(input("colunas"))


matrizA = [[random.randint(-10,10) for x in range(col)] for x in range(lin)]

print("Matriz A: ")
for i in range(0, lin, 1):
    for j in range(0, col, 1):
        print (locale.format("%3d",matrizA[i][j]), end= " ")
    print()


matrizB = [[2 for x in range(3)] for x in range(3)]
matrizC = [[0 for x in range(3)] for x in range(3)]

print("Matriz A: ")
for i in range(0, 3, 1):
    for j in range(0, 3, 1):
        print (locale.format("%3d",matrizA[i][j]), end= " ")
    print()

print("Matriz B: ")
for i in range(0, 3, 1):
    for j in range(0, 3, 1):
        print (locale.format("%3d",matrizB[i][j]), end= " ")
    print()

print("Matriz C: ")
for i in range(0, 3, 1):
    for j in range(0, 3, 1):
        matrizC[i][j]=matrizA[i][j]*matrizB[i][j]
        print (locale.format("%3d",matrizC[i][j]), end= " ")
    print()
