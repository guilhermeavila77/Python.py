import random

nrandom = random.randrange(1000)

while nrandom:
    numero_chutado = int(input('Chute algum numero: '))
    if (nrandom == numero_chutado):
        print('Numero correto')
        break
    if (nrandom < numero_chutado):
        print('Numero menor')
    if (nrandom > numero_chutado):
        print('Numero maior')
