#Ex0: Criar uma função que receba um número inteiro e retorne seu dobro.

#**FUNÇÃO******************************************# 
def dobro(n):
    '''
    >>> dobro(0)
    0
    >>> dobro(20)
    40
    '''
#-------- ADICIONAR SEU CÓDIGO AQUI -------#
    ret = n*2
    return ret
#------------------------------------------#


#**PROGRAMA PRINCIPAL *******************************#

#--DOCTEST -------#
# Comente esta parte durante o desenvolvimento
# caso queira pular o teste automático da função
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True,report=False)
#------------------#

#------Caso queira fazer seus próprios testes, colocar aqui --#
n=10
print("O dobro de 10 é ", dobro(10))