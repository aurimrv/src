#Ex1: Criar uma função que receba um número inteiro positivo(n >= 0) e retorne
#     seu fatorial. Caso n seja negativo retornar -1 como indicativo de erro.

#**FUNÇÃO******************************************# 
def fatorial(n):
    '''
    >>> [fatorial(n) for n in range(-1,6)]
    [-1, 1, 1, 2, 6, 24, 120]
    '''
#-------- ADICIONAR SEU CÓDIGO AQUI -------#
    #observe a endentação

    #não esqueça do return...
#-------------------------------------------#


#**PROGRAMA PRINCIPAL *******************************#

#--DOCTEST -------#
# Comente esta parte durante o desenvolvimento
# caso queira pular o teste automático da função
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True,report=False)
#------------------#

