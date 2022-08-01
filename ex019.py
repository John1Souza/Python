from random import choice


a = input('Digite o nome do aluno: ')
b = input('Digite outro: ')
c = input('Digite outro: ')
d = input('Digite o último: ')
rand = choice([a, b, c, d])
print(f'O aluno sorteado foi {rand}')
