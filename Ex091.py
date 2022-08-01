'''print(' Valores sorteados: ')
dict = dict()

dict['Jogador1'] = randint(1, 6)
print(f'O jogador1 tirou {dict["Jogador1"]}')
sleep(1)
dict['Jogador2'] = randint(1, 6)
print(f'O jogador2 tirou {dict["Jogador2"]}')
sleep(1)
dict['Jogador3'] = randint(1, 6)
print(f'O jogador3 tirou {dict["Jogador3"]}')
sleep(1)
dict['Jogador4'] = randint(1, 6)
print(f'O jogador4 tirou {dict["Jogador4"]}')
mai = men = 0
for k, v in dict.items():
    if k == 'Jogador1':
        mai = men = v
    else:
        if v > mai:
            mai = v
            print(k)
        if v < men:
            men = v
            print(k)
print(mai, men)'''

from random import randint
from time import sleep
from operator import itemgetter
jogo = {
    'jogador1':randint(1, 6),
    'jogador2':randint(1, 6),
    'jogador3':randint(1, 6),
    'jogador4':randint(1, 6)
}
ranking = list()
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('=-'*30)
print('  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'  {i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)