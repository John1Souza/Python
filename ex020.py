from random import shuffle


a1 = str(input('Digite o nome do aluno: '))
a2 = str(input('Digite outro: '))
a3 = str(input('Digite outro: '))
a4 = str(input('Digite o último: '))
lista = [a1, a2, a3, a4]
shuffle(lista)
print(f'A ordem de apresentação será {lista}')

