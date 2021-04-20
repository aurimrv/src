#Ex5: Uma forma inocente de criptografar uma mensagem é simplesmente trocar um
#    simbolo por outro, de acordo com alguma regra. Neste contexto, faça duas
#    funções, sendo uma que receba uma mensagem  de texto e devolva a mensagem
#    criptografada, e outra que receba a mensagem criptografada a devolva
#    descriptografada.
# Assuma as seguintes regras para criptografar a mensagem:
# i) mensagem original contém somente as letras entre 'a' e 'z' (minúsculas), espaço e ponto
# ii) Para criptografar a mensagem use as seguintes regras:
#      1) trocar espaço por P
#      2) trocar ponto  por E
#      3) trocar cada letra pela letra 5 posições à frente no alfabeto. Considere
#         o alfabeto como uma lista circular, ou seja, ao encontrar o 'z', volte para
#         o 'a' na contagem
#         Ex: a->f, b->h, t->a, u->b
#
#  Para descriptografar a mensagem aplique as regras inversas.
#
#  Como dica, para facilitar a manipulação da mensagem em texto, transforme a string
#  num vetor de caracteres com o comando list
#          vetor_caracteres = list('abcdefghijklmnopqrstuvwxyz')
#  agora vetor_caracteres tem a forma de vetor --> ['a','b',....,'z']
#  E para transforma um vetor de caracteres numa string use o comando join:
#                    vet = ['a','b','z']
#                    str = "".join(vet)  --> e str será 'abz'
#                      

def crypt(str):
    '''
    >>> crypt('abcdefghijklmnopqrstuvwxyz .')
    'fghijklmnopqrstuvwxyzabcdePE'
    '''
#------ ADICIONAR SEU CÓDIGO AQUI -------------#
    #observe a endentação

    #não esqueça do return...
#-----------------------------------------------#

def decrypt(str):
    '''
    >>> decrypt('fghijklmnopqrstuvwxyzabcdePE')
    'abcdefghijklmnopqrstuvwxyz .'
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
