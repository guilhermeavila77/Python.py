import random
numeros = ["", "", "", "", "", ""]

print('Você gostaria de ver os numeros?')
input_do_usuario = input()

if (input_do_usuario == 'SIM'):
    for i in range(6):
        nrandom = random.randrange(60)
        numeros[i] = nrandom

resultado = sorted(numeros)
print(resultado)
