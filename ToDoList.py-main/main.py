import PySimpleGUI as sg

def nova_janela():
    
    sg.theme('DarkAmber')
    layout_linha = [
        [sg.Checkbox(''), sg.Input('')]
    ]

    layout_main = [
        [sg.Frame('tarefas', layout=layout_linha, key='kontein')],
        [sg.Button('NOVA TAREFA'), sg.Button('RESET')]
    ]

    return sg.Window('ToDoList', layout=layout_main, finalize=True)

janela = nova_janela()

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED:
        break

    elif evento == 'NOVA TAREFA':
        janela.extend_layout(janela['kontein'], [[sg.Checkbox(''), sg.Input('')]])

    elif evento == 'RESET':
        janela.close()
        janela = nova_janela()


janela.close()