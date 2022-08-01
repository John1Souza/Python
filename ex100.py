from random import randint
from time import sleep


def lista(lst):
    soma_par = 0
    print(f'Sorteando 5 valores da lista: ', end='')
    for i in lst:
        if i % 2 == 0:
            soma_par += i
        print(i, end=' ')
        sleep(0.5)
    print('PRONTO!')
    print(f'Somando os valores pares de {lst}, temos {soma_par}')


# Programa Principal

numeros = [randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)]
lista(numeros)

def sorteia(lista):
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    for valores in lista:
        if valores % 2 == 0:
            soma += valores
    print(f'Somando os valores pares de {lista}, temos {soma}')


numeros = list()
sorteia(numeros)
somaPar(numeros)
