#Ex4: Considere um polinônio de forma geral dado por:
#         a + b*x + c*x**2 + ... + d*x**(n-1), com n>=1
# E considere que tal polinômio pode ser representado por um vetor dado por:
#         [a, b, ...., c, d]
#
# Assim, na posição 0 temos o multiplicador (a) do termo de expoente 0
#        na posição 1 temos o multiplicador (b) do termo de expoente 1
#        e assim por diante....
#
# Como por exemplo:
#  6 - 3*x + x**2  ---->  6*x**0 - 3*x**1 + 1*x**2  --> [6, -3, 1]
#
# Sabendo que a derivada e a integral de um polinômio como dado acima,
# geram outro polinônio, pela simples manipulação dos expoentes:
#           http://pt.wikihow.com/Calcular-a-Diferencial-de-um-Polin%C3%B4mio
#           http://pt.wikihow.com/Integrar
#
# a) implemente um função que recebe um vetor representando um polinônio
#    qualquer e retorne outro vetor, representando sua derivada

# b) implemente um função que recebe um vetor representando um polinônio
#    qualquer e retorne outro vetor, representando sua integral. Considere
#    que o termo constante que surge na integração é nulo.
#
#  Ex:   x**2 --> 0*x**0 + 0*x**1 + 1*x**2 --> [0,0,1]
#        derivar([0,0,1]) --> retorna [0,2] --> que representa 2*x
#
#  Obs: ao derivar um polinômio o seu grau sempre diminui, logo
#       a quantidade de elementos no vetor também. Retorne vetor
#       vazio ([]) ao derivar um vetor de tamanho 1, que corresponde
#       a derivar uma constante.

def derivar(pol):
    '''
    >>> derivar([1])
    []
    >>> derivar([2,2,2])
    [2, 4]
    '''
#--------------- ADICIONAR SEU CÓDIGO AQUI ------------#

#-------------------------------------------------------#

def integrar(pol):
    '''
    >>> integrar([4, 2])
    [0.0, 4.0, 1.0]
    >>> integrar([1,2,3])
    [0.0, 1.0, 1.0, 1.0]
    '''
#--------------- ADICIONAR SEU CÓDIGO AQUI ------------#

#-------------------------------------------------------#


#**PROGRAMA PRINCIPAL *******************************#

#--DOCTEST -------#
# Comente esta parte durante o desenvolvimento
# caso queira pular o teste automático da função
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True,report=False)
#------------------#

