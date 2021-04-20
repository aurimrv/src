#Ex3: Fazer uma função que receba um número na base 10 e
#     converta para uma base b, sendo 2<=b<10.
#     Exemplo: 64 na base 10 --> 1000000 na base 2 --> 100 na base 8
#


def converter(num, base):
    '''
    >>> converter(64, 2)
    1000000
    >>> converter(64, 8)
    100
    >>> converter(64, 10)
    64
    '''
#------ ADICIONAR SEU CÓDIGO AQUI -------------#  
    #observe a endentação

    #não esqueça do return...
#-----------------------------------------------#


#**PROGRAMA PRINCIPAL *******************************#

#--DOCTEST -------#
# Comente esta parte durante o desenvolvimento
# caso queira pular o teste automático da função
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True,report=False)
#------------------#

