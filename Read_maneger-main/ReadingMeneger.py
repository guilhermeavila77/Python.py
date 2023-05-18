from os import remove


livros_lidos = list()
progresso = list()
comand = input("Guilherme# ")

if comand == 'w livros':
    for cont in range(0, 1):
        livros_lidos.append(input('Qual o livro terminado? '))
    with open('LivrosLidos.txt', 'a') as arquivo:
        for nome in livros_lidos:
            arquivo.write(str(nome)+'\n')
elif comand == 'ls livros':
    with open('LivrosLidos.txt', 'r') as arquivo:
        for nome in arquivo:
            print(nome)
elif comand == 'progresso':
    progressostg = input('Deseja adicionar ou editar? ')
    if progressostg == 'add':
        for cont in range(0, 1):
            progresso.append(input('Qual livro? '))
            newpage = input(str('Pagina atual? '))
        with open('progresso.txt', 'a') as arquivo:
            for nome in progresso:
                arquivo.write(str(nome) + str(newpage)+'\n')
    elif progressostg == 'edit':
        progresso = list(open('progresso.txt'))
        livrinho = input(str('Qual o livro? '))
        newpage = input(str('Pagina atual? '))
        newline = str(livrinho + newpage)
        progresso.append(newline)
        with open('progresso.txt', 'r') as arquivo:
            mensagem = arquivo.readlines()
            for linha in mensagem:
                if livrinho in linha:
                    progresso.remove(linha)
        with open('progresso.txt', 'w') as arquivo:
            for nome in progresso:
                arquivo.write(nome)
    elif progressostg == 'ls progresso':
        with open('progresso.txt', 'r') as arquivo:
            for nome in arquivo:
                print(nome)
elif comand == 'remove':
    livros_lidos = list(open('LivrosLidos.txt'))
    rb = input(str('Qual livro remover? '))
    removebook = str(rb + '\n')
    for book in livros_lidos:
        if book == removebook:
            livros_lidos.remove(book)
            print(livros_lidos)
            with open('LivrosLidos.txt', 'w') as arquivo:
                for nome in livros_lidos:
                    arquivo.write(nome)
