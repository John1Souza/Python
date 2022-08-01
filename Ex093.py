'''jogador = dict()


jogador["nome"] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
soma = 0
lista_gols = []
for i in range(0, partidas):
    n = int(input(f'Quantos gols na partida {i}? '))
    lista_gols.append(n)
    soma += n
jogador["gols"] = lista_gols
jogador["total"] = soma
print('=-'*30)
print(jogador)
print('=-'*30)
print(f'O campo nome tem o valor {jogador["nome"]}.')
print(f'O campor gols tem o valor {jogador["gols"]}.')
print(f'O campo total tem o valor {jogador["total"]}.')
print('=-'*30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for j in range(0, partidas):
    print(f'{"=> Na partida":>15}',end='')
    print(f' {j}, fez {lista_gols[j]} gols.')
print(f'Foi um total de {jogador["total"]} gols.')'''

jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for c in range(0, tot):
    partidas.append(int(input(f'   Quantos gols na partida {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador['gols']):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols')
