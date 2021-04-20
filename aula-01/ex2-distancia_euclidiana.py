#Ex2: Podemos usar vetores para representar pontos num espaço de dimensões N
#     quaisquer. Por exemplo, o vetor [1, 2] pode representar o ponto x=1 e y=2
#     num espaço plano, ou [1,2,3] o ponto x=1, y=2 e z=3 num espaço tridimensional.
#
#     Sejam A e B dois vetores com N elementos cada, representando pontos num espaço
#     N dimensional. Faça uma função que receba estes dois pontos e retorne
#     a distância eucliana entre eles. Caso os vetores não tenham o mesmo número
#     de elementos retorne -1.
#     A distância euclidiana é dada pela raiz quadrada da somatória do quadrado das
#     diferenças entre as coordenadas do ponto:
#        https://pt.wikipedia.org/wiki/Dist%C3%A2ncia_euclidiana
#     Por exemplo:
#     A=[5,6] e B=[7,9]
#     d=sqrt((5-7)**2 + (6-9)**2)=sqrt(2**2+3**2)=sqrt(4+9)=sqrt(13)=3.6055


#**FUNÇÃO******************************************# 
def dist(A,B):
    '''
    >>> dist([0],[])
    -1
    >>> dist([10,10],[10,10])
    0.0
    >>> dist([0,0,0],[0,0,4])
    4.0
    '''
#-------- ADICIONAR SEU CÓDIGO AQUI --------------#
    #observe a endentação

    #não esqueça do return...
#--------------------------------------------------#


#**PROGRAMA PRINCIPAL *******************************#

#--DOCTEST -------#
# Comente esta parte durante o desenvolvimento
# caso queira pular o teste automático da função
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True,report=False)
#------------------#
