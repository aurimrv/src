import easygui as gui

def MostrarReservas():
    msg="Bem Vindo ao Air Civil/UFSCar"
    title="Air Civil UFSCar - Reserva de Assentos"

    text=''
    for i in range(0,10):
        text = text + "Fila " + str(i) + "-->"
        for j in range(0,4):
            if (i%2) == 0:
                text = text + str(j) + "(X) "
            else:
                text = text + str(j) + "( ) "

            if (j==1): #corredor
                text = text + "  "
        text = text + "\n"
        
    gui.codebox(msg,title,text)

MostrarReservas()
