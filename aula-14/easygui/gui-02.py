import easygui as gui

choices=["Ser Feliz", "Ter Saúde", "Ficar Rico", "Todas as Alternativas"]

def MenuPrincipal(botoes):
    msg="Escolha sua opção:"
    title="Exemplo de Menu"
    image=None
    default_choice="Ser Feliz"
    cancel_choice="Ter Saúde"

    opcao = gui.indexbox(msg,title,botoes,image,default_choice,cancel_choice)

    return opcao

opcaoMenu = MenuPrincipal(choices)

gui.msgbox("Opção Escolhida: " + str(opcaoMenu) + " = " + choices[opcaoMenu])
