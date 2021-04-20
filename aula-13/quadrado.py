#Define a função de nome "quadrado" recebendo
#como parâmetro um valor x
def quadrado(x):
    #Retorna o valor de x ao quadrado
    return x*x

#Gostaria de calcular o quadrado de um valor
#informado pelo usuário
#Leio um valor do usuário e converto para inteiro
numero = int(input("digite um nro: "))
#Mostro o valor informado pelo usuário
print ("Valor digitado: ", numero)
#Mostro o quadrado do valor informado
print ("Quadrado do valor digitado: ", quadrado(numero))
