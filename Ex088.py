from time import sleep
from random import randint
lista_de_jogos = []
jogos = []
print('-'*30)
print(f'{" JOGA NA MEGA SENA ":^30}')
print('-'*30)
n = int(input('Quantos jogos você quer que eu sorteie? '))
print('=-' * 3, f' SORTEANDO {n} JOGOS ','-=' * 3)
for i in range(0, n):
    for j in range(0, 6):
        n = randint(0,60)
        if n not in jogos:
            jogos.append(n)
    lista_de_jogos.append(jogos[:])
    print(f'Jogo {i+1}: {jogos}')
    jogos.clear()
    sleep(1)
print('=-'*5,end='')
print(f'{" BOA SORTE! ":^15}',end='')
print('=-'*5)
#print(lista_de_jogos)
lista = list()
jogos = list()
print('-' * 30, end='')
print(f"{' JOGA NA MEGA SENA ':^5}",end='')
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f' SORTEANDO {quant} JOGOS ', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l} ')
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)