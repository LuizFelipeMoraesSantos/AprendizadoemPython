from random import randint
from time import sleep


def sorteia(lista):
    print(f'Sorteando 5 valores da lista: ', end=' ')
    for c in range(0, 5):
        n = randint(1, 30)
        lista.append(n)
        print(f"{n}", end=' ', flush=True)
        sleep(0.5)
    print('PRONTO')


def sorteia_somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores par da lista {lista}, o resultado foi {soma}')
#programa principal

numero = list()
sorteia(numero)
sorteia_somaPar(numero)