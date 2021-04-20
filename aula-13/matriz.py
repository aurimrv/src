import random
###### FUNÇÕES:

def InicializaMatrizZero(linhas,colunas):
    matriz = [[0 for x in range(colunas)] for x in range(linhas)]
    return matriz


def InicializaMatrizAleatoria(linhas,colunas,menor,maior):
    matriz = InicializaMatrizZero(linhas,colunas)
    for i in range(0, linhas, 1):
        for j in range(0, colunas, 1):
            matriz[i][j]=random.randint(menor,maior)
    return matriz

def PrintMatriz(matriz):
    linhas=len(matriz)
    colunas=len(matriz[0])
    for i in range(0, linhas, 1):
        for j in range(0, colunas, 1):
            print("%6.2f"%matriz[i][j], end= " ")
        print()

    return

l=int(input("Número de linhas: "))
c=int(input("Número de colunas: "))
mat=InicializaMatrizAleatoria(l,c,-10,10)
PrintMatriz(mat)
