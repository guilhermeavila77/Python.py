import pandas as pd
import PySimpleGUI as sg

def gui():

    caminho = "ToDoList.xlsx"
    tabela_enviar = pd.read_excel(caminho, sheet_name='Enviar')
    tabela_analise = pd.read_excel(caminho, sheet_name='Analise')
    tabela_aprovados = pd.read_excel(caminho, sheet_name='Aprovados')
    tabela_recusados = pd.read_excel(caminho, sheet_name='Recusados')

    enviar_analise = tabela_enviar['NOME']
    em_analise = tabela_analise['NOME']
    recusado = tabela_recusados['NOME']
    aprovados = tabela_aprovados['NOME']

    lista_enviar = enviar_analise.tolist()
    lista_analise = em_analise.tolist()
    lista_recusado = recusado.tolist()
    lista_aprovados = aprovados.tolist()

    writer = pd.ExcelWriter(caminho, engine='xlsxwriter')

    print(lista_enviar)
    print(lista_analise)
    print(lista_recusado)
    print(lista_aprovados)

    tamanho = (300, 200)
    tamanho_frame = (300, 400)
    tamanho_list = (300, 300)

    layout_enviar = [
        [sg.Combo(lista_enviar, key='enviar')],
        [sg.Listbox(lista_enviar, size=tamanho_list)]
    ]

    layout_enviar_frame = [
        [sg.Frame("ENVIAR ANALISE", layout_enviar, size=tamanho_frame)],
        [sg.Button("EM ANALISE")]
    ]

    layout_analise = [
        [sg.Combo(lista_analise, size=tamanho, key='analise')],
        [sg.Listbox(lista_analise, size=tamanho_list)]
    ]

    layout_analise_frame = [
        [sg.Frame("EM ANALISE", layout_analise, size=tamanho_frame)],
        [sg.Button("APROVADO"), sg.Button("RECUSADO")]
    ]

    layout_recusado = [
        [sg.Combo(lista_recusado, size=tamanho, key='recusado')],
        [sg.Listbox(lista_recusado, size=tamanho_list)]
    ]

    layout_recusado_frame = [
        [sg.Frame("RECUSADOS", layout_recusado, size=tamanho_frame)],
        [sg.Button("REMOVER RECUSADO")]
    ]

    layout_aprovados = [
        [sg.Combo(lista_aprovados, size=tamanho, key='aprovado')],
        [sg.Listbox(lista_aprovados, size=tamanho_list)]
    ]

    layout_aprovados_frame = [
        [sg.Frame("APROVADOS", layout_aprovados, size=tamanho_frame)],
        [sg.Button("REMOVER APROVADO")]
    ]

    layout_kanban = [
        [sg.Column(layout_enviar_frame, justification='c'), sg.Column(layout_analise_frame, justification='c'), sg.Column(
            layout_recusado_frame, justification='c'), sg.Column(layout_aprovados_frame, justification='c')]
    ]

    window_cadastro = sg.Window("FLUXO DE OPERAÇÕES", layout_kanban)

    while True:
        evento, valores = window_cadastro.read()
        if evento == sg.WIN_CLOSED:
            break

        if evento == "EM ANALISE":
            env = str(valores['enviar'])
            n = lista_enviar.index(env)

            tabela_enviar = tabela_enviar.drop(n)
            print(tabela_enviar)

            tabela_analise = tabela_analise.append({'NOME' : env}, ignore_index=True)
            print(tabela_analise)

            tabela_enviar.to_excel(writer, sheet_name='Enviar', index=False)
            tabela_analise.to_excel(writer, sheet_name='Analise', index=False)
            tabela_aprovados.to_excel(writer, sheet_name='Aprovados', index=False)
            tabela_recusados.to_excel(writer, sheet_name='Recusados', index=False)

            writer.save()
            window_cadastro.close()

        if evento == "APROVADO":
            aprovado = str(valores['analise'])
            print(aprovado)
            n = lista_analise.index(aprovado)

            tabela_analise = tabela_analise.drop(n)
            print(tabela_analise)

            tabela_aprovados = tabela_aprovados.append({'NOME' : aprovado}, ignore_index=True)
            print(tabela_aprovados)

            tabela_enviar.to_excel(writer, sheet_name='Enviar', index=False)
            tabela_analise.to_excel(writer, sheet_name='Analise', index=False)
            tabela_aprovados.to_excel(writer, sheet_name='Aprovados', index=False)
            tabela_recusados.to_excel(writer, sheet_name='Recusados', index=False)

            writer.save()
            window_cadastro.close()

        if evento == "RECUSADO":
            recusado = str(valores['analise'])
            n = lista_analise.index(recusado)

            tabela_analise = tabela_analise.drop(n)
            print(tabela_analise)

            tabela_recusados = tabela_recusados.append({'NOME' : recusado}, ignore_index=True)
            print(tabela_recusados)

            tabela_enviar.to_excel(writer, sheet_name='Enviar', index=False)
            tabela_analise.to_excel(writer, sheet_name='Analise', index=False)
            tabela_aprovados.to_excel(writer, sheet_name='Aprovados', index=False)
            tabela_recusados.to_excel(writer, sheet_name='Recusados', index=False)

            writer.save()
            window_cadastro.close()

        if evento == "REMOVER RECUSADO":
            rec = str(valores['recusado'])
            n = lista_recusado.index(rec)

            tabela_recusados = tabela_recusados.drop(n)
            print(tabela_recusados)

            tabela_enviar.to_excel(writer, sheet_name='Enviar', index=False)
            tabela_analise.to_excel(writer, sheet_name='Analise', index=False)
            tabela_aprovados.to_excel(writer, sheet_name='Aprovados', index=False)
            tabela_recusados.to_excel(writer, sheet_name='Recusados', index=False)

            writer.save()
            window_cadastro.close()

        if evento == "REMOVER APROVADO":
            aprov = str(valores['aprovado'])
            n = lista_aprovados.index(aprov)

            tabela_aprovados = tabela_aprovados.drop(n)
            print(tabela_aprovados)

            tabela_enviar.to_excel(writer, sheet_name='Enviar', index=False)
            tabela_analise.to_excel(writer, sheet_name='Analise', index=False)
            tabela_aprovados.to_excel(writer, sheet_name='Aprovados', index=False)
            tabela_recusados.to_excel(writer, sheet_name='Recusados', index=False)

            writer.save()
            window_cadastro.close()

    window_cadastro.close()

gui()