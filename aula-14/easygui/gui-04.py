import easygui as gui
import pickle

def GravarMatrizDisco(matriz,nome):
    output = open(nome,'wb')
    pickle.dump(matriz,output)
    output.close()


#####################
matriz = [["-" for x in range(4)]for x in range(26)]
GravarMatrizDisco(matriz,"AviaoVoo345")
